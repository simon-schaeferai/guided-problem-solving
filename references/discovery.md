# Discovery: Fragen finden, priorisieren, stellen

Wie viele Runden erlaubt sind und was ohne Antwort passiert, regelt SKILL.md Abschnitt 5 (reguläre Discovery, zwingender Blocker, Freigabe). Diese Datei regelt nur, **welche** Fragen und **wie**.

## Selbst klären (nie fragen)
Nur so weit, wie es den nächsten prüfbaren Schritt beschleunigt:
- Was liegt im Projekt? (Dateien, Ordner, frühere Pläne, Memory)
- Welche Skills, MCP-Server, CLIs, API-Keys gibt es? (`ls ~/.claude/skills`, Projekt-Skills, `.env`-Variablennamen ohne Werte, `which <tool>`)
- Welche Projektregeln greifen? (CLAUDE.md, rules, Freigabe-Gates)
- Was sagt die Dokumentation eines Tools? (lesen statt raten)

## Fragenkatalog (nur, was nach dem Selbst-Klären offen ist)
| Bereich | Leitfrage |
|---|---|
| Zweck | Wofür genau, und woran merkst du, dass es funktioniert? |
| Nutzer | Wer bedient es, wie oft, mit welchem Vorwissen? |
| Input | Welche Daten/Beispiele gibt es, wo liegen sie, wie viele? |
| Output | Welches Format, wohin, wer nimmt es ab? |
| Qualität | Was ist „gut genug“? Gibt es ein Vorbild oder ein Negativbeispiel? |
| Grenzen | Budget pro Monat/Lauf, Zeitrahmen, No-Gos, Datenschutz |
| Integration | Mit welchen bestehenden Tools muss es zusammenspielen? |
| Kontrolle | Wo will der User eingreifen, was soll vollautomatisch sein? |

## Priorisieren
Score = (Wie stark ändert die Antwort die Architektur?) × (Wie unsicher bin ich?). Die höchsten zuerst, höchstens drei pro Runde. Fragen mit gutem Default nicht stellen, sondern Default nehmen und als „Annahme, korrigierbar“ notieren (im Chat oder, bei Projektgedächtnis, in `DECISIONS.md`).

Ein **zwingender Blocker** ist ein Input, ohne den kein sinnvoller Default möglich ist (z. B. Zugang, Zielsystem, Pflichtdatei). Er wird einzeln und gezielt erfragt, nicht in eine Discovery-Runde gepackt. Freigaben sind keine Discovery-Fragen (SKILL.md Abschnitt 1b).

## Formulierung
- Jede Frage eigenständig verständlich (der User sieht evtl. nur den Dialog).
- Optionen statt offener Frage, empfohlene Option zuerst mit „(Empfohlen)“ und einem Satz Warum.
- Zusammenhängende Fragen bündeln, unabhängige auf spätere Runden verteilen.
- Bei Geschmacksfragen Varianten zeigen statt Fragen stellen.

## Interview: implizites Wissen
Für die Dinge, die der User weiß, aber nie aufschreiben würde. Offene Fragen, keine Optionen; 3 bis 5 auswählen, die zum Vorhaben passen:
- Woran merkst du sofort, dass ein Ergebnis falsch ist?
- Was hast du schon probiert und verworfen, und warum?
- Welche Ausnahme oder Sonderregel kennst du, die nirgends steht?
- Was machst du jedes Mal gleich, ohne darüber nachzudenken?
- Wie sähe ein Ergebnis aus, das formal stimmt, dich aber trotzdem stört?
Antworten als **Absicht des Users** festhalten (bei Projektgedächtnis in `DECISIONS.md`), getrennt von gemessenen Befunden.
