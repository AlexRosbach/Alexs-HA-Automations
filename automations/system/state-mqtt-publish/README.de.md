# Eine MQTT-Nachricht senden

[English](README.md) · **Deutsch**

[Weitere Abläufe und Geräteaktionen](../../../README.de.md#system) → [MQTT-Nachrichten](../../../README.de.md#system-mqtt)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Eine MQTT-Nachricht senden. Starteinstellungen: Zustandsänderung. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

- **1.** Zustandsänderung: `media_player.example_01`; Attributname: nicht erhalten

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: keine der folgenden [Zustandsprüfung: `media_player.example_01`; Zustand: `idle`].

## Konkreter Ablauf

1. Eine MQTT-Nachricht senden; MQTT-Thema: “awtrix\_58fb64/notify”; MQTT-Inhalt: “\{"icon": 647, "repeat": 1, "text": "\{\{states.media\_player.example\_01.attributes.media\_artist\}\} - \{\{states.media\_player.example\_01.attributes.media\_title\}\}" \}”.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Eine eingerichtete MQTT-Anbindung für den Nachrichtenaustausch zwischen Geräten.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
