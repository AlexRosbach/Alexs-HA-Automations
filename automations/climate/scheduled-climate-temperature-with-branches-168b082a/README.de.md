# Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf — Variante A

[English](README.md) · **Deutsch**

[Heizung und Raumklima](../../../README.de.md#climate) → [Temperatur einstellen](../../../README.de.md#climate-temperature)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Einen Textwert speichern → wenn Zustand: `off`; 2 weitere Prüfungen: (Einen Textwert speichern → Einen Zahlenwert speichern → 2 weitere Schritte). Starteinstellungen: um 06:45:00. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

- **1.** Feste Uhrzeit: um 06:45:00

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Zeitprüfung: Wochentage: `mon`, `tue`, `wed`, `thu`, `fri`; Zustandsprüfung: `person.example_02`; Zustand: `home`; Zustandsprüfung: `sensor.example_22`; Zustand: nicht erhalten; Dauer 00:10:00 (Zeitformat); Formelprüfung: Formel: “\{\{ states\('input\_text.example\_02'\) \!= now\(\).date\(\)\|string \}\}”; Formelprüfung: Formel: “\{\{ not is\_state\('calendar.example\_01','IDENTIFIER\_160'\) \}\}”.

## Konkreter Ablauf

1. Einen Textwert speichern — `input_text.example_01`; gespeicherter Wert: “\{\{ now\(\).date\(\) \}\}”.

2. Wenn alle folgenden: Zustandsprüfung: `binary_sensor.example_15`; Zustand: `off`; Formelprüfung: Formel: “\{\{ states\('climate.example\_04'\) in \['auto','heat'\] and state\_attr\('climate.example\_04','temperature'\) is number \}\}”; Formelprüfung: Formel: “\{\{ states\('input\_text.example\_03'\) == '' \}\}”:

   **Dann:**

   1. Einen Textwert speichern — `input_text.example_04`; gespeicherter Wert: “\{\{ states\('climate.example\_04'\) \}\}”.

   2. Einen Zahlenwert speichern — `input_number.example_01`; gespeicherter Wert: “\{\{ state\_attr\('climate.example\_04','temperature'\) \}\}”.

   3. Die gewünschte Raumtemperatur einstellen — `climate.example_04`; Temperaturwert (Einheit nicht angegeben): 21; Heiz-/Kühlmodus: `heat`.

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
