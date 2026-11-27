# Die gewünschte Raumtemperatur einstellen · mit Wartebedingung im Ablauf — Variante A

[English](README.md) · **Deutsch**

[Heizung und Raumklima](../../../README.de.md#climate) → [Temperatur einstellen](../../../README.de.md#climate-temperature)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Zwischenwerte vorbereiten → den ersten passenden Zweig ausführen: Zwischenwerte vorbereiten → Einen Textwert speichern → 7 weitere Schritte / Zwischenwerte vorbereiten → Bedingungen prüfen; bei falsch diesen Ablauf stoppen → 6 weitere Schritte; 4 weitere Zweige. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Auslösertyp nicht erhalten: `binary_sensor.example_27`, `binary_sensor.example_21`, `binary_sensor.example_28`; von Zustand: nicht erhalten; zu Zustand: nicht erhalten; Auslöser-Verweis: `ID_32`
- **2.** Auslösertyp nicht erhalten: `binary_sensor.example_27`, `binary_sensor.example_21`, `binary_sensor.example_28`; zu Zustand: nicht erhalten; Dauer nicht erhalten; Auslöser-Verweis: `ID_33`
- **3.** Auslösertyp nicht erhalten: Dauer nicht erhalten; Formel: nicht erhalten; Auslöser-Verweis: `ID_34`
- **4.** Auslösertyp nicht erhalten: um nicht erhalten; Auslöser-Verweis: `ID_35`
- **5.** Auslösertyp nicht erhalten: um nicht erhalten; Auslöser-Verweis: `ID_36`
- **6.** Auslösertyp nicht erhalten: `climate.example_01`; Auslöser-Verweis: `ID_37`
- **7.** Auslösertyp nicht erhalten: `binary_sensor.example_14`; Auslöser-Verweis: `ID_38`

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten.

## Konkreter Ablauf

Die Automation bereitet außerdem Zwischenwerte vor; ihre Inhalte/Formeln sind nicht beschrieben.

1. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

2. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

   1. 2 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   2. Einen Textwert speichern — `input_text.example_12`; gespeicherter Wert: nicht erhalten.

   3. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   4. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   5. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   6. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   7. Die gewünschte Raumtemperatur einstellen — `climate.example_01`; Temperaturwert (Einheit nicht angegeben): 21; Heiz-/Kühlmodus: nicht erhalten.

   8. Warten, bis eine Formel wahr ist; die Formel ist nicht erhalten.

      Zeitgrenze: nicht erhalten. Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.

   9. Einen Textwert speichern — `input_text.example_12`; gespeicherter Wert: nicht erhalten.

   **Zweig 2:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

   1. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   2. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   3. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   4. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   5. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   6. Die gewünschte Raumtemperatur einstellen — `climate.example_01`; Temperaturwert (Einheit nicht angegeben): 21; Heiz-/Kühlmodus: nicht erhalten.

   7. Warten, bis eine Formel wahr ist; die Formel ist nicht erhalten.

      Zeitgrenze: nicht erhalten. Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.

   8. Einen Textwert speichern — `input_text.example_12`; gespeicherter Wert: nicht erhalten.

   **Zweig 3:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

   1. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   2. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   3. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   4. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   5. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   6. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   7. Die gewünschte Raumtemperatur einstellen — `climate.example_01`; Temperaturwert (Einheit nicht angegeben): 19; Heiz-/Kühlmodus: nicht erhalten.

   8. Warten, bis eine Formel wahr ist; die Formel ist nicht erhalten.

      Zeitgrenze: nicht erhalten. Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.

   9. Einen Textwert speichern — `input_text.example_12`; gespeicherter Wert: nicht erhalten.

   **Zweig 4:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

   1. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   2. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   3. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   4. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   5. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

   6. Die gewünschte Raumtemperatur einstellen — `climate.example_01`; Temperaturwert (Einheit nicht angegeben): 21; Heiz-/Kühlmodus: nicht erhalten.

   7. Warten, bis eine Formel wahr ist; die Formel ist nicht erhalten.

      Zeitgrenze: nicht erhalten. Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.

   8. Einen Textwert speichern — `input_text.example_12`; gespeicherter Wert: nicht erhalten.

   **Zweig 5:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten; Bedingungstyp nicht erhalten: Formel: nicht erhalten

   1. Einen Textwert speichern — `input_text.example_12`; gespeicherter Wert: nicht erhalten.

   **Zweig 6:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten; Bedingungstyp nicht erhalten: Formel: nicht erhalten

   1. Einen Textwert speichern — `input_text.example_12`; gespeicherter Wert: nicht erhalten.

   Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`queued`: Neue Durchläufe warten in einer Warteschlange und laufen in Eingangsreihenfolge. Sie werden nur eingereiht, wenn die Bedingungen beim Auslösen erfüllt sind. Grenze für laufende und wartende Durchläufe: 50.

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
