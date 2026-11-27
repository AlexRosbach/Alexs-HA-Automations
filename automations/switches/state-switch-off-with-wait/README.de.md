# Einen Schalter ausschalten · mit Wartebedingung im Ablauf

[English](README.md) · **Deutsch**

[Schalter und Steckdosen](../../../README.de.md#switches) → [Ausschalten](../../../README.de.md#switches-off)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Warten auf einen Wert über 7.999 oder 5 weitere Auslöser (bei Ablauf weiter) → wenn die eingestellten Bedingungen erfüllt sind: (Einen Schalter ausschalten) (ausgewählte Schritte; 2 weitere Aktionen ausgelassen). Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

- **1.** Auslösertyp nicht erhalten: `sensor.example_18`; von Zustand: nicht erhalten, nicht erhalten; zu Zustand: nicht erhalten; Dauer nicht erhalten

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Bedingungstyp nicht erhalten: `switch.example_15`; Zustand: nicht erhalten; Dauer nicht erhalten; Bedingungstyp nicht erhalten: `script.example_01`; Zustand: nicht erhalten; Bedingungstyp nicht erhalten: `automation.example_06`; unter 1; Attributname: nicht erhalten.

## Konkreter Ablauf

1. Wenn alle folgenden: Bedingungstyp nicht erhalten: verschachtelte Prüfungen; Verknüpfung nicht erhalten [Bedingungstyp nicht erhalten: `sensor.example_19`; über -0.001; unter 8]:

   **Dann:**

   1. Auf einen dieser Auslöser warten:

      - Auslösertyp nicht erhalten: `sensor.example_19`; unter 8
      - Auslösertyp nicht erhalten: `sensor.example_18`; zu Zustand: nicht erhalten
      - Auslösertyp nicht erhalten: `switch.example_15`; zu Zustand: nicht erhalten

      Zeitgrenze: nicht erhalten. Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

2. Prüfen: Bedingungstyp nicht erhalten: verschachtelte Prüfungen; Verknüpfung nicht erhalten [Bedingungstyp nicht erhalten: `switch.example_15`; Zustand: nicht erhalten; Dauer nicht erhalten; Bedingungstyp nicht erhalten: `script.example_01`; Zustand: nicht erhalten; Bedingungstyp nicht erhalten: `sensor.example_18`; Zustand: nicht erhalten; Dauer nicht erhalten; Bedingungstyp nicht erhalten: `automation.example_06`; unter 1; Attributname: nicht erhalten; Bedingungstyp nicht erhalten: `sensor.example_19`; über -0.001; unter 8]. Falls falsch, den aktuellen Ablauf hier stoppen.

3. Auf einen dieser Auslöser warten:

   - Auslösertyp nicht erhalten: `sensor.example_19`; über 7.999
   - Auslösertyp nicht erhalten: `sensor.example_19`; zu Zustand: nicht erhalten, nicht erhalten
   - Auslösertyp nicht erhalten: `sensor.example_18`; von Zustand: nicht erhalten
   - Auslösertyp nicht erhalten: `switch.example_15`; von Zustand: nicht erhalten
   - Auslösertyp nicht erhalten: `script.example_01`; zu Zustand: nicht erhalten
   - Auslösertyp nicht erhalten: `automation.example_06`; über 0; Attributname: nicht erhalten

   Zeitgrenze: nicht erhalten. Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

4. Wenn alle folgenden: Bedingungstyp nicht erhalten: `switch.example_15`; Zustand: nicht erhalten; Dauer nicht erhalten; Bedingungstyp nicht erhalten: `script.example_01`; Zustand: nicht erhalten; Bedingungstyp nicht erhalten: `sensor.example_18`; Zustand: nicht erhalten; Dauer nicht erhalten; Bedingungstyp nicht erhalten: `automation.example_06`; unter 1; Attributname: nicht erhalten; Bedingungstyp nicht erhalten: `sensor.example_19`; über -0.001; unter 8; Bedingungstyp nicht erhalten: Formel: nicht erhalten; Bedingungstyp nicht erhalten: Formel: nicht erhalten:

   **Dann:**

   1. Einen Schalter ausschalten — `switch.example_15`.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Einen Schalter oder eine schaltbare Steckdose in Home Assistant.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
