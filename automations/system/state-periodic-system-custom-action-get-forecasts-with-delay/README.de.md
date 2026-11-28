# Mehrere Funktionen verbinden · mit Wartezeit im Ablauf

[English](README.md) · **Deutsch**

[Weitere Abläufe und Geräteaktionen](../../../README.de.md#system) → [Wetterdaten abrufen](../../../README.de.md#system-weather)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Eine Wettervorhersage abrufen → Bedingungen prüfen; bei falsch diesen Ablauf stoppen → Zwischenwerte vorbereiten → 3 weitere Schritte (siehe Ablauf). Starteinstellungen: zu Zustand: `on`; Dauer 30 s / Dauer 30 s; 1 weiterer Auslöser in den Details. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Zustandsänderung: `binary_sensor.example_13`; zu Zustand: `on`; Dauer 00:00:30 (Zeitformat)
- **2.** Zustandsänderung: `binary_sensor.example_14`, `binary_sensor.example_15`, `binary_sensor.example_16`, `binary_sensor.example_17`, `binary_sensor.example_18`, `binary_sensor.example_19`, `binary_sensor.example_20`, `binary_sensor.example_21`, `binary_sensor.example_22`; zu Zustand: `on`; Dauer 00:00:30 (Zeitformat)
- **3.** Zustandsänderung: `weather.example_01`; zu Zustand: nicht erhalten; Dauer 00:00:30 (Zeitformat)
- **4.** Wiederholter Zeitplan: Minuten: /5

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Formelprüfung: Formel: “\{\{ 6 &lt;= now\(\).hour &lt; 21 \}\}”; Zustandsprüfung: `binary_sensor.example_13`; Zustand: `on`; Dauer 00:00:30 (Zeitformat); Formelprüfung: Formel: “\{\{ expand\(\["binary\_sensor.example\_14","binary\_sensor.example\_15","binary\_sensor.example\_16","binary\_sensor.example\_17","binary\_sensor.example\_18","binary\_sensor.example\_19","binary\_sensor.example\_20","binary\_sensor.example\_21","binary\_sensor.example\_22"\]\) \| selectattr\('state', 'eq', 'IDENTIFIER\_160'\) \| list \| count &gt; 0 \}\}”.

## Konkreter Ablauf

1. Eine Wettervorhersage abrufen — `weather.example_01`; Rückgabe für spätere Schritte speichern.

2. Prüfen: Formelprüfung: Formel: “\{% set prognose = variable\_54.get\('weather.example\_01', \{\}\).get\('forecast', \[\]\) %\} \{\{ is\_state\('weather.example\_01', 'pouring'\) or \(prognose \| count &gt; 0 and prognose\[0\].get\('condition'\) == 'pouring'\) \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

3. 2 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

4. Prüfen: Formelprüfung: Formel: “\{\{ variable\_56 \| count &gt; 0 \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

5. Ein eigenes Skript ausführen — `script.example_10`.

6. Warten für 00:30:00 (Zeitformat).

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein vorhandenes Home-Assistant-Skript, also eine gespeicherte Folge von Aktionen.
- Eine Wetteranbindung, die Vorhersagen bereitstellt.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
