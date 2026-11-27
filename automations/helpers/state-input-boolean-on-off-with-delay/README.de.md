# Gespeicherte Ein/Aus-Werte ändern · mit Wartezeit im Ablauf

[English](README.md) · **Deutsch**

[Zähler und gespeicherte Werte](../../../README.de.md#helpers) → [Virtuelle Schalter](../../../README.de.md#helpers-switches)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Einen gespeicherten Ein/Aus-Wert einschalten → warten für 180 s → Einen gespeicherten Ein/Aus-Wert ausschalten (ausgewählte Schritte; 1 weitere Aktion ausgelassen). Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Auslösertyp nicht erhalten: `binary_sensor.example_17`; von Zustand: nicht erhalten; zu Zustand: nicht erhalten; Auslöser-Verweis: `ID_06`
- **2.** Auslösertyp nicht erhalten: `event.example_05`; zu Zustand: ohne Wert (null); Auslöser-Verweis: `ID_07`
- **3.** Auslösertyp nicht erhalten: `input_boolean.example_03`, `input_boolean.example_04`; von Zustand: nicht erhalten; zu Zustand: nicht erhalten; Auslöser-Verweis: `ID_08`

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten.

## Konkreter Ablauf

1. Einen gespeicherten Ein/Aus-Wert einschalten — `input_boolean.example_03`, `input_boolean.example_04`.

2. Wenn alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten:

   **Dann:**

   1. Eine Gerätefunktion per Tastendruck auslösen — `button.example_01`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

3. Warten für 180 s.

4. Einen gespeicherten Ein/Aus-Wert ausschalten — `input_boolean.example_03`, `input_boolean.example_04`.

## Wenn sie erneut ausgelöst wird

`restart`: Ein neuer Auslöser stoppt den laufenden Durchlauf und startet neu, sofern die Bedingungen der Automation erfüllt sind.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Eine Gerätefunktion, die Home Assistant als Taste bereitstellt.
- Einen Ein/Aus-Helfer: ein gespeicherter Schalterwert in Home Assistant.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
