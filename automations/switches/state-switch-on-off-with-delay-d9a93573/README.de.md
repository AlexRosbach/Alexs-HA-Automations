# Schalter ein- und ausschalten · mit Wartezeit im Ablauf — Variante B

[English](README.md) · **Deutsch**

[Schalter und Steckdosen](../../../README.de.md#switches) → [Ein- und Ausschalten](../../../README.de.md#switches-on-off)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Den ersten passenden Zweig ausführen: Einen Schalter einschalten → warten für 3 min → 2 weitere Schritte / Bedingungen prüfen; bei falsch diesen Ablauf stoppen → Einen Schalter ausschalten. Starteinstellungen: Dauer 5 min.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Auslösertyp nicht erhalten: `binary_sensor.example_04`; zu Zustand: nicht erhalten
- **2.** Auslösertyp nicht erhalten: `binary_sensor.example_04`; zu Zustand: nicht erhalten; Dauer 5 min

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: `binary_sensor.example_04`; Zustand: nicht erhalten

   1. Einen Schalter einschalten — `DEVICE_22`.

   2. Warten für 3 min.

   3. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   4. Einen Schalter ausschalten — `switch.example_03`.

   **Zweig 2:** alle folgenden: Bedingungstyp nicht erhalten: `binary_sensor.example_04`; Zustand: nicht erhalten

   1. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   2. Einen Schalter ausschalten — `DEVICE_22`.

   Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`restart`: Ein neuer Auslöser stoppt den laufenden Durchlauf und startet neu, sofern die Bedingungen der Automation erfüllt sind.

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
