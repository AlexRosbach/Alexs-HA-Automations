# Nachrichten senden — Variante A

[English](README.md) · **Deutsch**

[Nachrichten und Hinweise](../../../README.de.md#notifications) → [Nachrichten versenden](../../../README.de.md#notifications-messages)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Zwischenwerte vorbereiten → Eine Nachricht an ein eigenes Ziel senden; Nachrichtentext: “In folgenden Räumen sind Fenster variable\_62: \{\{ variable\_17 \}\}”; Nachrichtentitel: “🌧️ Regenalarm · \{\{ variable\_16 \}\}” → Eine Nachricht an ein eigenes Ziel senden; Nachrichtentext: “In folgenden Räumen sind Fenster variable\_62: \{\{ variable\_17 \}\}”; Nachrichtentitel: “🌧️ Regenalarm · \{\{ variable\_16 \}\}”. Starteinstellungen: zu Zustand: `on`. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Zustandsänderung: `binary_sensor.example_13`; zu Zustand: `on`
- **2.** Zustandsänderung: `binary_sensor.example_14`, `binary_sensor.example_15`, `binary_sensor.example_16`, `binary_sensor.example_17`, `binary_sensor.example_18`, `binary_sensor.example_19`, `binary_sensor.example_20`, `binary_sensor.example_21`, `binary_sensor.example_22`; zu Zustand: `on`

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Zustandsprüfung: `binary_sensor.example_13`; Zustand: `on`; Formelprüfung: Formel: “\{\{ expand\(\[ 'binary\_sensor.example\_14', 'binary\_sensor.example\_15', 'binary\_sensor.example\_16', 'binary\_sensor.example\_17', 'binary\_sensor.example\_18', 'binary\_sensor.example\_19', 'binary\_sensor.example\_20', 'binary\_sensor.example\_21', 'binary\_sensor.example\_22' \]\) \| selectattr\('state', 'eq', 'IDENTIFIER\_160'\) \| list \| count &gt; 0 \}\}”.

## Konkreter Ablauf

1. 2 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

2. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “In folgenden Räumen sind Fenster variable\_62: \{\{ variable\_17 \}\}”; Nachrichtentitel: “🌧️ Regenalarm · \{\{ variable\_16 \}\}”.

3. Eine Nachricht an ein eigenes Ziel senden — `notify.example_02`; Nachrichtentext: “In folgenden Räumen sind Fenster variable\_62: \{\{ variable\_17 \}\}”; Nachrichtentitel: “🌧️ Regenalarm · \{\{ variable\_16 \}\}”.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
