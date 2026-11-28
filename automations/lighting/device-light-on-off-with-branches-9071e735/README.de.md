# Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante C

[English](README.md) · **Deutsch**

[Licht](../../../README.de.md#lighting) → [Ein- und Ausschalten](../../../README.de.md#lighting-on-off)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Wenn die eingestellten Bedingungen erfüllt sind: (den ersten passenden Zweig ausführen: Licht mit 86 % Helligkeit einschalten; Übergang: 1 s; Farbtemperatur: 4000 K → Ein eigenes Skript ausführen / Licht ausschalten; Übergang: 2 s → Ein eigenes Skript ausführen) → den ersten passenden Zweig ausführen: Einen Lüfter einschalten / Einen Lüfter ausschalten. Starteinstellungen: Geräteereignis.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Geräteereignis: `ENTITY_33`, `DEVICE_42`; Geräteereignis/-aktion: `occupied`
- **2.** Geräteereignis: `ENTITY_33`, `DEVICE_42`; Geräteereignis/-aktion: `not_occupied`

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Wenn alle folgenden: Geräteprüfung: `ENTITY_14`, `DEVICE_16`; Geräteereignis/-aktion: `is_off`:

   **Dann:**

   1. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Geräteprüfung: `ENTITY_33`, `DEVICE_42`; Geräteereignis/-aktion: nicht erhalten

      1. Licht einschalten — `light.example_10`, `light.example_11`, `light.example_12`; Helligkeit: 86%; Übergang: 1 s; Farbtemperatur: 4000 K.

      2. Ein eigenes Skript ausführen — `script.example_06`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

      **Zweig 2:** alle folgenden: Geräteprüfung: `ENTITY_33`, `DEVICE_42`; Geräteereignis/-aktion: nicht erhalten

      1. Licht ausschalten — `light.example_10`, `light.example_11`, `light.example_12`; Übergang: 2 s.

      2. Ein eigenes Skript ausführen — `script.example_07`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

      Kein Standardzweig eingestellt.

2. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Geräteprüfung: `ENTITY_33`, `DEVICE_42`; Geräteereignis/-aktion: nicht erhalten

   1. Einen Lüfter einschalten — `DEVICE_43`.

   **Zweig 2:** alle folgenden: Geräteprüfung: `ENTITY_33`, `DEVICE_42`; Geräteereignis/-aktion: nicht erhalten

   1. Einen Lüfter ausschalten — `DEVICE_43`.

   Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Einen Lüfter oder Luftreiniger, den Home Assistant steuern kann.
- Lampen, die Home Assistant steuern kann.
- Ein vorhandenes Home-Assistant-Skript, also eine gespeicherte Folge von Aktionen.
- Ein eingebundenes Gerät mit einem passenden Ereignis als Auslöser.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
