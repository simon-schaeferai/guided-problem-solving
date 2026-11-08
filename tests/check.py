#!/usr/bin/env python3
"""Prüft einen Lauf der Testreihe. Aufruf: python3 tests/check.py <lauf-ordner>

Je Fall: allgemeine Prüfungen aus case.json (Klasse, Fragen, Gedächtnis,
neue Dateien, unveränderte Dateien, Pflichtwörter im Bericht) und eine
fallspezifische Ergebnisprüfung. Exit 0 nur, wenn alles grün ist.
"""
import csv
import hashlib
import io
import json
import pathlib
import re
import subprocess
import sys
import tempfile

HIER = pathlib.Path(__file__).resolve().parent
FAELLE = HIER / "cases"


def md5(p: pathlib.Path) -> str:
    return hashlib.md5(p.read_bytes()).hexdigest()


def block(bericht: str) -> dict:
    werte = {}
    for schluessel in ("KLASSE", "FRAGEN", "BLOCKER", "FREIGABEN_ANGEFRAGT"):
        m = re.findall(rf"^\s*\**{schluessel}\**\s*:\s*\**\s*([A-Za-z0-9]+)", bericht, re.M)
        if m:
            werte[schluessel] = m[-1]
    return werte


# ---------- fallspezifische Ergebnisprüfungen ----------

def ergebnis_01(ziel: pathlib.Path) -> list:
    skript = ziel / "projekt" / "wortzaehler.py"
    fehler = []
    r = subprocess.run([sys.executable, "-I", "-B", str(skript), str(ziel / "projekt" / "beispiel.txt")],
                       capture_output=True, text=True)
    if r.returncode != 0 or r.stdout.strip() != "7":
        fehler.append(f"beispiel.txt: erwartet 7, bekommen {r.stdout.strip()!r} (Exit {r.returncode})")
    with tempfile.TemporaryDirectory() as t:
        probe = pathlib.Path(t) / "probe.txt"
        probe.write_text("Äpfel\nund  Birnen\tund Öl\n", encoding="utf-8")
        r = subprocess.run([sys.executable, "-I", "-B", str(skript), str(probe)], capture_output=True, text=True)
        if r.returncode != 0 or r.stdout.strip() != "5":
            fehler.append(f"Gegenprobe (Zeilenumbruch, Tab, doppeltes Leerzeichen): erwartet 5, bekommen {r.stdout.strip()!r}")
    return fehler


def ergebnis_02(ziel: pathlib.Path) -> list:
    projekt = ziel / "projekt"
    kandidaten = [p for p in projekt.glob("*.csv") if p.name not in ("kunden_jan.csv", "kunden_feb.csv")]
    if not kandidaten:
        return ["keine zusammengeführte CSV gefunden"]
    for p in kandidaten:
        text = p.read_text(encoding="utf-8-sig")
        try:
            dialekt = csv.Sniffer().sniff(text.splitlines()[0])
        except csv.Error:
            continue
        zeilen = list(csv.DictReader(io.StringIO(text), dialect=dialekt))
        spalte = next((k for k in (zeilen[0].keys() if zeilen else []) if "mail" in k.lower()), None)
        if not spalte:
            continue
        mails = [z[spalte].strip().lower() for z in zeilen]
        if sorted(mails) == ["anna@example.com", "ben@example.com", "cara@example.com", "dora@example.com"]:
            return []
        return [f"{p.name}: erwartet 4 eindeutige Kunden, bekommen {mails}"]
    return ["keine lesbare Kundenliste mit E-Mail-Spalte gefunden"]


def ergebnis_05(ziel: pathlib.Path) -> list:
    fehler = []
    progress = (ziel / "desktop" / "2026-11-01-rechnungsimport-k3f9" / "PROGRESS.md").read_text(encoding="utf-8")
    f1 = next((z for z in progress.splitlines() if z.startswith("| F1")), "")
    if "ausgelöst" not in f1.lower() and "klärung" not in f1.lower():
        fehler.append(f"F1 steht weder auf „ausgelöst“ noch auf „wartet auf Klärung“: {f1[-120:]!r}")
    if "klärung" not in progress.lower() and "blockiert" not in progress.lower():
        fehler.append("nächster Schritt ist weder „wartet auf Klärung“ noch „blockiert“")
    if re.search(r"\|\s*frei\s*\|", f1):
        fehler.append("F1 wurde wieder auf „frei“ gesetzt")
    if not re.search(r"Gescheiterte Ansätze\s*\|\s*\**2", progress):
        fehler.append("Zähler „Gescheiterte Ansätze“ steht nicht mehr auf 2")
    return fehler


ERGEBNIS = {"01-bugfix": ergebnis_01, "02-csv": ergebnis_02, "05-fortsetzung": ergebnis_05}


def pruefe_fall(lauf: pathlib.Path, fall: str) -> tuple:
    definition = json.loads((FAELLE / fall / "case.json").read_text(encoding="utf-8"))
    e = definition["erwartet"]
    ziel = lauf / fall
    vorher = json.loads((lauf / f".{fall}.vorher.json").read_text(encoding="utf-8"))
    fehler, hinweise = [], []

    bericht_pfad = lauf / f"{fall}.bericht.md"
    bericht = bericht_pfad.read_text(encoding="utf-8") if bericht_pfad.exists() else ""
    if not bericht:
        fehler.append("kein Bericht geschrieben")
    b = block(bericht)
    if b.get("KLASSE") not in e["klasse"]:
        fehler.append(f"Klasse {b.get('KLASSE')!r}, erwartet {e['klasse']}")
    for schluessel, grenze in (("FRAGEN", "max_fragen"), ("BLOCKER", "max_blocker")):
        wert = b.get(schluessel)
        if wert is None or not wert.isdigit():
            fehler.append(f"{schluessel} fehlt im Block")
        elif int(wert) > e[grenze]:
            fehler.append(f"{schluessel} {wert}, höchstens {e[grenze]}")

    for rel in e.get("unveraendert", []):
        p = ziel / rel
        if not p.exists() or md5(p) != vorher.get(rel):
            fehler.append(f"{rel} wurde verändert oder gelöscht")

    jetzt = {str(p.relative_to(ziel)) for p in ziel.rglob("*") if p.is_file() and "__pycache__" not in p.parts}
    neu = sorted(jetzt - set(vorher))
    neu_im_desktop = [n for n in neu if n.startswith("desktop/")]
    neu_sonst = [n for n in neu if not n.startswith("desktop/")]
    if e.get("kein_gedaechtnis") and neu_im_desktop:
        fehler.append(f"unnötiges Projektgedächtnis: {neu_im_desktop}")
    if len(neu_sonst) > e["max_neue_dateien"]:
        fehler.append(f"{len(neu_sonst)} neue Dateien, höchstens {e['max_neue_dateien']}: {neu_sonst}")

    for wort in e.get("bericht_enthaelt", []):
        if wort.lower() not in bericht.lower():
            fehler.append(f"Bericht nennt „{wort}“ nicht")
    eins = e.get("bericht_enthaelt_eins")
    if eins and not any(w.lower() in bericht.lower() for w in eins):
        fehler.append(f"Bericht nennt keins von {eins}")

    if fall in ERGEBNIS:
        try:
            fehler += ERGEBNIS[fall](ziel)
        except Exception as ex:  # Prüfung selbst darf den Lauf nicht abbrechen
            fehler.append(f"Ergebnisprüfung fehlgeschlagen: {ex}")

    metrik = {}
    roh = lauf / f"{fall}.claude.json"
    if roh.exists():
        try:
            j = json.loads(roh.read_text(encoding="utf-8") or "{}")
            metrik = {"turns": j.get("num_turns"), "sek": round((j.get("duration_ms") or 0) / 1000),
                      "usd": j.get("total_cost_usd")}
        except json.JSONDecodeError:
            hinweise.append("claude.json nicht lesbar")
    return fehler, hinweise, b, metrik


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    lauf = pathlib.Path(sys.argv[1]).resolve()
    faelle = sorted(p.name[1:-len(".vorher.json")] for p in lauf.glob(".*.vorher.json"))
    gesamt_ok = True

    desktop = pathlib.Path.home() / "Desktop"
    start = lauf / ".start"
    if desktop.is_dir() and start.exists():
        try:
            neu = [p.name for p in desktop.iterdir()
                   if p.stat().st_mtime > start.stat().st_mtime and p.name.startswith("20")]
        except PermissionError:
            neu = []
            print("Hinweis: ~/Desktop ist für diesen Prozess nicht lesbar (macOS-Datenschutz); Desktop-Prüfung übersprungen.")
        if neu:
            gesamt_ok = False
            print(f"FEHLER: Auf dem echten Desktop sind neue Projektordner entstanden: {neu}")

    print(f"{'Fall':<16} {'Ergebnis':<8} {'Klasse':<6} {'Fragen':<6} {'Turns':<6} {'Sek':<5}")
    details = []
    for fall in faelle:
        fehler, hinweise, b, m = pruefe_fall(lauf, fall)
        ok = not fehler
        gesamt_ok &= ok
        print(f"{fall:<16} {'grün' if ok else 'ROT':<8} {b.get('KLASSE', '?'):<6} {b.get('FRAGEN', '?'):<6} "
              f"{str(m.get('turns', '?')):<6} {str(m.get('sek', '?')):<5}")
        details += [f"  {fall}: {x}" for x in fehler] + [f"  {fall} (Hinweis): {x}" for x in hinweise]
    if details:
        print("\n" + "\n".join(details))
    print(f"\nGesamt: {'GRÜN' if gesamt_ok else 'ROT'} · Lauf-Ordner: {lauf}")
    return 0 if gesamt_ok else 1


if __name__ == "__main__":
    sys.exit(main())
