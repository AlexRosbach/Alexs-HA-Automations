# Eine Aufgabenliste lesen und Einträge entfernen · mit Bedingungen im Ablauf

[English](README.md) · **Deutsch**

[Aufgabenlisten und Erinnerungen](../../../README.de.md#tasks) → [Einträge entfernen](../../../README.de.md#tasks-remove)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Eine Aufgabenliste abfragen → wiederholen für jeden Listeneintrag: Zwischenwerte vorbereiten (ausgewählte Schritte; 4 weitere Aktionen ausgelassen).

## Wann startet sie?

- **1.** Auslösertyp nicht erhalten: Stunden: nicht erhalten

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

2. Eine Aufgabenliste abfragen — `todo.example_01`; Rückgabe für spätere Schritte speichern.

3. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

4. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

5. Für jeden Listeneintrag wiederholen; Anzahl Einträge: nicht erhalten.

   1. 4 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   2. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** Bedingungsformel nicht erhalten

      1. Ein eigenes Skript ausführen — `script.todo`.

      Kein Standardzweig eingestellt.

6. Für jeden Listeneintrag wiederholen; Anzahl Einträge: nicht erhalten.

   1. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   2. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** Bedingungsformel nicht erhalten

      1. Einen Eintrag aus einer Aufgabenliste entfernen — `todo.example_01`; Aufgabeneintrag: nicht erhalten.

      Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein vorhandenes Home-Assistant-Skript, also eine gespeicherte Folge von Aktionen.
- Eine in Home Assistant eingerichtete Aufgabenliste.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
