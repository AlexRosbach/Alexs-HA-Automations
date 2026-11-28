# Eine Aufgabenliste lesen und bearbeiten · mit Bedingungen im Ablauf — Variante A

[English](README.md) · **Deutsch**

[Aufgabenlisten und Erinnerungen](../../../README.de.md#tasks) → [Einträge bearbeiten](../../../README.de.md#tasks-edit)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Eine Aufgabenliste abfragen; Aufgabenstatus: `needs_action` → Zwischenwerte vorbereiten → wiederholen für jeden Listeneintrag: Zwischenwerte vorbereiten. Starteinstellungen: Stunden: /1.

## Wann startet sie?

- **1.** Wiederholter Zeitplan: Stunden: /1

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Eine Aufgabenliste abfragen — `todo.example_01`; Aufgabenstatus: `needs_action`; Rückgabe für spätere Schritte speichern.

2. 2 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

3. Für jeden Listeneintrag wiederholen; Anzahl Einträge: nicht erhalten.

   1. 4 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   2. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Formelprüfung: Formel: “\{\{ repeat.item in variable\_09 and \(variable\_14 not in \(variable\_21\['todo.example\_01'\]\['items'\] \| map\(attribute='variable\_15'\) \| list\)\) \}\}”

      1. Ein eigenes Skript ausführen — `script.example_01`.

      Kein Standardzweig eingestellt.

   3. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Formelprüfung: Formel: “\{\{ repeat.item not in variable\_09 \}\}”

      1. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

      2. Wenn alle folgenden: Formelprüfung: Formel: “\{\{ variable\_23 is defined and variable\_23 \}\}”:

         **Dann:**

         1. Einen Eintrag in einer Aufgabenliste ändern — `todo.example_01`; Aufgabenstatus: `completed`; Aufgabeneintrag: “\{\{ variable\_23.uid \}\}”.

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
