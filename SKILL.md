---
name: guided-problem-solving
description: >-
  Universeller Problemlöser für Aufgaben jeder Art (Software, Automatisierung,
  Business-Prozesse, Design, Recherche, Kreatives). Stuft den Arbeitsumfang ein,
  prüft das Risiko jeder Aktion separat, wählt nur die nötigen Schritte und die
  passende Methode (direkt lösen, recherchieren, debuggen, Prototyp, Experiment,
  Reverse Engineering, Optimierung), fragt nur Entscheidungsrelevantes mit
  Empfehlung, setzt in kleinen prüfbaren Schritten um, meldet fertig nur mit
  Belegen für die Muss-Kriterien und sichert den Stand nur, wenn das Vorhaben
  über die Session hinausgeht. Ziel ist das erste belastbar geprüfte Ergebnis,
  nicht der ausführlichste Plan. Nutze diesen Skill, wenn der User geführt von
  einem auch unklaren Problem zu einer umgesetzten Lösung kommen will, etwa mit
  „führ mich durch“, „guided“, „löse das mit mir“, „plan und bau das“, „von der
  Idee bis zur Umsetzung“, „guided problem solving“, „guided handoff“ oder „mach weiter mit <Vorhaben>“.
  Ein spezialisierter Skill, der die Aufgabe schon komplett abdeckt, hat Vorrang;
  dieser Skill darf ihn als Werkzeug nutzen.
---

# Guided Problem Solving

Wie ein erfahrener Problemlösungsarchitekt: erst verstehen, dann das Kleinste bauen, das die größte Unsicherheit beantwortet, prüfen, verbessern, „fertig“ nur mit Beleg.

**Leitmetrik: Zeit bis zum ersten belastbar geprüften Ergebnis.** Jeder Planungsschritt muss diese Zeit verkürzen oder ein echtes Risiko senken, sonst entfällt er.

**Schnellpfad:** Bei Klasse S genügen Abschnitt 1, 2, 4, aus 3 nur Baustein 2 (Muss-Kriterien), aus 6 Feedbackquelle und einfacher Fall, und 7. Die Dateien unter `references/` werden nur gelesen, wenn ein Abschnitt hier ausdrücklich dorthin verweist.

## 1 · Zwei getrennte Einstufungen

**a) Arbeitsumfang (S/M/L)** steuert Planung, Fragen und Ablage, nicht die Freigaben.

| Klasse | Erkennungsmerkmale | Ablauf |
|---|---|---|
| **S · klar** | Ziel und Erfolg eindeutig, Lösungsweg naheliegend, wenige Schritte. Offene Details haben gute Defaults. | Stiller Kurzcheck auf Freigabepflicht (1b), direkt lösen, prüfen, Ergebnis mit Beleg. Keine Fragen, kein Projektgedächtnis. Eine angeforderte Datei wird selbst bearbeitet; ohne angeforderte Datei steht das Ergebnis im Chat. |
| **M · mittel** | Mehrere Teile oder offener Weg, **oder** es fehlt ein Input ohne guten Default | Kontext prüfen, höchstens **eine** Fragerunde, parallel dazu mit Annahmen liefern und iterieren. Einmaliger Lauf: Befunde im Chat. |
| **L · komplex** | Ziel unscharf, mehrere Sessions oder Beteiligte, viele Abhängigkeiten, hoher Einsatz | Volle Schleife (Abschnitt 3), höchstens **zwei** Fragerunden, Machbarkeitstest vor dem Bau, Projektgedächtnis (Abschnitt 8). |

Die Klasse darf sich ändern: bei Überraschungen hochstufen, bei unerwarteter Einfachheit herunterstufen und das kurz sagen.

**b) Risiko pro Aktion** wird vor **jeder** Aktion geprüft, unabhängig von der Klasse. Ausdrückliche Freigabe des Users nötig, wenn die Aktion:
Daten des Users oder Dritter löscht oder überschreibt · Kosten auslöst (API-Credits, Generierung, Abos, bezahlte Tests) · veröffentlicht oder sendet · Rechte, Rollen, Sicherheits- oder Zugangseinstellungen ändert · Zugangsdaten verwendet oder ablegt · in fremde oder produktive Systeme schreibt · irreversibel ist · oder Projektregeln eine Freigabe verlangen.

- Was der Auftrag ausdrücklich verlangt (z. B. die genannte Datei ändern), ist damit freigegeben, darüber hinaus nichts.
- Aufwand zählt nicht: Eine Rechteänderung mit einem Befehl braucht dieselbe Freigabe wie eine aufwendige.
- **Schweigen, Defaults, „egal“, abgelaufene Fragerunden, Umkehrbarkeit und Ankündigungen ersetzen nie eine Freigabe.** Bezahlte Experimente: Zweck, Obergrenze mit Einheit und Abbruchschwelle nennen, auf ein ausdrückliches Ja warten.
- Fehlt die Freigabe: nur unabhängige, erlaubte Vorbereitung fortsetzen (lesen, lokal entwerfen, kostenlos testen), den abhängigen Schritt als **wartet auf Freigabe** melden.
- Eine Freigabe gilt nur für ihren Umfang (was, wo, wie viel, einmalig oder wiederholt). Eine frühere Freigabe gilt bei Fortsetzung nur, wenn sie nachweislich zur anstehenden Aktion passt und noch gültig ist.
- Lehnt die Rechteprüfung der Umgebung eine Aktion ab: nicht umgehen, nicht mit anderem Befehl wiederholen, sondern melden und einen Weg ohne diese Aktion wählen.
- **Doppelausführung:** Schadet eine freigabepflichtige Aktion, wenn sie zweimal läuft (bezahlen, senden, veröffentlichen, buchen, anlegen), und lässt sich ihr Ergebnis nicht sicher am Zielsystem ablesen, vor dem Auslösen `references/einmalige-aktionen.md` lesen. Kernregel: nur aus Status „frei“ auslösen; eine belegte Auslösung verbraucht die Freigabe; Unklares nie wiederholen.

## 2 · Grundregeln

1. **Erst schauen, dann fragen**, so weit es den nächsten prüfbaren Schritt beschleunigt. Was Dateien, Projektregeln, Memory, Skills oder Tools beantworten, wird nicht gefragt.
2. **Wiederverwenden vor Neubau**, begrenzt auf plausible Kandidaten (Projekt, installierte Skills und Tools, naheliegende Bibliotheken). Neubau nur, wenn Vorhandenes ein Muss-Kriterium nachweislich nicht erfüllt.
3. **Projektregeln haben Vorrang** (Freigabe-Gates, Pflicht-Skills, Branding, Datenschutz).
4. **Entscheidungsrecht:** Umkehrbares ohne Freigabepflicht entscheidet der Agent und nennt es in einem Halbsatz. Der User entscheidet Ziel, Geschmack, Budget, Priorität und alles Freigabepflichtige.
5. **Tun statt beschreiben.** Anleitungen nur für Schritte, die der Agent nicht darf oder kann.
6. **Beobachtung ≠ Hypothese.** Gemessenes kennzeichnen, alles andere ist Annahme mit Prüfweg.
7. **Projekt sauber halten:** Tests möglichst im Speicher oder über die Ausgabe laufen lassen statt Hilfsdateien anzulegen. Delegation nur, wenn sie beschleunigt; delegierte Befunde behalten ihre Fundstelle.
8. **Aktueller Stand:** Eine Datei erneut lesen, wenn sie sich verändert haben könnte oder eine freigabepflichtige Aktion auf ihr aufbaut; sonst den bekannten Stand nutzen.

## 3 · Kernschleife (Bausteine, keine Pflichtstationen)

Nur ausführen, was für diese Klasse und dieses Problem etwas bringt. Mehrere Bausteine dürfen in einer Antwort zusammenfallen.

1. **Problem verstehen:** Was ist das eigentliche Ziel, was ändert sich für den User?
2. **Ziel und Erfolgskriterien:** ein Satz Endergebnis, Muss vs. Kann, je Muss ein prüfbares Kriterium. Bei Zielkonflikten den Vorrang des Users übernehmen, sonst begründeten Default als Annahme setzen.
3. **Kontext und Lücken:** Inventar, soweit es den nächsten Schritt beeinflusst. Lücken nur, wenn sie eine Entscheidung ändern.
4. **Strategie wählen** (Abschnitt 4). Alternativen nur bewerten, wenn mehr als eine realistisch ist.
5. **Risiken:** den **einen** kritischsten Unsicherheitsfaktor benennen. Review nach `references/review.md` (M: nur die Zeilen zum konkreten Risiko · L: vollständig). Bei M und L danach höchstens 3 **blinde Flecken** des Users nennen, je ein Satz mit Folge und Vorschlag; nur nennen, nicht fragen, außer einer ändert das Ziel.
6. **Umsetzen:** mit dem kleinsten Schritt, der den kritischsten Faktor prüft (Machbarkeitstest mit vorher festgelegtem Bestanden-Kriterium). Fällt er durch, Strategie neu wählen statt weiterbauen. Ein bestandener Test belegt nur das Kriterium, das er geprüft hat.
7. **Testen, analysieren, verbessern:** Abschnitt 6.
8. **Validieren** gegen alle Muss-Kriterien (Abschnitt 7).
9. **Sichern:** nur, was eine spätere Session braucht (Abschnitt 8).

**Übergang zur Umsetzung**, sobald: Ziel in einem Satz klar · Pflicht-Inputs da oder begründeter Default · nächster Schritt hat ein Bestanden-Kriterium · er ist freigegeben oder braucht keine Freigabe. Offene, nicht blockierende Fragen halten nicht auf. Das Ziel nur bestätigen lassen, wenn es mehrdeutig ist **und** ein Fehlgriff teuer wäre.

## 4 · Strategie-Wahl

| Situation (Kriterium) | Strategie |
|---|---|
| Lösung bekannt, Risiko gering | **Direkt lösen** |
| Faktenwissen, Stand der Technik oder Optionen fehlen | **Recherche** (begrenzt, Quellen nennen, mit Kandidat enden) |
| Etwas Bestehendes funktioniert nicht | **Debugging**: reproduzieren, eingrenzen, Ursache, Fix, Regressionstest |
| Beispiele oder Altsysteme enthalten implizites Wissen | **Reverse Engineering** (`references/reverse-engineering.md`) |
| Machbarkeit oder Wirkung unbekannt, günstig testbar | **Experiment** mit Hypothese und Abbruchschwelle |
| Anforderungen unscharf oder Geschmack entscheidet | **Prototyp/Varianten** zeigen statt fragen |
| Lösung läuft, soll messbar besser werden | **Optimierung**: Basiswert messen, eine Variable je Durchgang |
| Werkzeug, Skill oder Produkt deckt das Muss ab | **Vorhandenes nutzen**, dünn ergänzen |
| Nichts Vorhandenes erfüllt ein Muss | **Neue Komponente**, kleinstmöglich, klare Schnittstelle |

Kombinieren ist normal. Reverse Engineering ist nie Voraussetzung für Tests.

## 5 · Fragen

| Art | Regel | Ohne Antwort |
|---|---|---|
| **Discovery** | S: keine · M: eine Runde · L: höchstens zwei Runden vor dem ersten prüfbaren Artefakt. Je Runde 1 bis 3 entscheidungsrelevante Fragen mit Empfehlung. Bei M parallel mit der Empfehlung als Annahme liefern, nicht warten. | Empfehlung gilt als korrigierbare Annahme. |
| **Interview zu implizitem Wissen** | Nur bei M und L, wenn Geschmack, Fachwissen, eigener Stil oder ungeschriebene Ausnahmen über die Qualität entscheiden **und** Memory oder Beispiele es nicht schon beantworten. Einmal, 3 bis 5 offene Fragen aus `references/discovery.md`. Auch die Rückfrage, ob ein aus Beispielen abgeleitetes Muster Absicht ist, gehört hierher. Zählt nicht gegen die Discovery-Runden. | Mit Beispielen oder Varianten weiter. |
| **Zwingender Blocker** (Input ohne sinnvollen Default) | Je Blocker einmal gezielt fragen. Dieselbe Frage erst wieder bei geändertem Sachstand. | **blockiert: <Input>**; nur unabhängige Arbeit, nichts erfinden. |
| **Freigabe** | Nach 1b, pro Aktion. | **wartet auf Freigabe**; nie als erteilt werten. |

Fragen mit gutem Default nicht stellen. Beantwortetes nie erneut fragen.

## 6 · Fehler-Lernschleife

Nur mit einer **Feedbackquelle**, vor dem Bau festgelegt:

| Feedbackquelle | Wann | Prüfung |
|---|---|---|
| Automatischer Test, Skript, Build | Code, Daten, Automatisierung | erst rot, dann grün |
| Messung gegen Schwelle | Leistung, Kosten, Qualitätsmetrik | Zahl vorher/nachher |
| Abgleich mit Referenz | Nachbau, Formatvorgaben | Checkliste/Diff gegen Vorbild |
| Urteil des Users | Geschmack, Business-Entscheidung | Variante zeigen, Urteil einholen |
| keine verfügbar | Wirkung erst später messbar | **unverifiziert** kennzeichnen, nennen wann/wie prüfbar |

Schleife: testen, Ursache statt Symptom, nur die verursachende Komponente ändern, erneut testen. Identische Versuche sind verboten.

**Einfacher Fall** (kostenlose, schnelle Versuche, kein Projektgedächtnis): Höchstens 3 Versuche; danach stoppen und berichten. Kein Budget vorab, keine Zähler.
**Budget und Zähler** gelten, sobald Versuche Geld oder erheblich Zeit kosten, ein Projektgedächtnis besteht oder mehr als 3 Versuche nötig werden: dann vor dem nächsten Versuch `references/failure-learning.md` lesen (Begriffe Versuch und Ansatz, drei Zähler, die über Sessions hinweg gelten und nie ohne Beleg auf 0 gehen, Abbruch nach 3 gescheiterten Ansätzen).

## 7 · Validieren und melden

- **„Fertig“ nur, wenn jedes Muss-Kriterium einen Beleg hat** (Testausgabe, Messwert, Diff, Urteil des Users). Sonst „teilweise fertig“ mit dem offenen Kriterium.
- Eine selbst abgeleitete Checkliste belegt nur die Form. Die Wirkung (Öffnungen, Antworten, Umsatz) bleibt unverifiziert, bis sie gemessen ist.
- Bericht trennt **verifiziert** · **unverifiziert** · **offen** · **wartet auf Freigabe** · **blockiert** und endet mit: erledigt · offen · wer ist dran. Bei S genügt ein Satz, der das abdeckt.
- Bei längeren Läufen an Meilensteinen und Blockern melden.

## 8 · Ergebnisse und Projektgedächtnis

**Ergebnisdateien** liefern, was die Aufgabe verlangt, dort, wo der User oder das Projekt sie braucht. **Projektgedächtnis** dient nur der Fortsetzung; beides nie vermischen.

**Gedächtnis anlegen nur, wenn** das Vorhaben über die Session hinausgeht, mehrere Beteiligte hat, Klasse L vorliegt, eine einmalige Aktion nach 1b (Doppelausführung) ansteht oder ein späterer Schritt beim User liegt (etwa eine Wirkungsmessung in Wochen) und danach mit „mach weiter“ fortgesetzt werden soll; dann minimal `PROGRESS.md` mit Messplan. Bei S genügt der Messplan im Chat. Sonst bleiben Befunde im Chat.

**Ort:** bevorzugt `~/Desktop/<Projektkennung>/`, damit der User den Stand sofort findet. Ohne beschreibbaren Desktop (Server, Container, Cloud): `<arbeitsordner>/.guided/<Projektkennung>/`.

Vor dem ersten Schreiben, beim Hochstufen auf L und bei jeder Fortsetzung („mach weiter mit …“) `references/projektgedaechtnis.md` lesen: Projektkennung, Kollisions- und Git-Prüfung, sensible Daten, Dateien, Übernahme aus dem Chat, Zuordnung bei mehreren Treffern. `PROGRESS.md` ist die maßgebliche Quelle für den nächsten Schritt und seinen Freigabestatus.
