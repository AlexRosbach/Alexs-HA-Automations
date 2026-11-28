# Nachrichten senden

[English](README.md) · **Deutsch**

[Nachrichten und Hinweise](../../../README.de.md#notifications) → [Nachrichten versenden](../../../README.de.md#notifications-messages)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Einen Textwert speichern → Eine Nachricht an ein eigenes Ziel senden; Nachrichtentext: “Bitte die Restmülltonne person. Über die Aktion kannst du bestätigen.”; Nachrichtentitel: “Restmüll morgen” → Eine Nachricht an ein eigenes Ziel senden; Nachrichtentext: “Bitte die Restmülltonne person. Über die Aktion kannst du bestätigen.”; Nachrichtentitel: “Restmüll morgen”. Starteinstellungen: um 20:00:00 / zu Zustand: `on`. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Feste Uhrzeit: um 20:00:00
- **2.** Zustandsänderung: `binary_sensor.example_32`; zu Zustand: `on`

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Zustandsprüfung: `binary_sensor.example_32`; Zustand: `on`; Zeitprüfung: vor 23:59:59; nach 19:59:59; Formelprüfung: Formel: “\{\{ states\('input\_text.example\_05'\) \!= states\('input\_text.example\_06'\) \}\}”.

## Konkreter Ablauf

1. Einen Textwert speichern — `input_text.example_05`; gespeicherter Wert: “\{\{ states\('input\_text.example\_06'\) \}\}”.

2. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Bitte die Restmülltonne person. Über die Aktion kannst du bestätigen.”; Nachrichtentitel: “Restmüll morgen”.

3. Eine Nachricht an ein eigenes Ziel senden — `notify.example_02`; Nachrichtentext: “Bitte die Restmülltonne person. Über die Aktion kannst du bestätigen.”; Nachrichtentitel: “Restmüll morgen”.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Die Geräte und die Aktion, die du selbst ergänzen möchtest.
- Einen Helfer, der einen Textwert speichert.
- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
