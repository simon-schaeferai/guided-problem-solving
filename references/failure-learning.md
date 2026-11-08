# Failure Learning: Budget, Zähler, Abbruch

Gilt, sobald Versuche Geld oder erheblich Zeit kosten, ein Projektgedächtnis besteht oder mehr als 3 Versuche nötig werden (SKILL.md Abschnitt 6). Vorher reicht die einfache Schleife dort.

## Vor dem nächsten Versuch festlegen
Gesamtbudget (Versuche, Zeit, Kosten), Mindestfortschritt je Versuch und Qualitätskriterien (Kriterium | Messmethode | Schwelle). Kosten sind freigabepflichtig (SKILL.md 1b).

## Begriffe
- **Versuch:** eine Änderung plus eine Prüfung gegen die Feedbackquelle. Dieselbe Prüfung ohne Änderung erneut laufen zu lassen, ist kein neuer Versuch.
- **Ansatz:** ein Lösungsweg, erkennbar am Mechanismus (Werkzeug, Methode, Architektur). Andere Parameter oder ein neuer Name im selben Mechanismus sind derselbe Ansatz.
- **Ansatz gescheitert:** zwei Versuche in Folge ohne Mindestfortschritt **oder** ein Versuch, der die Voraussetzung des Ansatzes nachweislich widerlegt. Dann ist ein Ansatzwechsel Pflicht.

## Drei Zähler
| Zähler | Ändert sich | Grenze |
|---|---|---|
| Budget verbraucht (Versuche, Zeit, Kosten) | nach jedem Versuch | Gesamtbudget |
| Gescheiterte Ansätze | +1, wenn ein Ansatz scheitert | 3 |
| Serie ohne Mindestfortschritt | +1 ohne Fortschritt; 0 bei Fortschritt oder nach Ansatzwechsel | 2, dann gilt der Ansatz als gescheitert |

- Versuchsnummern laufen über Ansätze hinweg weiter.
- Kein Session-, Strategie- oder Namenswechsel setzt einen Zähler zurück. Kein Zähler wird ohne Beleg auf 0 gesetzt; ein nicht belegbarer Stand heißt **unbekannt**.
- Ein ausgelöster, aber noch ungeprüfter Versuch zählt im Budget mit der Obergrenze seiner Freigabe, bis die echten Kosten belegt sind.
- Bei Projektgedächtnis stehen die Zähler in `PROGRESS.md`, Details je Versuch in `TEST_RESULTS.md`.

## Schleife
0. Zähler prüfen. Endgültig stoppen, wenn 3 Ansätze gescheitert sind oder das Budget erreicht ist: keinen Versuch starten, sondern berichten (was versucht, was gelernt, Optionen mit Empfehlung). Mehr Budget oder weitere Ansätze gibt nur der User.
1. Test ausführen, Rohergebnis sichern.
2. Fehler klassifizieren: Eingabe · Logik · Werkzeug/Umgebung · Anforderung falsch verstanden · Geschmack.
3. Ursache benennen (eine Ebene tiefer als das Symptom).
4. Nur die verursachende Komponente ändern.
5. Erneut testen, gegen vorher und gegen den Mindestfortschritt vergleichen, Zähler aktualisieren.

Vor einem neuen Versuch den bekannten Logstand nutzen und nur neue Einträge lesen.

## Log
In `TEST_RESULTS.md`, sobald Projektgedächtnis besteht; sonst im Chat.
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
