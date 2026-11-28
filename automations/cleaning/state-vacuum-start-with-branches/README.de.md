# Einen Saugroboter starten · mit Bedingungen im Ablauf

[English](README.md) · **Deutsch**

[Saugroboter](../../../README.de.md#cleaning) → [Starten](../../../README.de.md#cleaning-start)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Wenn Zustand: `not_home`; 1 weitere Prüfung: (wenn Zustand: `off`: (Eine Nachricht senden; Nachrichtentext: “Keiner zuhause. Es wird sauber gemacht.”; Nachrichtentitel: “Staubsauger” → Einen gespeicherten Ein/Aus-Wert einschalten → 1 weiterer Schritt)). Starteinstellungen: Zustandsänderung.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Zustandsänderung: `person.example_02`
- **2.** Zustandsänderung: `person.example_01`

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Wenn alle folgenden: Zustandsprüfung: `person.example_01`; Zustand: `not_home`; Zustandsprüfung: `person.example_02`; Zustand: `not_home`:

   **Dann:**

   1. Wenn alle folgenden: Zustandsprüfung: `input_boolean.example_05`; Zustand: `off`:

      **Dann:**

      1. Eine Nachricht senden; Nachrichtentext: “Keiner zuhause. Es wird sauber gemacht.”; Nachrichtentitel: “Staubsauger”.

      2. Einen gespeicherten Ein/Aus-Wert einschalten — `input_boolean.example_05`.

      3. Einen Saugroboter starten — `vacuum.example_03`, `vacuum.example_02`, `vacuum.example_04`, `vacuum.example_05`, `vacuum.example_06`, `DEVICE_07`.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Einen Ein/Aus-Helfer: ein gespeicherter Schalterwert in Home Assistant.
- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Einen in Home Assistant eingebundenen Saugroboter.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
