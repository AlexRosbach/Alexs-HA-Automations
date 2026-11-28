# Nachrichten senden — Variante B

[English](README.md) · **Deutsch**

[Nachrichten und Hinweise](../../../README.de.md#notifications) → [Nachrichten versenden](../../../README.de.md#notifications-messages)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Einen Zähler zurücksetzen → Ein eigenes Skript ausführen → Eine Nachricht senden; Nachrichtentext: “Windelzähler wurde zurückgesetzt. Ein To‑Do person Leeren des Windeleimers wurde erstellt.”; Nachrichtentitel: “Windelzähler”. Starteinstellungen: Geräteereignis.

## Wann startet sie?

- **1.** Geräteereignis: `DEVICE_01`; Geräteereignis/-aktion: nicht erhalten

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Einen Zähler zurücksetzen — `counter.example_01`.

2. Ein eigenes Skript ausführen — `script.example_01`.

3. Eine Nachricht senden; Nachrichtentext: “Windelzähler wurde zurückgesetzt. Ein To‑Do person Leeren des Windeleimers wurde erstellt.”; Nachrichtentitel: “Windelzähler”.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Einen Zähler-Helfer in Home Assistant.
- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Ein vorhandenes Home-Assistant-Skript, also eine gespeicherte Folge von Aktionen.
- Ein eingebundenes Gerät mit einem passenden Ereignis als Auslöser.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
