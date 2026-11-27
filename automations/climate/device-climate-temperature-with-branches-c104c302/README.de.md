# Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf — Variante B

[English](README.md) · **Deutsch**

[Heizung und Raumklima](../../../README.de.md#climate) → [Temperatur einstellen](../../../README.de.md#climate-temperature)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Wiederholen bis Bedingungen erfüllt sind: Temperatur auf 5 setzen → wiederholen bis Bedingungen erfüllt sind: Temperatur auf 5 setzen → wenn die eingestellten Bedingungen erfüllt sind: (Temperatur auf 21 setzen) → 1 weiterer Schritt (siehe Ablauf).

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Auslösertyp nicht erhalten: `ENTITY_31`, `DEVICE_39`; Geräteereignis/-aktion: nicht erhalten
- **2.** Auslösertyp nicht erhalten: `ENTITY_31`, `DEVICE_39`; Geräteereignis/-aktion: nicht erhalten
- **3.** Auslösertyp nicht erhalten: `ENTITY_32`, `DEVICE_40`; Geräteereignis/-aktion: nicht erhalten
- **4.** Auslösertyp nicht erhalten: `ENTITY_32`, `DEVICE_40`; Geräteereignis/-aktion: nicht erhalten

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Mindestens einmal ausführen, danach wiederholen, bis alle folgenden: Bedingungstyp nicht erhalten: `ENTITY_31`, `DEVICE_39`; Geräteereignis/-aktion: nicht erhalten.

   1. Die gewünschte Raumtemperatur einstellen — `climate.example_05`; Temperaturwert (Einheit nicht angegeben): 5; Heiz-/Kühlmodus: nicht erhalten.

2. Mindestens einmal ausführen, danach wiederholen, bis alle folgenden: Bedingungstyp nicht erhalten: `ENTITY_31`, `DEVICE_39`; Geräteereignis/-aktion: nicht erhalten.

   1. Die gewünschte Raumtemperatur einstellen — `climate.example_05`; Temperaturwert (Einheit nicht angegeben): 5; Heiz-/Kühlmodus: nicht erhalten.

3. Wenn alle folgenden: Bedingungstyp nicht erhalten: `ENTITY_32`, `DEVICE_40`; Geräteereignis/-aktion: nicht erhalten:

   **Dann:**

   1. Die gewünschte Raumtemperatur einstellen — `climate.example_05`; Temperaturwert (Einheit nicht angegeben): 21; Heiz-/Kühlmodus: nicht erhalten.

4. Wenn alle folgenden: Bedingungstyp nicht erhalten: `ENTITY_32`, `DEVICE_40`; Geräteereignis/-aktion: nicht erhalten:

   **Dann:**

   1. Die gewünschte Raumtemperatur einstellen — `climate.example_05`; Temperaturwert (Einheit nicht angegeben): 21; Heiz-/Kühlmodus: nicht erhalten.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein eingebundenes Thermostat oder eine Klimaanlage.
- Ein eingebundenes Gerät mit einem passenden Ereignis als Auslöser.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
