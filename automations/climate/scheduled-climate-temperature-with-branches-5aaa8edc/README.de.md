# Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf — Variante B

[English](README.md) · **Deutsch**

[Heizung und Raumklima](../../../README.de.md#climate) → [Temperatur einstellen](../../../README.de.md#climate-temperature)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Einen Textwert speichern → wenn die eingestellten Bedingungen erfüllt sind: (Einen Textwert speichern → Einen Zahlenwert speichern → 2 weitere Schritte). Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

- **1.** Auslösertyp nicht erhalten: um nicht erhalten

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Bedingungstyp nicht erhalten: Wochentage: nicht erhalten, nicht erhalten, nicht erhalten, nicht erhalten, nicht erhalten; Bedingungstyp nicht erhalten: `person.example_02`; Zustand: nicht erhalten; Bedingungstyp nicht erhalten: `sensor.example_16`; Zustand: nicht erhalten; Dauer nicht erhalten; Bedingungstyp nicht erhalten: Formel: nicht erhalten; Bedingungstyp nicht erhalten: Formel: nicht erhalten.

## Konkreter Ablauf

1. Einen Textwert speichern — `input_text.example_02`; gespeicherter Wert: nicht erhalten.

2. Wenn alle folgenden: Bedingungstyp nicht erhalten: `binary_sensor.example_07`; Zustand: nicht erhalten; Bedingungstyp nicht erhalten: Formel: nicht erhalten; Bedingungstyp nicht erhalten: Formel: nicht erhalten:

   **Dann:**

   1. Einen Textwert speichern — `input_text.example_03`; gespeicherter Wert: nicht erhalten.

   2. Einen Zahlenwert speichern — `input_number.example_01`; gespeicherter Wert: nicht erhalten.

   3. Die gewünschte Raumtemperatur einstellen — `climate.example_04`; Temperaturwert (Einheit nicht angegeben): 21; Heiz-/Kühlmodus: nicht erhalten.

   4. Einen gespeicherten Ein/Aus-Wert einschalten — `input_boolean.example_14`.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein eingebundenes Thermostat oder eine Klimaanlage.
- Einen Ein/Aus-Helfer: ein gespeicherter Schalterwert in Home Assistant.
- Einen Helfer, der einen Zahlenwert speichert.
- Einen Helfer, der einen Textwert speichert.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
