# Gespeicherte Ein/Aus-Werte ändern · mit Bedingungen im Ablauf

[English](README.md) · **Deutsch**

[Zähler und gespeicherte Werte](../../../README.de.md#helpers) → [Virtuelle Schalter](../../../README.de.md#helpers-switches)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Den ersten passenden Zweig ausführen: Einen gespeicherten Ein/Aus-Wert einschalten / Einen gespeicherten Ein/Aus-Wert ausschalten. Starteinstellungen: von Zustand: `off`; zu Zustand: `on` / von Zustand: `on`; zu Zustand: `off`; 1 weiterer Auslöser in den Details.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Zustandsänderung: `switch.example_14`; von Zustand: `off`; zu Zustand: `on`; Auslöser-Verweis: nicht erhalten
- **2.** Zustandsänderung: `switch.example_14`; von Zustand: `on`; zu Zustand: `off`; Auslöser-Verweis: nicht erhalten
- **3.** Feste Uhrzeit: um 12:00:00; Auslöser-Verweis: nicht erhalten

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Auslöser-Verweis prüfen: Auslöser-Verweis: nicht erhalten; Formelprüfung: Formel: “\{\{ trigger.to\_state.context.parent\_id is none \}\}”

   1. Einen gespeicherten Ein/Aus-Wert einschalten — `input_boolean.example_12`.

   **Zweig 2:** alle folgenden: Auslöser-Verweis prüfen: Auslöser-Verweis: nicht erhalten

   1. Einen gespeicherten Ein/Aus-Wert ausschalten — `input_boolean.example_12`.

   Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`queued`: Neue Durchläufe warten in einer Warteschlange und laufen in Eingangsreihenfolge. Sie werden nur eingereiht, wenn die Bedingungen beim Auslösen erfüllt sind. Grenze für laufende und wartende Durchläufe: 10.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Einen Ein/Aus-Helfer: ein gespeicherter Schalterwert in Home Assistant.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
