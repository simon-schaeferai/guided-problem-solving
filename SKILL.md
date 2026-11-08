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

**Leitmetrik: Zeit bis zum ersten belastbar geprüften Ergebnis.** Jeder Planungsschritt muss diese Zeit verkürzen oder ein echtes Risiko senken, sonst entfällt er. Planung ist Werkzeug, nie Produkt.

## 1 · Zwei getrennte Einstufungen

**a) Arbeitsumfang (S/M/L)** steuert Planung, Fragen und Ablage. Er sagt nichts darüber, ob eine Aktion freigegeben ist.

| Klasse | Erkennungsmerkmale | Ablauf |
|---|---|---|
| **S · klar** | Ziel und Erfolg eindeutig, ein Lösungsweg naheliegend, wenige Schritte | Stiller Kurzcheck auf Freigabepflicht (1b), dann direkt lösen, prüfen, Ergebnis mit Beleg. Keine Discovery-Fragen, kein Projektgedächtnis; die angeforderte Datei selbst wird bearbeitet. |
| **M · mittel** | Ziel klar, Weg offen oder mehrere Teile; oder ein Input fehlt, der das Ergebnis ändert | Kontext prüfen, höchstens **eine** reguläre Discovery-Runde, kleinster prüfbarer Schritt, iterieren. Einmaliger Lauf: Test- und Entscheidungsbefunde im Chat. |
| **L · komplex** | Ziel unscharf, mehrere Sessions oder Beteiligte, viele Abhängigkeiten, hoher Einsatz bei subjektiver Qualität | Volle Schleife (Abschnitt 3), höchstens **zwei** reguläre Discovery-Runden, Machbarkeitstest vor dem Bau, Projektgedächtnis (Abschnitt 8). |

Die Klasse darf sich ändern: bei Überraschungen hochstufen, bei unerwarteter Einfachheit herunterstufen und das kurz sagen.

**b) Risiko pro Aktion** wird vor **jeder** Aktion geprüft, unabhängig von der Klasse. Eine Aktion braucht eine ausdrückliche Freigabe des Users, wenn sie eines davon tut:
Daten löschen oder fremde Daten überschreiben · Kosten auslösen (API-Credits, Generierung, Abos, bezahlte Tests) · veröffentlichen oder senden · Rechte, Rollen, Freigaben, Sicherheits- oder Zugangseinstellungen ändern · Zugangsdaten verwenden oder ablegen · in fremde oder produktive Systeme schreiben · etwas Irreversibles tun · oder Projektregeln verlangen eine Freigabe.

- Aufwand zählt nicht: Eine Rechteänderung mit einem Befehl braucht dieselbe Freigabe wie eine aufwendige.
- **Schweigen, Defaults, „egal“, abgelaufene Fragerunden und Umkehrbarkeit ersetzen nie eine erforderliche Freigabe.** Defaults gelten nur für Entscheidungen ohne Freigabepflicht.
- Eine Ankündigung ist keine Freigabe. Bezahlte Experimente: Zweck, Obergrenze mit Einheit und Abbruchschwelle nennen und auf ein ausdrückliches Ja warten.
- Fehlt eine Freigabe, nur unabhängige, bereits erlaubte Vorbereitung fortsetzen (lesen, lokal entwerfen, kostenlos testen). Der abhängige Schritt wird als **wartet auf Freigabe** gemeldet.
- Eine Freigabe gilt nur für den genannten Umfang (was, wo, wie viel, einmalig oder wiederholt), nicht darüber hinaus und nicht für spätere ähnliche Aktionen.
- **Frühere Freigaben (Fortsetzung, Wiederaufnahme):** Sie gelten nur, wenn sie nachweislich zur konkreten anstehenden Aktion passen (gleiche Aktion, gleiches Ziel, Umfang nicht überschritten) und noch gültig sind (nicht widerrufen, Gültigkeitsbedingung erfüllt, Sachlage unverändert).

**c) Einmalige Aktionen gegen Doppelausführung sichern.** Gilt nur für freigabepflichtige Aktionen, die bei zweifacher Ausführung schaden (bezahlen, senden, veröffentlichen, buchen, anlegen) und deren Ergebnis sich nicht sicher am Zielsystem ablesen lässt. Alles andere braucht diesen Schritt nicht.
- Status der Freigabe: **frei → reserviert → begonnen → ausgeführt** (mit Beleg). Daneben **abgebrochen** (vor dem Auslösen gestoppt, ohne Wirkung, damit wieder frei) und **wartet auf Klärung**. Vor dem Start „reserviert“, direkt vor dem Auslösen „begonnen“, danach das Ergebnis.
- Ort: Freigabe-Tabelle in `PROGRESS.md`. Gibt es noch kein Projektgedächtnis, für diese eine Aktion ein minimales `PROGRESS.md` (Kopf und Freigabe-Tabelle) anlegen; eine Chat-Notiz überlebt keine Unterbrechung.
- Steht nach einer Unterbrechung eine Freigabe auf „reserviert“ oder „begonnen“: zuerst den tatsächlichen Zustand lesend prüfen (Zielsystem, Logs, Abrechnung, Ausgabedateien). Belegt nicht ausgeführt: zurück auf „frei“, einmal ausführen. Belegt ausgeführt: „ausgeführt“. Weiter ungeklärt: **wartet auf Klärung**; nicht wiederholen, bis der User den Zustand klärt oder eine neue Freigabe erteilt.
- Ausgelöst werden darf nur eine Freigabe im Status „frei“. „Ausgeführt“ ist verbraucht.

## 2 · Grundregeln

1. **Erst schauen, dann fragen**, aber nur so weit, wie es den nächsten prüfbaren Schritt beschleunigt. Was Dateien, Projektregeln, Memory, Skills oder Tools beantworten, wird nicht gefragt.
2. **Wiederverwenden vor Neubau.** Vorhandenes zuerst prüfen, begrenzt auf plausible Kandidaten (Projekt, installierte Skills/Tools, naheliegende Bibliotheken oder Produkte). Neubau nur, wenn Vorhandenes ein Muss-Kriterium nachweislich nicht erfüllt.
3. **Projektregeln haben Vorrang** (Freigabe-Gates, Pflicht-Skills, Branding, Datenschutz). Dieser Skill ist der Rahmen; Fach-Skills sind seine Werkzeuge.
4. **Entscheidungsrecht:** Umkehrbares und Technisches ohne Freigabepflicht entscheidet der Agent und nennt es in einem Halbsatz. Der User entscheidet Ziel, Geschmack, Budget, Priorität und alles mit Freigabepflicht (1b).
5. **Tun statt beschreiben.** Wo ein Tool die Arbeit kann, wird es benutzt. Anleitungen nur für Schritte, die der Agent nicht darf oder kann.
6. **Beobachtung ≠ Hypothese.** Gemessenes, Gelesenes, Getestetes kennzeichnen; alles andere ist Annahme mit Prüfweg.
7. **Delegation nur, wenn sie beschleunigt** (breite Suche, große Lektüre). Delegierte Befunde behalten ihre Fundstelle (Datei:Zeile, URL, Befehl).
8. **Ehrlich über Grenzen:** Nicht Machbares konkret begründen und die beste praktikable Alternative nennen.

## 3 · Kernschleife (Bausteine, keine Pflichtstationen)

Jeden Baustein nur ausführen, wenn er für diese Klasse und dieses Problem etwas bringt. Mehrere Bausteine dürfen in einer Antwort zusammenfallen.

1. **Problem verstehen:** Was ist das eigentliche Ziel? Was ändert sich für den User, wenn es gelöst ist?
2. **Ziel und Erfolgskriterien:** Ein Satz Endergebnis, Muss vs. Kann, je Muss ein prüfbares Kriterium (Messmethode und Schwelle). Bei Zielkonflikten den Vorrang des Users übernehmen; ohne Vorgabe einen begründeten Default setzen und als Annahme kennzeichnen.
3. **Kontext und Lücken:** Inventar des Vorhandenen, soweit es den nächsten Schritt beeinflusst. Lücken nur auflisten, wenn sie eine Entscheidung ändern.
4. **Strategie wählen** (Abschnitt 4). Alternativen nur bewerten, wenn mehr als eine realistisch ist.
5. **Risiken, Annahmen, Budget:** den **einen** kritischsten Unsicherheitsfaktor benennen. Review nach `references/review.md` (S: entfällt bis auf 1b · M: nur die Punkte, die das konkrete Risiko betreffen, Abhängigkeiten eingeschlossen, wenn sie entscheiden · L: vollständig). Bei M und L dem User danach seine **blinden Flecken** zeigen: höchstens 3 Punkte, die er vermutlich nicht bedacht hat, je ein Satz mit Folge und Vorschlag. Nur nennen, nicht fragen, außer einer ändert das Ziel. Vor dem ersten Versuch Budget und Abbruchgrenzen festlegen (Abschnitt 6).
6. **Umsetzen:** mit dem kleinsten Schritt beginnen, der den kritischsten Faktor prüft (Machbarkeitstest mit vorher festgelegtem Bestanden-Kriterium). Fällt er durch, Strategie neu wählen statt weiterbauen; der Versuch zählt auf Budget und Zähler. Ein bestandener Machbarkeitstest belegt nur das Kriterium, das er geprüft hat.
7. **Testen, analysieren, verbessern:** Abschnitt 6.
8. **Validieren:** gegen alle Muss-Kriterien aus Baustein 2, je Kriterium mit Beleg (Abschnitt 7).
9. **Erkenntnisse sichern:** nur, was eine spätere Session oder ein späterer Lauf braucht (Abschnitt 8).

**Übergang Planung → Umsetzung**, sobald gilt: Ziel ist in einem Satz klar · Pflicht-Inputs liegen vor (oder es gibt für sie einen begründeten Default) · der nächste Schritt hat ein Bestanden-Kriterium · und er ist freigegeben oder braucht keine Freigabe. Nicht blockierende Fragen halten nicht auf. Das Ziel nur bestätigen lassen, wenn es mehrdeutig ist **und** ein Fehlgriff teuer wäre.

## 4 · Strategie-Wahl

| Situation (Kriterium) | Strategie |
|---|---|
| Lösung bekannt, Risiko gering | **Direkt lösen** |
| Fehlendes Faktenwissen, Stand der Technik, externe Optionen unklar | **Recherche** (zeitlich begrenzt, Quellen nennen, mit Kandidat enden) |
| Etwas Bestehendes funktioniert nicht | **Debugging**: reproduzieren, eingrenzen, Ursache, Fix, Regressionstest |
| Gute Beispiele oder Altsysteme enthalten implizites Wissen, das sonst nur teuer zu erfragen ist | **Reverse Engineering** (`references/reverse-engineering.md`) |
| Machbarkeit oder Wirkung unbekannt, schnell und günstig testbar | **Experiment** mit Hypothese und Abbruchschwelle |
| Anforderungen unscharf oder Geschmack entscheidet | **Prototyp/Varianten** zeigen und Feedback holen statt Fragen |
| Lösung läuft, Qualität oder Leistung soll messbar steigen | **Systematische Optimierung**: Basiswert messen, eine Variable je Durchgang |
| Werkzeug, Skill oder Produkt deckt das Muss ab | **Vorhandenes nutzen**, ggf. dünn ergänzen |
| Nichts Vorhandenes erfüllt ein Muss-Kriterium | **Neue Komponente**, kleinstmöglich, hinter klarer Schnittstelle |

Strategien kombinieren ist normal. Reverse Engineering ist nie Voraussetzung für Tests oder Failure Learning.

## 5 · Fragen

Vier Arten, jede mit eigenem Endzustand:

| Art | Regel | Ohne Antwort |
|---|---|---|
| **Reguläre Discovery** | S: keine · M: höchstens eine Runde · L: höchstens zwei Runden vor dem ersten prüfbaren Artefakt. Je Runde 1 bis 3 entscheidungsrelevante Fragen, empfohlene Option zuerst mit einem Satz Trade-off. | Empfehlung gilt, als korrigierbare Annahme genannt. |
| **Interview zu implizitem Wissen** | Nur bei M und L, wenn Wissen, das der User nie aufschreiben würde, über die Qualität entscheidet (Geschmack, Fachwissen, eigener Stil, ungeschriebene Ausnahmen). Einmal vor dem ersten Artefakt, 3 bis 5 offene Fragen aus `references/discovery.md`. Zählt nicht gegen die Discovery-Runden. | Mit Beispielen oder Varianten weiter; die Reaktion darauf ersetzt das Interview. |
| **Zwingender Blocker** (Input ohne sinnvollen Default) | Je Blocker **einmal** gezielt fragen, auch außerhalb der Discovery-Runden. Dieselbe Frage erst wieder, wenn sich der Sachstand ändert. | Abhängiger Schritt: **blockiert: <Input>**. Nur unabhängige Arbeit erledigen. Nichts erfinden. |
| **Freigabe** | Nach 1b, pro Aktion. | **wartet auf Freigabe**; nie als erteilt werten. |

- Fragen mit gutem Default nicht stellen. Bei subjektiver Qualität lieber 2 bis 3 konkrete Varianten zeigen als abstrakt fragen.
- Beantwortetes nie erneut fragen. Formulierung und Priorisierung: `references/discovery.md`.

## 6 · Fehler-Lernschleife, Budget und Abbruch

Nur wenn eine **Feedbackquelle** existiert. Vor dem Bau festlegen, welche:

| Feedbackquelle | Wann | Prüfung |
|---|---|---|
| Automatischer Test, Skript, Build | Code, Daten, Automatisierung | Test läuft rot, dann grün |
| Messung gegen Schwelle | Leistung, Kosten, Qualitätsmetrik | Zahl vorher/nachher |
| Abgleich mit Referenz | Nachbau, Formatvorgaben | Checkliste/Diff gegen Vorbild |
| Urteil des Users oder Stakeholders | Geschmack, Business-Entscheidung | Variante zeigen, Urteil einholen |
| keine verfügbar | z. B. Wirkung erst später messbar | Ergebnis als **unverifiziert** kennzeichnen und nennen, wann/wie es prüfbar wird |

**Vor dem ersten Versuch festlegen:** Gesamtbudget (Versuche, Zeit, Kosten), Mindestfortschritt je Versuch und Abbruchgrenzen.

**Begriffe:**
- **Versuch:** eine Änderung plus eine Prüfung gegen die Feedbackquelle. Dieselbe Prüfung ohne Änderung erneut laufen zu lassen, ist kein neuer Versuch.
- **Ansatz:** ein bestimmter Lösungsweg, erkennbar am Mechanismus (Werkzeug, Methode, Architektur). Andere Parameter oder ein neuer Name im selben Mechanismus sind derselbe Ansatz.
- **Ansatz gescheitert:** zwei Versuche in Folge ohne Mindestfortschritt **oder** ein Versuch, der die Voraussetzung des Ansatzes nachweislich widerlegt (z. B. die Schnittstelle kann das Nötige nicht). Dann ist ein Ansatzwechsel Pflicht.

**Drei Zähler** für das ganze Vorhaben:

| Zähler | Ändert sich | Grenze |
|---|---|---|
| Budget verbraucht (Versuche, Zeit, Kosten) | nach jedem Versuch | Gesamtbudget |
| Gescheiterte Ansätze | +1, wenn ein Ansatz scheitert | 3 |
| Serie ohne Mindestfortschritt | +1 ohne Fortschritt; 0 bei Fortschritt oder nach Ansatzwechsel | 2, dann gilt der Ansatz als gescheitert |

Versuchsnummern laufen über Ansätze hinweg weiter. Kein Session-, Strategie- oder Namenswechsel setzt einen Zähler zurück, und kein Zähler wird ohne Beleg auf 0 gesetzt; ein nicht belegbarer Stand heißt **unbekannt** (Abschnitt 8, Hochstufen).

**Vor jedem weiteren Versuch** die Zähler prüfen. Endgültig stoppen, wenn 3 Ansätze gescheitert sind oder das Budget erreicht ist: keinen Versuch starten, sondern berichten (was versucht, was gelernt, Optionen mit Empfehlung). Mehr Budget oder weitere Ansätze gibt nur der User. Identische Versuche sind verboten. Bei Projektgedächtnis stehen die Zähler in `PROGRESS.md` und werden nach jedem Versuch aktualisiert.

Schleife und Logformat: `references/failure-learning.md`.

## 7 · Validieren und melden

- **„Fertig“ nur, wenn jedes Muss-Kriterium einen Beleg hat** (Testausgabe, Messwert, Screenshot, Diff, Urteil des Users). Fehlt ein Beleg, ist der Stand „teilweise fertig“ mit Nennung des offenen Kriteriums.
- Bericht trennt **verifiziert** (wie geprüft) · **unverifiziert** (warum, wie prüfbar) · **offen** · **wartet auf Freigabe** · **blockiert**.
- Fortschritt bei längeren Läufen an Meilensteinen und Blockern melden, nicht nach jedem Kleinschritt.
- Antwort endet mit: erledigt · offen · wer ist dran (bei S genügt ein Satz).

## 8 · Ergebnisse und Projektgedächtnis

**Ergebnisdateien** sind das, was die Aufgabe liefern soll (Code, Dokument, Konfiguration). Sie liegen dort, wo der User oder das Projekt sie braucht. **Projektgedächtnis** ist optional und dient nur der Fortsetzung. Beides nie vermischen.

**Wann:** nur, wenn das Vorhaben über die aktuelle Session hinausgeht, mehrere Beteiligte hat, Klasse L vorliegt oder eine einmalige Aktion nach 1c ansteht. Sonst bleiben Befunde, Testlog und Entscheidungen im Chat.

**Hochstufen auf L oder Übergang in eine weitere Session:** Gedächtnis sofort anlegen und aus dem Chat übernehmen, was die Fortsetzung braucht: Ergebnisse, Versuche mit Ergebnis, gescheiterte Ansätze mit Grund, Entscheidungen und Annahmen, Freigaben mit Status. Zähler nur mit Beleg übernehmen, sonst als **unbekannt** eintragen, nie als 0. Ist ein Zähler oder ein Freigabestatus unbekannt, vor dem nächsten kostenpflichtigen oder freigabepflichtigen Versuch den Stand rekonstruieren (Chatverlauf, Logs, Zielsystem). Gelingt das nicht, das Budget vom User neu bestätigen lassen; kostenlose, harmlose Versuche dürfen weiterlaufen.

**Projektkennung:** `<YYYY-MM-DD>-<slug>-<4 Zeichen>` (z. B. `2026-11-08-rechnungsimport-k3f9`, Suffix zufällig aus a–z/0–9). Einmal vergeben, nie geändert; steht im Ordnernamen und im Kopf von `PROGRESS.md`.

**Ort:**
- Bevorzugt `~/Desktop/<Projektkennung>/`, damit der User den Stand sofort findet und hineinschauen kann.
- **Ausweichpfad**, wenn der Desktop fehlt, nicht beschreibbar ist oder die Umgebung keinen hat (Server, Container, Cloud-Session): `<arbeitsordner>/.guided/<Projektkennung>/`.

**Vor dem ersten Schreiben:**
1. Ort beschreibbar und nach Projektregeln erlaubt? Sonst den anderen Ort nehmen oder nach einem Pfad fragen.
2. Kollision: Existiert der Ordner schon, ein neues Suffix ziehen.
3. Liegt der Ort in einem Git-Repo: mit `git check-ignore` prüfen. Ist er nicht ignoriert und erlauben die Projektregeln Änderungen an Git-Metadaten, den Pfad in `.git/info/exclude` eintragen (lokal, nicht versioniert) und das nennen. Sonst den Desktop nehmen oder nach einem Ort außerhalb des Repos fragen. Nie versehentlich einchecken.
4. **Sensible Rohdaten** (Kundendaten, Exporte, Zugangsdaten, private Medien) bleiben am freigegebenen Projektort; das Gedächtnis enthält nur Pfade, Zusammenfassungen und Kennzahlen.

**Dateien** (Vorlagen in `templates/`):
- **Kern:** `PROGRESS.md` ist die **maßgebliche Quelle** für Projektkennung, Vorhaben (ein Satz), Arbeitsordner, Gedächtnisort, den **unmittelbar nächsten Schritt mit Freigabestatus**, die drei Zähler aus Abschnitt 6 und die Freigaben (Umfang, Art, Gültigkeit, Status nach 1c, Beleg). `NEXT_STEPS.md` enthält nur nachgelagerte Schritte und offene Fragen; bei Widerspruch gilt `PROGRESS.md`.
- **Bei Bedarf:** `PROJECT_BRIEF.md` (Ziel, Kriterien), `DECISIONS.md` (Entscheidungen, Annahmen), `ARCHITECTURE.md` (mehrere Bausteine), `IMPLEMENTATION_PLAN.md` (mehr als ca. 5 Schritte), `TEST_RESULTS.md` (sobald Projektgedächtnis besteht und iterativ getestet wird; Details je Versuch, die Zähler bleiben in `PROGRESS.md`).

**Fortsetzung:**
1. Kandidaten suchen: `~/Desktop` und, falls bekannt, `<arbeitsordner>/.guided/` nach Stichwort oder Projektkennung.
2. **Jeden** Treffer prüfen, auch einen einzelnen: Passen Vorhaben und Arbeitsordner im `PROGRESS.md`-Kopf zum aktuellen Auftrag und existiert der Arbeitsordner? Nicht passende Treffer verwerfen.
3. Bleiben mehrere passende Treffer, die Kandidaten mit Projektkennung, Datum und Vorhaben zur Auswahl stellen. Bleibt keiner und ist der Arbeitsordner unbekannt, gezielt nach dem Pfad fragen.
4. `PROGRESS.md` und `NEXT_STEPS.md` lesen, weitere Dateien nur bei Bedarf. Zähler übernehmen, Freigaben nach 1b prüfen, offene Status nach 1c klären. Stand in einem Satz melden und weitermachen.

**Übergabetest:** Könnte eine neue Session mit `PROGRESS.md` und `NEXT_STEPS.md` in einer Minute weitermachen? Wenn nein, nachschärfen. `PROGRESS.md` unter ca. 60 Zeilen halten, verlinken statt kopieren.

## 9 · Effizienz

- Bekannten Dateistand nutzen; erneut lesen, wenn sich die Datei verändert haben könnte (andere Session, Tool, User) oder bevor auf ihrer Grundlage eine freigabepflichtige Aktion folgt. Bei Logs nur neue Einträge lesen (z. B. ab der letzten bekannten Versuchsnummer).
- Die Absicherungen kosten harmlose Aufgaben nichts: S bleibt beim stillen Kurzcheck aus 1b, 1c greift nur bei schädlicher Doppelausführung.
- Tabellen statt Prosa. Keine Dokumente, die niemand liest.
