# Licht ein- und ausschalten · mit Bedingungen im Ablauf

[English](README.md) · **Deutsch**

[Licht](../../../README.de.md#lighting) → [Ein- und Ausschalten](../../../README.de.md#lighting-on-off)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Den ersten passenden Zweig ausführen: Licht mit 76 % Helligkeit einschalten → Ein eigenes Skript ausführen → 2 weitere Schritte / wenn Zustand: `on`: (Ein vorhandenes Skript starten) → Ein eigenes Skript ausführen → 2 weitere Schritte. Starteinstellungen: MQTT-Nachricht.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** MQTT-Nachricht: MQTT-Thema: nicht erhalten; MQTT-Inhalt: nicht erhalten; Auslöser-Verweis: nicht erhalten
- **2.** MQTT-Nachricht: MQTT-Thema: nicht erhalten; MQTT-Inhalt: nicht erhalten; Auslöser-Verweis: nicht erhalten

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Auslöser-Verweis prüfen: Auslöser-Verweis: nicht erhalten

   1. Licht einschalten — `light.example_10`, `light.example_11`, `light.example_12`; Helligkeit: 76%.

   2. Ein eigenes Skript ausführen — `script.example_06`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

   3. Einen Schalter einschalten — `switch.example_08`.

   4. Ein vorhandenes Skript starten — `script.example_04`.

   **Zweig 2:** alle folgenden: Auslöser-Verweis prüfen: Auslöser-Verweis: nicht erhalten

   1. Wenn alle folgenden: Zustandsprüfung: `switch.example_15`; Zustand: `on`:

      **Dann:**

      1. Ein vorhandenes Skript starten — `script.example_05`.

   2. Ein eigenes Skript ausführen — `script.example_07`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

   3. Licht ausschalten — `light.example_10`, `light.example_11`, `light.example_12`.

   4. Wenn alle folgenden: Zustandsprüfung: `switch.example_08`; Zustand: `on`:

      **Dann:**

      1. Ein eigenes Skript ausführen — `script.example_08`.

   Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Lampen, die Home Assistant steuern kann.
- Ein vorhandenes Home-Assistant-Skript, also eine gespeicherte Folge von Aktionen.
- Einen Schalter oder eine schaltbare Steckdose in Home Assistant.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
