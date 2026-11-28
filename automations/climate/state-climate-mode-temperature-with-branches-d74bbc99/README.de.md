# Heizung oder Klimaanlage einstellen · mit Bedingungen im Ablauf — Variante D

[English](README.md) · **Deutsch**

[Heizung und Raumklima](../../../README.de.md#climate) → [Heiz- und Kühlmodus](../../../README.de.md#climate-modes)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Den ersten passenden Zweig ausführen: Temperatur auf 5 setzen → Den Heiz- oder Kühlbetrieb einstellen; Heiz-/Kühlmodus: `off`; sonst: Den Heiz- oder Kühlbetrieb einstellen; Heiz-/Kühlmodus: `heat_cool` → Temperatur auf 21 setzen. Starteinstellungen: zu Zustand: `on`, `off`. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

- **1.** Zustandsänderung: `binary_sensor.example_14`, `binary_sensor.example_16`, `binary_sensor.example_17`, `binary_sensor.example_15`, `binary_sensor.example_18`, `binary_sensor.example_19`, `binary_sensor.example_20`; zu Zustand: `on`, `off`

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Formelprüfung: Formel: “\{\{ false \}\}”.

## Konkreter Ablauf

Die Automation bereitet außerdem Zwischenwerte vor; ihre Inhalte/Formeln sind nicht beschrieben.

1. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Formel: “\{\{ variable\_53 \}\}”

   1. Die gewünschte Raumtemperatur einstellen — `ENTITY_43`; Temperaturwert (Einheit nicht angegeben): 5.

   2. Den Heiz- oder Kühlbetrieb einstellen — `ENTITY_43`; Heiz-/Kühlmodus: `off`.

   **Wenn kein Zweig passt:**

   1. Den Heiz- oder Kühlbetrieb einstellen — `ENTITY_43`; Heiz-/Kühlmodus: `heat_cool`.

   2. Die gewünschte Raumtemperatur einstellen — `ENTITY_43`; Temperaturwert (Einheit nicht angegeben): 21.

## Wenn sie erneut ausgelöst wird

`queued`: Neue Durchläufe warten in einer Warteschlange und laufen in Eingangsreihenfolge. Sie werden nur eingereiht, wenn die Bedingungen beim Auslösen erfüllt sind. Grenze für laufende und wartende Durchläufe: 10. Die Automation ist anfangs deaktiviert.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein eingebundenes Thermostat oder eine Klimaanlage.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
