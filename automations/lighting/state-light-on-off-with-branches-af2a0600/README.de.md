# Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante C

[English](README.md) · **Deutsch**

[Licht](../../../README.de.md#lighting) → [Ein- und Ausschalten](../../../README.de.md#lighting-on-off)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Den ersten passenden Zweig ausführen: Einen Schalter einschalten → Licht einschalten / Einen Schalter ausschalten → wenn die eingestellten Bedingungen erfüllt sind: (Licht ausschalten). Starteinstellungen: Dauer 1 min / Dauer 5 min. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Auslösertyp nicht erhalten: `binary_sensor.example_24`; von Zustand: nicht erhalten; zu Zustand: nicht erhalten; Dauer 1 min; Auslöser-Verweis: `ID_22`
- **2.** Auslösertyp nicht erhalten: `binary_sensor.example_24`; zu Zustand: nicht erhalten; Dauer 5 min; Auslöser-Verweis: `ID_23`

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Bedingungstyp nicht erhalten: `input_boolean.example_05`; Zustand: nicht erhalten.

## Konkreter Ablauf

1. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Auslöser-Verweis: `ID_22`

   1. Einen Schalter einschalten — `switch.example_03`.

   2. Licht einschalten — `light.example_01`.

   **Zweig 2:** alle folgenden: Bedingungstyp nicht erhalten: Auslöser-Verweis: `ID_23`

   1. Einen Schalter ausschalten — `switch.example_03`.

   2. Wenn alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten:

      **Dann:**

      1. Licht ausschalten — `light.example_01`.

   Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

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
