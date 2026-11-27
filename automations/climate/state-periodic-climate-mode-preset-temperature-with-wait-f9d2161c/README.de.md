# Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante E

[English](README.md) · **Deutsch**

[Heizung und Raumklima](../../../README.de.md#climate) → [Heiz- und Klimaprofile](../../../README.de.md#climate-profiles)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Den ersten passenden Zweig ausführen: wenn die eingestellten Bedingungen erfüllt sind: (Einen Textwert speichern) → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen) → 2 weitere Schritte / Den Heiz- oder Kühlbetrieb einstellen → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen) → 3 weitere Schritte (ausgewählte Schritte; 4 weitere Aktionen ausgelassen).

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Auslösertyp nicht erhalten: `binary_sensor.example_07`; zu Zustand: nicht erhalten, nicht erhalten
- **2.** Auslösertyp nicht erhalten: `climate.example_04`; Dauer nicht erhalten; Attributname: nicht erhalten
- **3.** Auslösertyp nicht erhalten: `climate.example_04`; Dauer nicht erhalten; Attributname: nicht erhalten
- **4.** Auslösertyp nicht erhalten: `climate.example_04`; zu Zustand: nicht erhalten, nicht erhalten; Dauer nicht erhalten
- **5.** Auslösertyp nicht erhalten: Ereignis: nicht erhalten
- **6.** Auslösertyp nicht erhalten: Minuten: nicht erhalten

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. 3 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

2. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

3. 3 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

4. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

5. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

   1. Wenn alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten:

      **Dann:**

      1. Einen Textwert speichern — `input_text.example_04`; gespeicherter Wert: nicht erhalten.

   2. Wenn alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten:

      **Dann:**

      1. Ein Heiz- oder Klimaprofil auswählen — `climate.example_04`; Profil: nicht erhalten.

   3. Wenn alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten:

      **Dann:**

      1. Den Heiz- oder Kühlbetrieb einstellen — `climate.example_04`; Heiz-/Kühlmodus: nicht erhalten.

   4. Wenn alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten:

      **Dann:**

      1. Die gewünschte Raumtemperatur einstellen — `climate.example_04`; Temperaturwert (Einheit nicht angegeben): 5.

   **Zweig 2:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

   1. Den Heiz- oder Kühlbetrieb einstellen — `climate.example_04`; Heiz-/Kühlmodus: nicht erhalten.

   2. Wenn alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten:

      **Dann:**

      1. Ein Heiz- oder Klimaprofil auswählen — `climate.example_04`; Profil: nicht erhalten.

   3. Die gewünschte Raumtemperatur einstellen — `climate.example_04`; Temperaturwert (Einheit nicht angegeben): nicht erhalten.

   4. Warten, bis eine Formel wahr ist; die Formel ist nicht erhalten.

      Zeitgrenze: nicht erhalten. Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.

   5. Einen Textwert speichern — `input_text.example_04`; gespeicherter Wert: nicht erhalten.

   Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`queued`: Neue Durchläufe warten in einer Warteschlange und laufen in Eingangsreihenfolge. Sie werden nur eingereiht, wenn die Bedingungen beim Auslösen erfüllt sind. Grenze für laufende und wartende Durchläufe: 10.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein eingebundenes Thermostat oder eine Klimaanlage.
- Einen Helfer, der einen Textwert speichert.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
