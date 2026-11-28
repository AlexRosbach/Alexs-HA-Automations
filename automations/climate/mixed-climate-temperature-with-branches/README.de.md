# Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf

[English](README.md) · **Deutsch**

[Heizung und Raumklima](../../../README.de.md#climate) → [Temperatur einstellen](../../../README.de.md#climate-temperature)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Bedingungen prüfen; bei falsch diesen Ablauf stoppen → wenn Zustand: `on`; 2 weitere Prüfungen: (Die gewünschte Raumtemperatur einstellen) → Einen gespeicherten Ein/Aus-Wert ausschalten. Starteinstellungen: um 18:00:00 / Home-Assistant-Ereignis; 2 weitere Auslöser in den Details. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Feste Uhrzeit: um 18:00:00
- **2.** Home-Assistant-Ereignis: Ereignis: `start`
- **3.** Zustandsänderung: `input_text.example_03`; zu Zustand: nicht erhalten
- **4.** Wiederholter Zeitplan: Minuten: /5

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Formelprüfung: Formel: “\{\{ now\(\).hour&gt;=18 or states\('input\_text.example\_01'\) \!= now\(\).date\(\)\|string \}\}”.

## Konkreter Ablauf

1. Prüfen: Formelprüfung: Formel: “\{\{ states\('input\_text.example\_03'\) == '' \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

2. Wenn alle folgenden: Zustandsprüfung: `input_boolean.example_14`; Zustand: `on`; Zustandsprüfung: `climate.example_04`; Zustand: `heat`; Formelprüfung: Formel: “\{\{ state\_attr\('climate.example\_04','temperature'\)\|float\(0\)==21 and states\('input\_text.example\_04'\) in \['auto','heat'\] \}\}”:

   **Dann:**

   1. Die gewünschte Raumtemperatur einstellen — `climate.example_04`; Temperaturwert (Einheit nicht angegeben): nicht erhalten; Heiz-/Kühlmodus: nicht erhalten.

3. Einen gespeicherten Ein/Aus-Wert ausschalten — `input_boolean.example_14`.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein eingebundenes Thermostat oder eine Klimaanlage.
- Einen Ein/Aus-Helfer: ein gespeicherter Schalterwert in Home Assistant.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
