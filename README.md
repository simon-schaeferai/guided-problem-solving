# guided-problem-solving

*Ich wollte keinen Agenten, der schöne Pläne schreibt. Ich wollte einen, der mich wie ein erfahrener Problemlösungsarchitekt von einer unklaren Idee zu einem Ergebnis führt, das nachweislich funktioniert, und der dabei weiß, wann er fragen muss und wann nicht. Simon Schaefer, November 2026*

Die Idee: ein Claude-Code-Skill für Probleme jeder Art, ob Software, Automatisierung, Business-Prozess, Design, Recherche oder etwas Kreatives. Er stuft zuerst den Arbeitsumfang ein (S, M, L) und prüft davon getrennt das Risiko jeder einzelnen Aktion. Dann wählt er nur die Schritte und die Methode, die das Problem wirklich braucht: direkt lösen, recherchieren, debuggen, Prototyp, Experiment, Reverse Engineering oder Optimierung. Er setzt in kleinen prüfbaren Schritten um, lernt aus Fehlschlägen mit festen Abbruchgrenzen und meldet „fertig“ nur mit Beleg für jedes Muss-Kriterium. Geht ein Vorhaben über eine Session hinaus, legt er ein knappes Projektgedächtnis an, mit dem die nächste Session in einer Minute weitermacht. Die Leitmetrik ist die Zeit bis zum ersten belastbar geprüften Ergebnis, nicht die Ausführlichkeit des Plans.

## How it works

- **`SKILL.md`** · der Kern in acht Abschnitten: Einstufung und Freigaben, Grundregeln, Kernschleife, Strategie-Wahl, Fragen, Fehler-Lernschleife, Validierung, Projektgedächtnis. Für einfache Aufgaben genügen vier davon. Hier arbeitest du, wenn du den Skill anpasst.
- **`references/`** · sechs Vertiefungen, die der Skill nur lädt, wenn der Fall eintritt: Discovery und Interview, Critical Review, Reverse Engineering, Budget und Zähler, Schutz vor Doppelausführung, Projektgedächtnis.
- **`templates/`** · sieben Vorlagen für das Projektgedächtnis. Maßgeblich ist `PROGRESS.md` (nächster Schritt, Freigabestatus, Zähler, Freigaben); alle anderen entstehen nur, wenn sie Inhalt haben.
- **`tests/`** · fünf feste Testfälle mit maschineller Prüfung. Nach jeder Änderung am Skill: `python3 tests/run.py` (Details in `tests/README.md`).

Die zentrale Konstante: Einfache Probleme bleiben einfach (höchstens drei kostenlose Versuche, kein Ballast). Sobald Versuche Geld oder viel Zeit kosten, greifen **drei Zähler** (Budget, gescheiterte Ansätze bis 3, Versuche ohne Fortschritt bis 2), die kein Strategie- oder Sessionwechsel zurücksetzt.

## Quick start

**Requirements:** [Claude Code](https://claude.com/claude-code). Keine Keys, keine Abhängigkeiten.

```bash
# global, in allen Projekten verfügbar
git clone https://github.com/simon-schaeferai/guided-problem-solving ~/.claude/skills/guided-problem-solving

# oder nur für ein Projekt
git clone https://github.com/simon-schaeferai/guided-problem-solving .claude/skills/guided-problem-solving
```

Neue Claude-Code-Session starten. Steht `guided-problem-solving` in der Skill-Liste, bist du startklar.

## Using it

```
Führ mich durch: Ich will meine Rechnungen aus dem Postfach automatisch in die Buchhaltung bringen.
```

Später in einer neuen Session:

```
Mach weiter mit dem Rechnungsimport.
```

## Design choices

- **Arbeitsumfang und Risiko sind getrennt.** Eine Rechteänderung mit einem Befehl ist „klein“, braucht aber trotzdem eine Freigabe. Preis: Auch bei S-Aufgaben läuft ein stiller Risiko-Check mit.
- **Schweigen ist nie eine Freigabe.** Defaults gelten nur für umkehrbare Entscheidungen. Preis: Bei bezahlten Tests oder Veröffentlichungen wartet der Agent, statt weiterzumachen.
- **Fragen sind gedeckelt.** S fragt nicht, M höchstens eine Runde, L höchstens zwei; zwingende Blocker werden einzeln gefragt und sonst als blockiert gemeldet. Preis: Manchmal baut der Agent mit einer Annahme, die du korrigieren musst.
- **Gedächtnis nur bei Bedarf, bevorzugt auf dem Desktop.** Du findest den Stand sofort, ohne in versteckten Ordnern zu suchen. Ohne Desktop (Server, Container) fällt es auf `<arbeitsordner>/.guided/` zurück und wird vor dem Schreiben gegen Git-Commits abgesichert. Preis: Der Desktop füllt sich bei vielen Vorhaben.
- **„Fertig“ heißt belegt.** Ohne Beleg je Muss-Kriterium meldet der Skill „teilweise fertig“. Preis: ehrlichere, aber manchmal unbequemere Abschlussmeldungen.

## Limitations

- Der Skill ist auf Deutsch geschrieben. Ein englischer Fork ist willkommen.
- Er wurde mit unabhängigen Audits und fünf Testläufen in einer Sandbox nachgeschärft (Bugfix, Automatisierung, Business-Problem, kreative Aufgabe, Fortsetzung mit bezahlter Aktion). Die Antworten des Users waren dabei simuliert; viele echte Läufe stehen noch aus.
- Die Einstufung S, M, L ist eine Urteilsfrage des Modells. Ein riskantes Problem, das harmlos wirkt, kann zu niedrig eingestuft werden; die Freigabeprüfung pro Aktion fängt das bei kritischen Aktionen ab, nicht bei Qualitätsfragen.
- Projektregeln (zum Beispiel `CLAUDE.md`) haben Vorrang. In streng geregelten Projekten verhält sich der Skill deshalb vorsichtiger.

## License

MIT
