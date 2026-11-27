# Einen Schalter einschalten · mit Wartebedingung im Ablauf

[English](README.md) · **Deutsch**

[Schalter und Steckdosen](../../../README.de.md#switches) → [Einschalten](../../../README.de.md#switches-on)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Den ersten passenden Zweig ausführen: Einen gespeicherten Ein/Aus-Wert einschalten / Einen gespeicherten Ein/Aus-Wert ausschalten → Bedingungen prüfen; bei falsch diesen Ablauf stoppen → 4 weitere Schritte. Starteinstellungen: Dauer 8 min / Dauer 20 s.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Auslösertyp nicht erhalten: Dauer 8 min; Formel: nicht erhalten; Auslöser-Verweis: `ID_24`
- **2.** Auslösertyp nicht erhalten: `sensor.example_16`; zu Zustand: nicht erhalten; Dauer 20 s; Auslöser-Verweis: `ID_25`

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

Die Automation bereitet außerdem Zwischenwerte vor; ihre Inhalte/Formeln sind nicht beschrieben.

1. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

   1. Einen gespeicherten Ein/Aus-Wert einschalten — `input_boolean.example_11`.

   **Zweig 2:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten; Bedingungstyp nicht erhalten: Formel: nicht erhalten

   1. Einen gespeicherten Ein/Aus-Wert ausschalten — `input_boolean.example_11`.

   2. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   3. Prüfen: Bedingungstyp nicht erhalten: `switch.example_08`; Zustand: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   4. Warten, bis eine Formel wahr ist; die Formel ist nicht erhalten.

      Zeitgrenze: 30 s. Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.

   5. Eine Frage per Sprache stellen — `assist_satellite.example_01`; Ankündigungston: ja; Antwortmöglichkeiten: 2; Antworttexte nicht erhalten; Fortsetzung nach unterstützten Aktionsfehlern eingestellt; Rückgabe für spätere Schritte speichern.

   6. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

      1. Einen Schalter einschalten — `switch.example_08`.

      **Zweig 2:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

      1. Diesen Durchlauf stoppen.

      Kein Standardzweig eingestellt.

   Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein in Home Assistant eingerichtetes Sprachgerät.
- Einen Ein/Aus-Helfer: ein gespeicherter Schalterwert in Home Assistant.
- Einen Schalter oder eine schaltbare Steckdose in Home Assistant.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
