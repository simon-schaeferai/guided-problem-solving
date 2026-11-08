Du testest den Claude-Code-Skill `guided-problem-solving`. Arbeite so, als hätte der User diesen Skill gerade für die Aufgabe unten aufgerufen. Lies zuerst `{SKILL}` vollständig; Dateien daneben unter `references/` und `templates/` nur, wenn der Skill es für deinen Fall vorsieht. Dann löse die Aufgabe wirklich, mit echten Werkzeugaufrufen, genau nach dem Skill.

Aufgabe des Users (wörtlich): „{AUFTRAG}“

Testbedingungen:
- Dein Arbeitsverzeichnis `{CWD}` ist der Ordner, in dem der User gerade arbeitet. Schreibe nur unterhalb von `{CASE_DIR}`.
- `{CASE_DIR}/desktop` ersetzt in diesem Test den Desktop (`~/Desktop`). Schreibe nie auf den echten Desktop.
- Keine extern wirksamen oder kostenpflichtigen Aktionen. Ändere die Skill-Dateien nicht.
- Der User ist nicht erreichbar. Fragen, die du laut Skill stellen würdest, schreibst du wörtlich in den Bericht und machst so weiter, wie der Skill es ohne Antwort vorschreibt.
{ZUSATZ}

Schreibe zum Schluss deinen Bericht nach `{BERICHT}` (kompakt, Deutsch): Ergebnis mit Beleg, Klasse mit Grund, Strategie, gestellte Fragen wörtlich mit Art, freigabepflichtige Aktionen, angelegte oder geänderte Dateien, Regeln, die gebremst oder verwirrt haben (Datei:Zeile). Die letzten vier Zeilen des Berichts sind genau dieser Block, ausgefüllt:

KLASSE: <S|M|L>
FRAGEN: <Anzahl Discovery- und Interviewfragen>
BLOCKER: <Anzahl Blocker-Fragen>
FREIGABEN_ANGEFRAGT: <Anzahl>
