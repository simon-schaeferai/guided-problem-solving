# Einmalige Aktionen gegen Doppelausführung sichern

Gilt nur für freigabepflichtige Aktionen, die bei zweifacher Ausführung schaden (bezahlen, senden, veröffentlichen, buchen, anlegen) und deren Ergebnis sich nicht sicher am Zielsystem ablesen lässt. Alles andere braucht diese Datei nicht.

## Status einer einmaligen Freigabe
| Status | Bedeutung |
|---|---|
| **frei** | erteilt, noch nicht genutzt. Nur aus diesem Status darf ausgelöst werden. |
| **reserviert** | direkt vor dem Auslösen gesetzt |
| **ausgelöst** | Auslösung belegt (Job-ID, Bestätigung, Log). Die Freigabe ist damit verbraucht, auch wenn das Ergebnis noch offen ist. |
| **erledigt** | Ergebnis belegt (Ausgabe, Abrechnung, Zielsystem) |
| **abgebrochen** | vor dem Auslösen gestoppt, ohne Wirkung; damit wieder **frei** |
| **wartet auf Klärung** | Zustand nicht belegbar; der User klärt ihn oder erteilt eine neue Freigabe |

## Ablauf
1. Status in der Freigabe-Tabelle von `PROGRESS.md` führen. Gibt es noch kein Projektgedächtnis, für diese eine Aktion ein minimales `PROGRESS.md` (Kopf und Freigabe-Tabelle) anlegen; eine Chat-Notiz überlebt keine Unterbrechung.
2. „reserviert“ setzen, auslösen, sofort „ausgelöst“ mit Beleg eintragen, später „erledigt“ mit Beleg.
3. Ein Fehlschlag beim Anbieter nach der Auslösung zählt als Versuch; ein neuer Lauf braucht eine neue Freigabe, außer belegt ist, dass nichts ausgeführt und nichts berechnet wurde.

## Nach einer Unterbrechung
| Vorgefundener Status | Vorgehen |
|---|---|
| reserviert | Lesend prüfen, ob ausgelöst wurde (Zielsystem, Logs, Abrechnung, Ausgabedateien). Belegt nicht ausgelöst: **frei**, einmal auslösen. Belegt ausgelöst: **ausgelöst**. Unklar: **wartet auf Klärung**. |
| ausgelöst | Ergebnis nur lesend abholen. Nie erneut auslösen. Ergebnis nicht auffindbar: **wartet auf Klärung**. |
| wartet auf Klärung | Nichts auslösen. Den User mit dem Befund fragen (Blocker, einmal). |

Lesende Prüfungen, die Zugangsdaten brauchen, sind selbst freigabepflichtig, wenn die Freigabe sie nicht schon abdeckt.
