# Heizung oder Klimaanlage einstellen · mit Bedingungen im Ablauf — Variante D

[English](README.md) · **Deutsch**

[Heizung und Raumklima](../../../README.de.md#climate) → [Heiz- und Kühlmodus](../../../README.de.md#climate-modes)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Den ersten passenden Zweig ausführen: Temperatur auf 5 setzen → Den Heiz- oder Kühlbetrieb einstellen / Den Heiz- oder Kühlbetrieb einstellen → Temperatur auf 21 setzen.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Auslösertyp nicht erhalten: `binary_sensor.example_06`; zu Zustand: nicht erhalten; Auslöser-Verweis: `ID_09`
- **2.** Auslösertyp nicht erhalten: `binary_sensor.example_06`; zu Zustand: nicht erhalten; Auslöser-Verweis: `ID_10`

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Auslöser-Verweis: `ID_09`

   1. Die gewünschte Raumtemperatur einstellen — `climate.example_02`; Temperaturwert (Einheit nicht angegeben): 5.

   2. Den Heiz- oder Kühlbetrieb einstellen — `climate.example_02`; Heiz-/Kühlmodus: nicht erhalten.

   **Zweig 2:** alle folgenden: Bedingungstyp nicht erhalten: Auslöser-Verweis: `ID_10`

   1. Den Heiz- oder Kühlbetrieb einstellen — `climate.example_02`; Heiz-/Kühlmodus: nicht erhalten.

   2. Die gewünschte Raumtemperatur einstellen — `climate.example_02`; Temperaturwert (Einheit nicht angegeben): 21.

   Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

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
