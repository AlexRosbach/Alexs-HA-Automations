# Die gewünschte Raumtemperatur einstellen · mit Wartebedingung im Ablauf — Variante C

[English](README.md) · **Deutsch**

[Heizung und Raumklima](../../../README.de.md#climate) → [Temperatur einstellen](../../../README.de.md#climate-temperature)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Zwischenwerte vorbereiten → den ersten passenden Zweig ausführen: Zwischenwerte vorbereiten → Einen Textwert speichern → 7 weitere Schritte / Zwischenwerte vorbereiten → Bedingungen prüfen; bei falsch diesen Ablauf stoppen → 6 weitere Schritte; 4 weitere Zweige. Starteinstellungen: von Zustand: `off`; zu Zustand: `on` / zu Zustand: `on`; Dauer 2 min; 4 weitere Auslöser in den Details. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Zustandsänderung: `binary_sensor.example_34`, `binary_sensor.example_28`, `binary_sensor.example_35`; von Zustand: `off`; zu Zustand: `on`; Auslöser-Verweis: nicht erhalten
- **2.** Zustandsänderung: `binary_sensor.example_34`, `binary_sensor.example_28`, `binary_sensor.example_35`; zu Zustand: `on`; Dauer 00:02:00 (Zeitformat); Auslöser-Verweis: nicht erhalten
- **3.** Formel wird wahr: Dauer 00:30:00 (Zeitformat); Formel: “\{\{ \['binary\_sensor.example\_34', 'binary\_sensor.example\_28', 'binary\_sensor.example\_35'\] \| select\('is\_state','IDENTIFIER\_159'\) \| list \| count == 3 \}\}”; Auslöser-Verweis: nicht erhalten
- **4.** Feste Uhrzeit: um 08:00:00; Auslöser-Verweis: nicht erhalten
- **5.** Feste Uhrzeit: um 18:00:00; Auslöser-Verweis: nicht erhalten
- **6.** Zustandsänderung: `climate.example_01`; Auslöser-Verweis: nicht erhalten
- **7.** Zustandsänderung: `binary_sensor.example_22`; Auslöser-Verweis: nicht erhalten

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Formelprüfung: Formel: “\{\{ states\('input\_text.example\_13'\) not in \['unknown','unavailable'\] \}\}”.

## Konkreter Ablauf

Die Automation bereitet außerdem Zwischenwerte vor; ihre Inhalte/Formeln sind nicht beschrieben.

1. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

2. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Formelprüfung: Formel: “\{\{ trigger.id == 'IDENTIFIER\_164' \}\}”

   1. 2 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   2. Einen Textwert speichern — `input_text.example_13`; gespeicherter Wert: “\{\{ \{'e':variable\_66,'d':variable\_65.get\('d',''\)\}\|to\_json \}\}”.

   3. Prüfen: Formelprüfung: Formel: “\{\{ variable\_66\|count &gt;= 4 and as\_timestamp\(now\(\)\) - \(variable\_66\[-1\]\|float\) &lt;= 600 \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   4. Prüfen: Formelprüfung: Formel: “\{\{ \['binary\_sensor.example\_22'\] \| select\('is\_state','IDENTIFIER\_159'\) \| list \| count == 1 \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   5. Prüfen: Formelprüfung: Formel: “\{\{ states\(thermostat\) in \['heat','auto'\] and state\_attr\(thermostat,'temperature'\) is number \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   6. Prüfen: Formelprüfung: Formel: “\{\{ states\(thermostat\) \!= 'heat' or state\_attr\(thermostat,'temperature'\) \!= 21 \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   7. Die gewünschte Raumtemperatur einstellen — `climate.example_01`; Temperaturwert (Einheit nicht angegeben): 21; Heiz-/Kühlmodus: `heat`.

   8. Warten, bis diese Formel wahr ist: “\{\{ is\_state\(thermostat,'heat'\) and state\_attr\(thermostat,'temperature'\) == 21 \}\}”.

      Zeitgrenze: 00:00:20 (Zeitformat). Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.

   9. Einen Textwert speichern — `input_text.example_13`; gespeicherter Wert: “\{\{ \{'e':variable\_66,'d':''\}\|to\_json \}\}”.

   **Zweig 2:** alle folgenden: Formelprüfung: Formel: “\{\{ trigger.id == 'IDENTIFIER\_165' \}\}”

   1. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   2. Prüfen: Formelprüfung: Formel: “\{\{ is\_state\(trigger.entity\_id,'IDENTIFIER\_160'\) and as\_timestamp\(states\[trigger.entity\_id\].last\_changed\) &lt;= as\_timestamp\(now\(\)\) - 120 \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   3. Prüfen: Formelprüfung: Formel: “\{\{ \['binary\_sensor.example\_22'\] \| select\('is\_state','IDENTIFIER\_159'\) \| list \| count == 1 \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   4. Prüfen: Formelprüfung: Formel: “\{\{ states\(thermostat\) in \['heat','auto'\] and state\_attr\(thermostat,'temperature'\) is number \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   5. Prüfen: Formelprüfung: Formel: “\{\{ states\(thermostat\) \!= 'heat' or state\_attr\(thermostat,'temperature'\) \!= 21 \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   6. Die gewünschte Raumtemperatur einstellen — `climate.example_01`; Temperaturwert (Einheit nicht angegeben): 21; Heiz-/Kühlmodus: `heat`.

   7. Warten, bis diese Formel wahr ist: “\{\{ is\_state\(thermostat,'heat'\) and state\_attr\(thermostat,'temperature'\) == 21 \}\}”.

      Zeitgrenze: 00:00:20 (Zeitformat). Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.

   8. Einen Textwert speichern — `input_text.example_13`; gespeicherter Wert: “\{\{ \{'e':variable\_66,'d':''\}\|to\_json \}\}”.

   **Zweig 3:** alle folgenden: Formelprüfung: Formel: “\{\{ trigger.id in \['IDENTIFIER\_166','IDENTIFIER\_167'\] \}\}”

   1. Prüfen: Formelprüfung: Formel: “\{\{ 8 &lt;= now\(\).hour &lt; 18 \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   2. Prüfen: Formelprüfung: Formel: “\{\{ \['binary\_sensor.example\_34', 'binary\_sensor.example\_28', 'binary\_sensor.example\_35'\] \| select\('is\_state','IDENTIFIER\_159'\) \| list \| count == 3 \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   3. Prüfen: Formelprüfung: Formel: “\{\{ \['binary\_sensor.example\_34', 'binary\_sensor.example\_28', 'binary\_sensor.example\_35'\] \| expand \| map\(attribute='last\_changed'\) \| map\('as\_timestamp'\) \| max &lt;= as\_timestamp\(now\(\)\) - 1800 \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   4. Prüfen: Formelprüfung: Formel: “\{\{ \['binary\_sensor.example\_22'\] \| select\('is\_state','IDENTIFIER\_159'\) \| list \| count == 1 \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   5. Prüfen: Formelprüfung: Formel: “\{\{ states\(thermostat\) in \['heat','auto'\] and state\_attr\(thermostat,'temperature'\) is number \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   6. Prüfen: Formelprüfung: Formel: “\{\{ state\_attr\(thermostat,'temperature'\) &gt; 19 \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   7. Die gewünschte Raumtemperatur einstellen — `climate.example_01`; Temperaturwert (Einheit nicht angegeben): 19; Heiz-/Kühlmodus: `heat`.

   8. Warten, bis diese Formel wahr ist: “\{\{ is\_state\(thermostat,'heat'\) and state\_attr\(thermostat,'temperature'\) == 19 \}\}”.

      Zeitgrenze: 00:00:20 (Zeitformat). Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.

   9. Einen Textwert speichern — `input_text.example_13`; gespeicherter Wert: “\{\{ \{'e':\[\],'d':day\}\|to\_json \}\}”.

   **Zweig 4:** alle folgenden: Formelprüfung: Formel: “\{\{ trigger.id == 'IDENTIFIER\_168' \}\}”

   1. Prüfen: Formelprüfung: Formel: “\{\{ variable\_65.get\('d'\) == day and is\_state\(thermostat,'heat'\) and state\_attr\(thermostat,'temperature'\) == 19 \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   2. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   3. Prüfen: Formelprüfung: Formel: “\{\{ \['binary\_sensor.example\_22'\] \| select\('is\_state','IDENTIFIER\_159'\) \| list \| count == 1 \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   4. Prüfen: Formelprüfung: Formel: “\{\{ states\(thermostat\) in \['heat','auto'\] and state\_attr\(thermostat,'temperature'\) is number \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   5. Prüfen: Formelprüfung: Formel: “\{\{ states\(thermostat\) \!= 'heat' or state\_attr\(thermostat,'temperature'\) \!= 21 \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   6. Die gewünschte Raumtemperatur einstellen — `climate.example_01`; Temperaturwert (Einheit nicht angegeben): 21; Heiz-/Kühlmodus: `heat`.

   7. Warten, bis diese Formel wahr ist: “\{\{ is\_state\(thermostat,'heat'\) and state\_attr\(thermostat,'temperature'\) == 21 \}\}”.

      Zeitgrenze: 00:00:20 (Zeitformat). Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.

   8. Einen Textwert speichern — `input_text.example_13`; gespeicherter Wert: “\{\{ \{'e':variable\_66,'d':''\}\|to\_json \}\}”.

   **Zweig 5:** alle folgenden: Formelprüfung: Formel: “\{\{ trigger.id == 'IDENTIFIER\_169' \}\}”; Formelprüfung: Formel: “\{\{ variable\_65.get\('d'\) and \(states\(thermostat\) \!= 'heat' or state\_attr\(thermostat,'temperature'\) \!= 19 or state\_attr\(thermostat,'preset\_mode'\) == 'boost'\) \}\}”

   1. Einen Textwert speichern — `input_text.example_13`; gespeicherter Wert: “\{\{ \{'e':variable\_65.get\('e',\[\]\),'d':''\}\|to\_json \}\}”.

   **Zweig 6:** alle folgenden: Formelprüfung: Formel: “\{\{ trigger.id == 'IDENTIFIER\_170' \}\}”; Formelprüfung: Formel: “\{% set safe = \['binary\_sensor.example\_22'\] \| select\('is\_state','IDENTIFIER\_159'\) \| list \| count == 1 %\}\{\{ not safe \}\}”

   1. Einen Textwert speichern — `input_text.example_13`; gespeicherter Wert: “\{\{ \{'e':\[\],'d':''\}\|to\_json \}\}”.

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
