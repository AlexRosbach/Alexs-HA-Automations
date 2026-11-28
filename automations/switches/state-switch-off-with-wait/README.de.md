# Einen Schalter ausschalten · mit Wartebedingung im Ablauf

[English](README.md) · **Deutsch**

[Schalter und Steckdosen](../../../README.de.md#switches) → [Ausschalten](../../../README.de.md#switches-off)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Warten auf einen Wert über 7.999 oder 5 weitere Auslöser (bis zu 1 min; bei Ablauf weiter) → wenn Zustand: `on`; Dauer 3 min; 6 weitere Prüfungen: (Einen Schalter ausschalten) (ausgewählte Schritte; 2 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `unavailable`; Dauer 1 min. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

- **1.** Zustandsänderung: `sensor.example_23`; von Zustand: nicht erhalten, nicht erhalten; zu Zustand: `unavailable`; Dauer 00:01:00 (Zeitformat)

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Zustandsprüfung: `switch.example_15`; Zustand: `on`; Dauer 00:03:00 (Zeitformat); Zustandsprüfung: `script.example_04`; Zustand: `off`; Zahlenprüfung: `automation.example_06`; unter 1; Attributname: nicht erhalten.

## Konkreter Ablauf

1. Wenn alle folgenden: keine der folgenden [Zahlenprüfung: `sensor.example_24`; über -0.001; unter 8]:

   **Dann:**

   1. Auf einen dieser Auslöser warten:

      - Überschreiten oder Unterschreiten eines Zahlenwerts: `sensor.example_24`; unter 8
      - Zustandsänderung: `sensor.example_23`; zu Zustand: nicht erhalten
      - Zustandsänderung: `switch.example_15`; zu Zustand: `off`

      Zeitgrenze: 00:10:00 (Zeitformat). Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

2. Prüfen: alle folgenden [Zustandsprüfung: `switch.example_15`; Zustand: `on`; Dauer 00:03:00 (Zeitformat); Zustandsprüfung: `script.example_04`; Zustand: `off`; Zustandsprüfung: `sensor.example_23`; Zustand: `unavailable`; Dauer 00:01:00 (Zeitformat); Zahlenprüfung: `automation.example_06`; unter 1; Attributname: nicht erhalten; Zahlenprüfung: `sensor.example_24`; über -0.001; unter 8]. Falls falsch, den aktuellen Ablauf hier stoppen.

3. Auf einen dieser Auslöser warten:

   - Überschreiten oder Unterschreiten eines Zahlenwerts: `sensor.example_24`; über 7.999
   - Zustandsänderung: `sensor.example_24`; zu Zustand: `unknown`, `unavailable`
   - Zustandsänderung: `sensor.example_23`; von Zustand: `unavailable`
   - Zustandsänderung: `switch.example_15`; von Zustand: `on`
   - Zustandsänderung: `script.example_04`; zu Zustand: `on`
   - Überschreiten oder Unterschreiten eines Zahlenwerts: `automation.example_06`; über 0; Attributname: nicht erhalten

   Zeitgrenze: 00:01:00 (Zeitformat). Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

4. Wenn alle folgenden: Zustandsprüfung: `switch.example_15`; Zustand: `on`; Dauer 00:03:00 (Zeitformat); Zustandsprüfung: `script.example_04`; Zustand: `off`; Zustandsprüfung: `sensor.example_23`; Zustand: `unavailable`; Dauer 00:01:00 (Zeitformat); Zahlenprüfung: `automation.example_06`; unter 1; Attributname: nicht erhalten; Zahlenprüfung: `sensor.example_24`; über -0.001; unter 8; Formelprüfung: Formel: “\{\{ not wait.completed \}\}”; Formelprüfung: Formel: “\{\{ as\_timestamp\(now\(\)\) - as\_timestamp\(states.sensor.example\_24.last\_reported, 0\) &lt; 90 \}\}”:

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
