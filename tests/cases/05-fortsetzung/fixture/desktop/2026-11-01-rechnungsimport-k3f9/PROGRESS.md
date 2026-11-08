# PROGRESS · Rechnungsimport

**Projektkennung:** 2026-11-01-rechnungsimport-k3f9 · **Vorhaben:** Eingangsrechnungen aus dem Postfach automatisch als Buchungssätze in die Buchhaltung importieren
**Arbeitsordner:** {CASE_DIR}/projekte/rechnungsimport · **Gedächtnisort:** {CASE_DIR}/desktop/2026-11-01-rechnungsimport-k3f9 · **Git-ignoriert:** nicht im Repo
**Klasse:** L · **Stand:** 2026-11-07 · **Strategie:** Vorhandenes nutzen (OCR-Dienst), dann Zuordnungsregeln

## Nächster Schritt (maßgeblich)
**Schritt:** Bezahlten OCR-Testlauf mit 50 Rechnungs-PDFs beim OCR-Dienst ausführen · **Bestanden, wenn:** mindestens 45 von 50 Beträgen korrekt erkannt
**Freigabestatus:** F1 (Status siehe Tabelle)
**Wer ist dran:** Agent

## Zähler (gelten über Sessions und Strategiewechsel hinweg)
| Zähler | Stand | Grenze |
|---|---|---|
| Budget verbraucht | 6 von 10 Versuchen · 4 h · 9 € | 10 Versuche · 30 € |
| Gescheiterte Ansätze | 2 | 3 |
| Serie ohne Mindestfortschritt (aktueller Ansatz A3) | 1 | 2 |
Mindestfortschritt je Versuch: +5 korrekt erkannte Beträge · Letzter Versuch: V6

## Freigaben
| Nr | Datum | Umfang (was, wo, wie viel) | Art (einmalig/wiederholt) | Gültig bis/solange | Status mit Zeit und Beleg | Beleg der Zusage |
|---|---|---|---|---|---|---|
| F1 | 2026-11-07 | OCR-Testlauf, 50 PDFs, OCR-Dienst, max. 12 € | einmalig | bis 2026-11-14 | reserviert 2026-11-07 18:01 | „Ja, mach den Test mit den 50 PDFs, max 12 Euro“ (Chat 07.11.) |

## Muss-Kriterien
| Kriterium | Status | Beleg |
|---|---|---|
| Beträge korrekt (>= 90 %) | offen | |
| Lieferant korrekt zugeordnet | offen | |

## Verlauf
- 2026-11-01 · Start, Klasse L
- 2026-11-05 · A1 (Regex auf PDF-Text) gescheitert: gescannte PDFs ohne Text
- 2026-11-06 · A2 (lokales Tesseract) gescheitert: 2 Versuche ohne Fortschritt
- 2026-11-07 · A3 OCR-Dienst, V6 kostenlose Probe mit 5 PDFs: 3 von 5 korrekt
