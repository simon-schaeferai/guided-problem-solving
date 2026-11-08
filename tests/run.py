#!/usr/bin/env python3
"""Testreihe für den Skill guided-problem-solving.

Kopiert jeden Fall in einen frischen Sandbox-Ordner, lässt ihn von Claude Code
ohne Oberfläche (`claude -p`) nach dem Skill bearbeiten und prüft danach das
Ergebnis mit check.py.

Aufruf:
  python3 tests/run.py                  # alle Fälle nacheinander
  python3 tests/run.py 01-bugfix 05-fortsetzung --parallel 2
  python3 tests/run.py --nur-vorbereiten  # Sandbox anlegen, Prompts zeigen, nichts ausführen
  python3 tests/run.py --pruefen <lauf-ordner>  # nur prüfen, z. B. nach manuellem Lauf
"""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

HIER = pathlib.Path(__file__).resolve().parent
REPO = HIER.parent
FAELLE = HIER / "cases"

ERLAUBTE_BEFEHLE = ["python3", "ls", "cat", "head", "tail", "wc", "diff", "grep",
                    "find", "mkdir", "file", "md5", "md5sum", "git check-ignore"]


def pruefsummen(ordner: pathlib.Path) -> dict:
    ergebnis = {}
    for p in sorted(ordner.rglob("*")):
        if p.is_file():
            ergebnis[str(p.relative_to(ordner))] = hashlib.md5(p.read_bytes()).hexdigest()
    return ergebnis


def vorbereiten(fall: str, lauf: pathlib.Path) -> dict:
    quelle = FAELLE / fall
    definition = json.loads((quelle / "case.json").read_text(encoding="utf-8"))
    ziel = lauf / fall
    shutil.copytree(quelle / "fixture", ziel)
    for p in ziel.rglob("*"):
        if p.is_file():
            try:
                text = p.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if "{CASE_DIR}" in text:
                p.write_text(text.replace("{CASE_DIR}", str(ziel)), encoding="utf-8")
    (ziel / ".." / f".{fall}.vorher.json").resolve().write_text(json.dumps(pruefsummen(ziel)), encoding="utf-8")
    cwd = ziel / definition.get("cwd", "projekt")
    zusatz = definition.get("zusatz", "")
    prompt = (HIER / "prompt.md").read_text(encoding="utf-8").format(
        SKILL=REPO / "SKILL.md",
        AUFTRAG=definition["auftrag"],
        CWD=cwd,
        CASE_DIR=ziel,
        ZUSATZ=f"- {zusatz}" if zusatz else "",
        BERICHT=lauf / f"{fall}.bericht.md",
    )
    return {"fall": fall, "ziel": ziel, "cwd": cwd, "prompt": prompt}


def ausfuehren(job: dict, lauf: pathlib.Path, modell: str | None, timeout: int) -> dict:
    pfade = {str(lauf), str(lauf.resolve())}
    erlaubt = ["Read", "Glob", "Grep", "TodoWrite"]
    erlaubt += [f"{tool}(/{p}/**)" for p in pfade for tool in ("Edit", "Write")]
    erlaubt += [f"Bash({b}:*)" for b in ERLAUBTE_BEFEHLE]
    befehl = ["claude", "-p", job["prompt"], "--output-format", "json",
              "--add-dir", str(lauf), "--add-dir", str(REPO),
              "--allowedTools", *erlaubt,
              "--disallowedTools", "WebFetch", "WebSearch",
              "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}']
    if modell:
        befehl += ["--model", modell]
    start = datetime.datetime.now()
    try:
        proc = subprocess.run(befehl, cwd=job["cwd"], capture_output=True, text=True, timeout=timeout)
        ausgabe, code = proc.stdout, proc.returncode
        if proc.stderr:
            (lauf / f"{job['fall']}.stderr.txt").write_text(proc.stderr, encoding="utf-8")
    except subprocess.TimeoutExpired:
        ausgabe, code = "", "timeout"
    (lauf / f"{job['fall']}.claude.json").write_text(ausgabe or "{}", encoding="utf-8")
    return {"fall": job["fall"], "code": code, "sekunden": (datetime.datetime.now() - start).seconds}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("faelle", nargs="*", help="Fall-IDs, leer = alle")
    ap.add_argument("--parallel", type=int, default=1)
    ap.add_argument("--modell", default=None)
    ap.add_argument("--timeout", type=int, default=900, help="Sekunden je Fall")
    ap.add_argument("--nur-vorbereiten", action="store_true")
    ap.add_argument("--pruefen", metavar="LAUF", help="nur check.py auf einen vorhandenen Lauf-Ordner")
    args = ap.parse_args()

    if args.pruefen:
        return subprocess.call([sys.executable, str(HIER / "check.py"), args.pruefen])

    faelle = args.faelle or sorted(p.name for p in FAELLE.iterdir() if (p / "case.json").exists())
    lauf = (pathlib.Path(tempfile.gettempdir()) / "gps-tests" / datetime.datetime.now().strftime("%Y%m%d-%H%M%S")).resolve()
    lauf.mkdir(parents=True)
    (lauf / ".start").touch()
    jobs = [vorbereiten(f, lauf) for f in faelle]
    print(f"Lauf-Ordner: {lauf}")

    if args.nur_vorbereiten:
        for j in jobs:
            print(f"\n--- {j['fall']} (cwd {j['cwd']}) ---\n{j['prompt']}")
        return 0

    if shutil.which("claude") is None:
        print("claude CLI nicht gefunden", file=sys.stderr)
        return 2
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.parallel) as pool:
        for r in pool.map(lambda j: ausfuehren(j, lauf, args.modell, args.timeout), jobs):
            print(f"{r['fall']}: Exit {r['code']}, {r['sekunden']} s")
    return subprocess.call([sys.executable, str(HIER / "check.py"), str(lauf)])


if __name__ == "__main__":
    sys.exit(main())
