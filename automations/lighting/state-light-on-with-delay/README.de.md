# Licht einschalten · mit Wartezeit im Ablauf

[English](README.md) · **Deutsch**

[Licht](../../../README.de.md#lighting) → [Einschalten](../../../README.de.md#lighting-on)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Licht mit 5 % Helligkeit einschalten → wenn Zustand: `off`: (Einen Schalter einschalten → warten für 5 min → 1 weiterer Schritt). Starteinstellungen: von Zustand: `off`; zu Zustand: `on`. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

- **1.** Zustandsänderung: `binary_sensor.example_22`; von Zustand: `off`; zu Zustand: `on`

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Zustandsprüfung: `sun.example_01`; Zustand: nicht erhalten; Zustandsprüfung: `light.example_17`; Zustand: `on`.

## Konkreter Ablauf

1. Licht einschalten — `light.example_17`; Helligkeit: 5%.

2. Wenn alle folgenden: Zustandsprüfung: `input_boolean.example_12`; Zustand: `off`:

   **Dann:**

   1. Einen Schalter einschalten — `switch.example_14`.

   2. Warten für 5 min.

   3. Wenn alle folgenden: Zustandsprüfung: `input_boolean.example_12`; Zustand: `off`:

      **Dann:**

      1. Einen Schalter ausschalten — `switch.example_14`.

## Wenn sie erneut ausgelöst wird

`restart`: Ein neuer Auslöser stoppt den laufenden Durchlauf und startet neu, sofern die Bedingungen der Automation erfüllt sind.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Lampen, die Home Assistant steuern kann.
- Einen Schalter oder eine schaltbare Steckdose in Home Assistant.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
