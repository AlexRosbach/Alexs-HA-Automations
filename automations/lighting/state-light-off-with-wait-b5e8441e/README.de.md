# Licht ausschalten · mit Wartebedingung im Ablauf — Variante D

[English](README.md) · **Deutsch**

[Licht](../../../README.de.md#lighting) → [Ausschalten](../../../README.de.md#lighting-off)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Auf einen von 2 Auslösern warten (bei Ablauf weiter) → Licht ausschalten (ausgewählte Schritte; 9 weitere Aktionen ausgelassen). Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

- **1.** Auslösertyp nicht erhalten: `sensor.example_16`; zu Zustand: nicht erhalten; Dauer nicht erhalten

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten; Bedingungstyp nicht erhalten: Formel: nicht erhalten.

## Konkreter Ablauf

1. Ein Datum oder eine Uhrzeit speichern — `input_datetime.example_01`; gespeicherte Zeit: nicht erhalten.

2. 2 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

3. Aktionstyp nicht erhalten; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

4. Auf einen dieser Auslöser warten:

   - Auslösertyp nicht erhalten: Ereignisname: nicht erhalten
   - Auslösertyp nicht erhalten: Ereignisname: nicht erhalten

   Zeitgrenze: nicht erhalten. Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

5. Aktionstyp nicht erhalten; Nachrichtentext: nicht erhalten.

6. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

7. Prüfen: Bedingungstyp nicht erhalten: `sensor.example_16`; Zustand: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

8. Prüfen: Bedingungstyp nicht erhalten: `binary_sensor.example_20`; Zustand: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

9. Licht ausschalten — `light.example_10`, `light.example_11`, `light.example_12`, `light.example_18`, `light.example_19`, `light.example_20`.

10. Ein eigenes Skript ausführen — `script.led_aus`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

11. Wenn alle folgenden: Bedingungstyp nicht erhalten: `switch.example_08`; Zustand: nicht erhalten:

    **Dann:**

    1. Ein eigenes Skript ausführen — `script.ausschalten`.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Einen Helfer, der ein Datum oder eine Uhrzeit speichert.
- Lampen, die Home Assistant steuern kann.
- Ein vorhandenes Home-Assistant-Skript, also eine gespeicherte Folge von Aktionen.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
