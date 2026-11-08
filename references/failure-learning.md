# Failure Learning: testen, verstehen, gezielt verbessern

**Voraussetzung:** eine Feedbackquelle (SKILL.md Abschnitt 6). Ohne sie keine Schleife simulieren, sondern das Ergebnis als unverifiziert kennzeichnen. Begriffe (Versuch, Ansatz, gescheitert), die drei Zähler und die Abbruchgrenzen regelt ebenfalls Abschnitt 6; hier stehen nur Ablauf und Logformat.

## Vor dem ersten Versuch
- Qualitätskriterien als prüfbare Liste (Kriterium | Messmethode | Schwelle), mindestens für jedes Muss.
- Wo möglich automatisch prüfen (Skript, Test, Diff, Metrik), sonst feste Sichtprüfung mit Checkliste.

## Schleife
0. Zähler prüfen (Abschnitt 6). Grenze erreicht: kein Versuch, stoppen und berichten.
1. Test ausführen, Rohergebnis sichern.
2. Fehler klassifizieren: Eingabe · Logik · Werkzeug/Umgebung · Anforderung falsch verstanden · Geschmack.
3. Ursache benennen (eine Ebene tiefer als das Symptom).
4. Nur die verursachende Komponente ändern.
5. Erneut testen, Ergebnis gegen vorher und gegen den Mindestfortschritt vergleichen. Zähler aktualisieren.

Ein bestandener Test belegt nur das Kriterium, das er geprüft hat. Nie denselben Versuch wiederholen; vor einem neuen Versuch den bekannten Logstand nutzen und nur neue Einträge lesen.

## Log
In `TEST_RESULTS.md`, sobald Projektgedächtnis besteht; sonst im Chat. Die Zähler stehen zusätzlich in `PROGRESS.md`.
```
### V<n> · <Datum> · Ansatz A<n> · <Komponente>
Hypothese: …
Aktion: …
Ergebnis: bestanden / nicht bestanden (Messwert) · Mindestfortschritt: ja/nein · Ansatz widerlegt: ja/nein (Beleg)
Ursache: …
Zähler danach: Budget <x>/<gesamt> · gescheiterte Ansätze <y>/3 · Serie ohne Fortschritt <z>/2
Nächster Versuch / Regel abgeleitet: …
```
Ungelöstes bleibt mit Status „offen“ im Log.
