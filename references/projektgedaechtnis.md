# Projektgedächtnis: anlegen, übernehmen, fortsetzen

Wann es angelegt wird und wo es liegt, steht in SKILL.md Abschnitt 8. Diese Datei regelt das Wie.

## Projektkennung
`<YYYY-MM-DD>-<slug>-<4 Zeichen>` (z. B. `2026-11-08-rechnungsimport-k3f9`, Suffix zufällig aus a–z und 0–9). Einmal vergeben, nie geändert; steht im Ordnernamen und im Kopf von `PROGRESS.md`.

## Vor dem ersten Schreiben
1. Ort beschreibbar und nach Projektregeln erlaubt? Sonst den anderen Ort nehmen oder nach einem Pfad fragen.
2. Kollision: Existiert der Ordner schon, ein neues Suffix ziehen.
3. Liegt der Ort in einem Git-Repo: mit `git check-ignore` prüfen. Ist er nicht ignoriert und erlauben die Projektregeln Änderungen an Git-Metadaten, den Pfad in `.git/info/exclude` eintragen (lokal, nicht versioniert) und das nennen. Sonst den Desktop nehmen oder nach einem Ort außerhalb des Repos fragen.
4. **Sensible Rohdaten** (Kundendaten, Exporte, Zugangsdaten, private Medien) bleiben am freigegebenen Projektort; das Gedächtnis enthält nur Pfade, Zusammenfassungen und Kennzahlen.

## Dateien (Vorlagen in `templates/`)
- **Kern:** `PROGRESS.md` ist maßgeblich für Projektkennung, Vorhaben (ein Satz), Arbeitsordner, Gedächtnisort, den **unmittelbar nächsten Schritt mit Freigabestatus**, die Zähler (`references/failure-learning.md`), die Freigaben mit Status (`references/einmalige-aktionen.md`) und gegebenenfalls den Messplan. `NEXT_STEPS.md` enthält nur nachgelagerte Schritte und offene Fragen mit „gestellt am“; bei Widerspruch gilt `PROGRESS.md`.
- **Bei Bedarf:** `PROJECT_BRIEF.md` (Ziel, Kriterien), `DECISIONS.md` (Entscheidungen, Annahmen, Absichten des Users), `ARCHITECTURE.md` (mehrere Bausteine), `IMPLEMENTATION_PLAN.md` (mehr als ca. 5 Schritte), `TEST_RESULTS.md` (iteratives Testen, Details je Versuch).

## Hochstufen auf L oder Übergang in eine weitere Session
Gedächtnis sofort anlegen und aus dem Chat übernehmen, was die Fortsetzung braucht: Ergebnisse, Versuche mit Ergebnis, gescheiterte Ansätze mit Grund, Entscheidungen und Annahmen, Freigaben mit Status, gestellte Fragen mit Datum. Zähler nur mit Beleg übernehmen, sonst **unbekannt**, nie 0. Ist ein Zähler oder Freigabestatus unbekannt, vor dem nächsten kostenpflichtigen oder freigabepflichtigen Versuch rekonstruieren (Chatverlauf, Logs, Zielsystem); gelingt das nicht, das Budget vom User neu bestätigen lassen. Kostenlose, harmlose Versuche dürfen weiterlaufen.

## Fortsetzung
1. Kandidaten suchen: `~/Desktop` und, falls bekannt, `<arbeitsordner>/.guided/` nach Stichwort oder Projektkennung.
2. **Jeden** Treffer prüfen, auch einen einzelnen: Passen Vorhaben und Arbeitsordner im `PROGRESS.md`-Kopf zum Auftrag, und existiert der Arbeitsordner? Nicht passende verwerfen.
3. Mehrere passende Treffer: mit Projektkennung, Datum und Vorhaben zur Auswahl stellen. Keiner und Arbeitsordner unbekannt: gezielt nach dem Pfad fragen.
4. `PROGRESS.md` und `NEXT_STEPS.md` lesen, weitere Dateien nur bei Bedarf. Zähler übernehmen, Freigaben nach SKILL.md 1b prüfen, offene Status nach `references/einmalige-aktionen.md` klären, bereits gestellte Fragen nicht wiederholen. Stand in einem Satz melden und weitermachen.

## Übergabetest
Könnte eine neue Session mit `PROGRESS.md` und `NEXT_STEPS.md` in einer Minute weitermachen? Wenn nein, nachschärfen. `PROGRESS.md` unter ca. 60 Zeilen halten, verlinken statt kopieren.
