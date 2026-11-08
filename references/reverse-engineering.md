# Reverse Engineering: aus Beispielen Regeln machen

**Lohnt sich, wenn:** gute Beispiele oder ein Altsystem existieren, sie implizites Wissen enthalten (Stil, Regeln, Entscheidungslogik) und Erfragen teurer oder unzuverlässiger wäre als Ableiten. **Nicht, wenn:** keine aussagekräftigen Beispiele da sind, die Regel einfach erfragbar ist oder das Ziel bewusst vom Bestehenden abweichen soll.

**Kurzform bei Klasse S:** nur Schritte 2 bis 4, Befund im Chat, Regeln als vorläufig kennzeichnen. Ein Regelwerk nur speichern (Schritt 6), wenn es wiederverwendet wird; die Absicht nur bei M und L abfragen (Schritt 7).

1. **Korpus festlegen:** Welche Beispiele zählen (beste, typische, gescheiterte)? Menge so klein wie möglich, so groß wie nötig. Bei genug Beispielen einige als Gegenprobe zurückhalten.
2. **Messbares extrahieren:** zuerst maschinell (Metadaten, Längen, Zeitstempel, Häufigkeiten, Strukturen). Für Formate mit eigenen Analysewerkzeugen (Code, Logs, Tabellen, Medien, Dokumente) die Fach-Werkzeuge des Projekts nutzen; nie schätzen, was messbar ist.
3. **Beobachtungen notieren** (Tabelle: Beispiel | Merkmal | Wert | Fundstelle). Nur Gemessenes.
4. **Hypothesen bilden:** „Wenn A, dann B“ mit Häufigkeit („in 7 von 9 Beispielen“).
5. **Gegenprobe** an den zurückgehaltenen Beispielen: Sagt die Regel sie richtig vorher? Treffer/Fehler zählen. Bei zu wenigen Beispielen für eine Gegenprobe bleibt jede abgeleitete Regel **vorläufig**.
6. **Regelwerk speichern** (Ergebnisdatei, nicht Projektgedächtnis), je Regel zwei getrennte Felder:
   - **Empirisch:** Häufigkeit, Gegenprobe ja/nein, Status vorläufig oder bestätigt.
   - **Absicht:** vom User bestätigt ja/nein/offen.
   Maschinenlesbar, wenn ein Programm sie nutzen soll (JSON/YAML), sonst Markdown.
7. **Absicht beim User abfragen**, wo Geschmack im Spiel ist (zählt als Interview nach SKILL.md Abschnitt 5, nicht als Discovery-Runde): „Ich lese heraus, dass du X machst. Stimmt das, und ist es Absicht?“ Eine bestätigte Absicht darf eine Messung übersteuern, ersetzt aber keine empirische Bestätigung; beides wird getrennt geführt.
