# Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante B

[English](README.md) · **Deutsch**

[Heizung und Raumklima](../../../README.de.md#climate) → [Heiz- und Klimaprofile](../../../README.de.md#climate-profiles)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Den ersten passenden Zweig ausführen: wenn die eingestellten Bedingungen erfüllt sind: (Einen Textwert speichern) → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen; Profil: “Default”) → 2 weitere Schritte / Den Heiz- oder Kühlbetrieb einstellen → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen; Profil: “\{\{ variable\_61.p \}\}”) → 3 weitere Schritte (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `on`, `off` / Dauer 10 s; 3 weitere Auslöser in den Details.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Zustandsänderung: `binary_sensor.example_20`; zu Zustand: `on`, `off`
- **2.** Zustandsänderung: `climate.example_06`; Dauer 00:00:10 (Zeitformat); Attributname: nicht erhalten
- **3.** Zustandsänderung: `climate.example_06`; Dauer 00:00:10 (Zeitformat); Attributname: nicht erhalten
- **4.** Zustandsänderung: `climate.example_06`; zu Zustand: `auto`, `heat`; Dauer 00:00:10 (Zeitformat)
- **5.** Home-Assistant-Ereignis: Ereignis: `start`
- **6.** Wiederholter Zeitplan: Minuten: /5

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. 3 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

2. Prüfen: Formelprüfung: Formel: “\{\{ states\(thermostat\) in \['auto','heat'\] and state\_attr\(thermostat,'temperature'\) is number and states\(variable\_60\) not in \['unknown','unavailable'\] \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

3. 3 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

4. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

5. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Formelprüfung: Formel: “\{\{ variable\_62 or \(variable\_64 and not variable\_63\) \}\}”

   1. Wenn alle folgenden: Formelprüfung: Formel: “\{\{ not variable\_64 \}\}”:

      **Dann:**

      1. Einen Textwert speichern — `input_text.example_10`; gespeicherter Wert: “\{\{ \{'t':state\_attr\(thermostat,'temperature'\),'m':states\(thermostat\),'p':state\_attr\(thermostat,'preset\_mode'\)\}\|to\_json \}\}”.

   2. Wenn alle folgenden: Formelprüfung: Formel: “\{\{ state\_attr\(thermostat,'preset\_mode'\) == 'boost' \}\}”:

      **Dann:**

      1. Ein Heiz- oder Klimaprofil auswählen — `climate.example_06`; Profil: “Default”.

   3. Wenn alle folgenden: Formelprüfung: Formel: “\{\{ not is\_state\(thermostat,'heat'\) \}\}”:

      **Dann:**

      1. Den Heiz- oder Kühlbetrieb einstellen — `climate.example_06`; Heiz-/Kühlmodus: `heat`.

   4. Wenn alle folgenden: Formelprüfung: Formel: “\{\{ state\_attr\(thermostat,'temperature'\) \!= 5 \}\}”:

      **Dann:**

      1. Die gewünschte Raumtemperatur einstellen — `climate.example_06`; Temperaturwert (Einheit nicht angegeben): 5.

   **Zweig 2:** alle folgenden: Formelprüfung: Formel: “\{\{ variable\_63 and variable\_64 \}\}”

   1. Den Heiz- oder Kühlbetrieb einstellen — `climate.example_06`; Heiz-/Kühlmodus: nicht erhalten.

   2. Wenn alle folgenden: Formelprüfung: Formel: “\{\{ variable\_61.get\('p'\) not in \[none,'none','unknown','unavailable'\] and variable\_61.get\('p'\) in \(state\_attr\(thermostat,'preset\_modes'\) or \[\]\) and state\_attr\(thermostat,'preset\_mode'\) \!= variable\_61.p \}\}”:

      **Dann:**

      1. Ein Heiz- oder Klimaprofil auswählen — `climate.example_06`; Profil: “\{\{ variable\_61.p \}\}”.

   3. Die gewünschte Raumtemperatur einstellen — `climate.example_06`; Temperaturwert (Einheit nicht angegeben): nicht erhalten.

   4. Warten, bis diese Formel wahr ist: “\{\{ states\(thermostat\) == variable\_61.m and state\_attr\(thermostat,'temperature'\) == variable\_61.t \}\}”.

      Zeitgrenze: 00:00:20 (Zeitformat). Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.

   5. Einen Textwert speichern — `input_text.example_10`; gespeicherter Wert: “”.

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
