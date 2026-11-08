# Critical Review: ein Durchgang, dann handeln

Tiefe nach Arbeitsumfang: **S** nur der stille Kurzcheck auf Freigabepflicht (SKILL.md Abschnitt 1b), diese Tabelle entfällt. **M** nur die Zeilen, die das konkrete Risiko betreffen; Abhängigkeiten immer, wenn sie über Erfolg oder Kosten entscheiden. **L** die ganze Tabelle. Die Freigabeprüfung pro Aktion gilt in jeder Klasse.

| Frage | Prüfen |
|---|---|
| Was könnte scheitern? | Top 3 Ausfallszenarien mit Wahrscheinlichkeit und Folge |
| Unbelegte Annahmen? | Jede Annahme: belegt (Quelle) oder Hypothese (Testweg) |
| Fehlende Anforderungen? | Fehlerfall, Leerfall, Skalierung, Bedienung, Wartung, Kosten pro Lauf |
| Einfachere Lösung? | Was ist die 20-%-Lösung, die 80 % liefert? Gibt es das schon fertig? |
| Übersehene Abhängigkeiten? | Accounts, Lizenzen, Rate-Limits, Hardware, Dateiformate, andere Sessions/Repos |
| Qualitätshebel? | Wo entsteht der größte Qualitätsgewinn pro Aufwand? |
| Effizienzhebel? | Was lässt sich wiederverwenden, cachen, parallelisieren? |

Ergebnis: Liste „geändert / bewusst nicht geändert (Grund)". Ein zweiter Durchgang nur mit neuer Information.
