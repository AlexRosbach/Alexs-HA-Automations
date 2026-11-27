# Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante C

[English](README.md) · **Deutsch**

[Aufgabenlisten und Erinnerungen](../../../README.de.md#tasks) → [Aufgabenlisten abfragen](../../../README.de.md#tasks-read)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Wenn die eingestellten Bedingungen erfüllt sind: (Eine Nachricht senden) → wenn die eingestellten Bedingungen erfüllt sind: (Eine Nachricht senden → Eine Aufgabenliste abfragen → 2 weitere Schritte).

## Wann startet sie?

- **1.** Auslösertyp nicht erhalten: `sensor.example_03`

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Wenn alle folgenden: Bedingungstyp nicht erhalten: `sensor.example_03`; Zustand: nicht erhalten:

   **Dann:**

   1. Eine Nachricht senden; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

2. Wenn alle folgenden: Bedingungstyp nicht erhalten: `sensor.example_03`; Zustand: nicht erhalten:

   **Dann:**

   1. Eine Nachricht senden; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

   2. Eine Aufgabenliste abfragen — `todo.example_01`; Aufgabenstatus: nicht erhalten; Rückgabe für spätere Schritte speichern.

   3. 2 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   4. Wenn alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten:

      **Dann:**

      1. Ein eigenes Skript ausführen — `script.todo`.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Ein vorhandenes Home-Assistant-Skript, also eine gespeicherte Folge von Aktionen.
- Eine in Home Assistant eingerichtete Aufgabenliste.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
