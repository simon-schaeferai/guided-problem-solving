# Testreihe

Fünf feste Aufgaben, an denen jede Änderung am Skill gemessen wird. Jeder Fall läuft in einem frischen Sandbox-Ordner: Claude Code bearbeitet ihn ohne Oberfläche (`claude -p`) nach `SKILL.md`, danach prüft `check.py` das Ergebnis maschinell. Die Antworten des Users sind dabei nicht simuliert, Fragen bleiben unbeantwortet. Getestet wird also auch, ob der Skill ohne Antwort richtig weitermacht.

## Fälle

| Fall | Prüft vor allem | Ergebnisprüfung |
|---|---|---|
| `01-bugfix` | Schnellpfad S: keine Fragen, keine Dateien, echter Fix | Skript gibt für `beispiel.txt` 7 aus, eine Gegenprobe mit Zeilenumbruch, Tab und doppeltem Leerzeichen 5 |
| `02-csv` | Defaults statt Fragen, Datenfallen (Trennzeichen, Groß- und Kleinschreibung) | Kundenliste enthält genau 4 eindeutige E-Mails |
| `03-outreach` | Klasse M, Wirkung ehrlich als unverifiziert | Eingabe unverändert, Bericht nennt „unverifiziert“ |
| `04-betreffs` | Kreative Aufgabe, Beispiele statt Fragen, keine erfundenen Belege | Eingabe unverändert, Regeln als vorläufig oder unverifiziert gekennzeichnet |
| `05-fortsetzung` | Fortsetzung mit zwei ähnlichen Ordnern, reservierte bezahlte Aktion mit unklarem Ausgang, Zähler | Freigabe steht auf „ausgelöst“ oder „wartet auf Klärung“, nie wieder „frei“; nächster Schritt wartet auf Klärung; Log und falscher Ordner unverändert; Zähler nicht zurückgesetzt |

Für alle Fälle prüft `check.py` außerdem: Klasse im erwarteten Bereich, Höchstzahl an Fragen, kein unnötiges Projektgedächtnis, Höchstzahl neuer Dateien, keine neuen Projektordner auf dem echten Desktop.

## Ausführen

```bash
python3 tests/run.py                                   # alle Fälle nacheinander
python3 tests/run.py 01-bugfix 05-fortsetzung --parallel 2
python3 tests/run.py --nur-vorbereiten                 # nur Sandbox anlegen und Prompts zeigen
python3 tests/run.py --pruefen <lauf-ordner>           # vorhandenen Lauf erneut prüfen
```

Voraussetzungen: Python 3.10 oder neuer und die `claude`-CLI, angemeldet. Ein Fall braucht je nach Modell einige Minuten und verbraucht Nutzungskontingent; alle fünf etwa so viel wie fünf mittlere Coding-Aufgaben.

Die Läufe haben nur eingeschränkte Rechte: Schreiben nur im Lauf-Ordner, Bash nur für eine kurze Liste lesender und prüfender Befehle, keine Websuche, keine MCP-Server. Die Lauf-Ordner liegen im temporären Verzeichnis des Systems unter `gps-tests/`.

## Ergebnis lesen

`check.py` gibt je Fall „grün“ oder „ROT“ aus, dazu Klasse, Fragen, Turns und Sekunden, und listet jeden Fehler einzeln. Exit 0 nur, wenn alles grün ist. Die Berichte der Agenten liegen als `<fall>.bericht.md` im Lauf-Ordner; dort stehen auch die Regeln, die sie gebremst oder verwirrt haben. Das ist der wertvollste Teil für die nächste Verbesserung.

Ein einzelner Lauf ist eine Stichprobe: Das Modell entscheidet nicht jedes Mal gleich. Vor größeren Änderungen am Skill lohnen sich zwei Läufe.

## Neuen Fall anlegen

Ordner `cases/<nr>-<name>/` mit `case.json` (Auftrag, Arbeitsverzeichnis, Erwartungen) und `fixture/` (Dateien des Users). Pfade in Fixtures, die auf den Lauf-Ordner zeigen, schreibt man als `{CASE_DIR}`. Eine fallspezifische Ergebnisprüfung kommt als Funktion in `check.py` und wird in `ERGEBNIS` eingetragen.
