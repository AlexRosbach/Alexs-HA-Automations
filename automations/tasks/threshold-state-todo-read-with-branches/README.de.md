# Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf

[English](README.md) · **Deutsch**

[Aufgabenlisten und Erinnerungen](../../../README.de.md#tasks) → [Aufgabenlisten abfragen](../../../README.de.md#tasks-read)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Den ersten passenden Zweig ausführen: Einen gespeicherten Ein/Aus-Wert einschalten / Einen gespeicherten Ein/Aus-Wert ausschalten → Aktionstyp nicht erhalten → 4 weitere Schritte. Starteinstellungen: über 10; Dauer 2 min / unter 5; Dauer 20 min; 1 weiterer Auslöser in den Details.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Auslösertyp nicht erhalten: `sensor.example_01`; über 10; Dauer 2 min; Auslöser-Verweis: `ID_13`
- **2.** Auslösertyp nicht erhalten: `sensor.example_01`; unter 5; Dauer 20 min; Auslöser-Verweis: `ID_14`
- **3.** Auslösertyp nicht erhalten: `switch.example_13`; zu Zustand: nicht erhalten; Dauer 1 min; Auslöser-Verweis: `ID_15`

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Auslöser-Verweis: `ID_13`

   1. Einen gespeicherten Ein/Aus-Wert einschalten — `input_boolean.example_10`.

   **Zweig 2:** alle folgenden: Bedingungstyp nicht erhalten: Auslöser-Verweis: `ID_14`, `ID_15`; Bedingungstyp nicht erhalten: `input_boolean.example_10`; Zustand: nicht erhalten

   1. Einen gespeicherten Ein/Aus-Wert ausschalten — `input_boolean.example_10`.

   2. Aktionstyp nicht erhalten; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

   3. Eine Nachricht an ein eigenes Ziel senden — `notify.example_04`; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

   4. Eine Aufgabenliste abfragen — `todo.example_01`; Aufgabenstatus: nicht erhalten; Rückgabe für spätere Schritte speichern.

   5. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   6. Wenn alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten:

      **Dann:**

      1. Ein eigenes Skript ausführen — `script.todo`.

   Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Einen Ein/Aus-Helfer: ein gespeicherter Schalterwert in Home Assistant.
- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Ein vorhandenes Home-Assistant-Skript, also eine gespeicherte Folge von Aktionen.
- Eine in Home Assistant eingerichtete Aufgabenliste.
- Einen passenden Sensor oder anderen Zahlenwert in Home Assistant und die gewünschte Messwertgrenze.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
