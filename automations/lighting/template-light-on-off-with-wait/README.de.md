# Licht ein- und ausschalten · mit Wartebedingung im Ablauf

[English](README.md) · **Deutsch**

[Licht](../../../README.de.md#lighting) → [Ein- und Ausschalten](../../../README.de.md#lighting-on-off)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Licht einschalten → auf eine Bedingung warten → Licht ausschalten (ausgewählte Schritte; 1 weitere Aktion ausgelassen). Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

- **1.** Auslösertyp nicht erhalten: Dauer nicht erhalten; Formel: nicht erhalten

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Bedingungstyp nicht erhalten: `input_boolean.example_13`; Zustand: nicht erhalten; Bedingungstyp nicht erhalten: `input_boolean.example_02`; Zustand: nicht erhalten; Bedingungstyp nicht erhalten: `input_boolean.example_05`; Zustand: nicht erhalten.

## Konkreter Ablauf

1. Licht einschalten — `light.example_01`.

2. Warten, bis eine Formel wahr ist; die Formel ist nicht erhalten.

   Keine Zeitgrenze eingestellt.

3. Prüfen: Bedingungstyp nicht erhalten: `input_boolean.example_05`; Zustand: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

4. Licht ausschalten — `light.example_01`.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Lampen, die Home Assistant steuern kann.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
