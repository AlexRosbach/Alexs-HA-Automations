# Eigene Aktion einrichten · mit Wartebedingung im Ablauf — Variante A

[English](README.md) · **Deutsch**

[Weitere Abläufe und Geräteaktionen](../../../README.de.md#system) → [Noch einzurichtende Aktionen](../../../README.de.md#system-unfinished)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Wenn die eingestellten Bedingungen erfüllt sind: (wenn unter 10: (Geräteaktion: `turn_on` → warten auf von Zustand: `on`; zu Zustand: `off` (bis zu 1 min; bei Ablauf weiter) → 1 weiterer Schritt)). Starteinstellungen: Geräteereignis.

## Wann startet sie?

- **1.** Geräteereignis: `ENTITY_36`, `DEVICE_45`; Geräteereignis/-aktion: `occupied`

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Wenn alle folgenden: Geräteprüfung: `ENTITY_36`, `DEVICE_45`; Geräteereignis/-aktion: nicht erhalten:

   **Dann:**

   1. Wenn alle folgenden: Zahlenprüfung: `sensor.example_07`; unter 10:

      **Dann:**

      1. Geräteaktion: `turn_on` — `ENTITY_37`, `DEVICE_46`.

      2. Auf einen dieser Auslöser warten:

         - Zustandsänderung: `binary_sensor.example_28`; von Zustand: `on`; zu Zustand: `off`

         Zeitgrenze: 1 min. Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

      3. Geräteaktion: `turn_off` — `ENTITY_37`, `DEVICE_46`.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Die Geräte und die Aktion, die du selbst ergänzen möchtest.
- Ein eingebundenes Gerät mit einem passenden Ereignis als Auslöser.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
