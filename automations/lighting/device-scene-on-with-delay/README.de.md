# Eine gespeicherte Szene aktivieren · mit Wartezeit im Ablauf

[English](README.md) · **Deutsch**

[Licht](../../../README.de.md#lighting) → [Szenen](../../../README.de.md#lighting-scenes)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Warten für 1 s → Eine gespeicherte Szene aktivieren → warten für 52 s 700 ms (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). Starteinstellungen: Geräteereignis.

## Wann startet sie?

- **1.** Geräteereignis: `DEVICE_36`; Geräteereignis/-aktion: nicht erhalten

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Wenn alle folgenden: Zustandsprüfung: `input_boolean.example_01`; Zustand: `on`:

   **Dann:**

   1. Die Lautstärke einstellen — `media_player.example_02`; Lautstärke (0–1): 0.21.

   **Sonst:**

   1. Die Lautstärke einstellen — `media_player.example_02`; Lautstärke (0–1): 0.43.

2. Medien abspielen — `media_player.example_02`; Medienauswahl nicht erhalten.

3. Warten für 1 s.

4. Eine gespeicherte Szene aktivieren — `scene.example_01`.

5. Warten für 52 s 700 ms.

6. Die Wiedergabe starten oder pausieren — `media_player.example_02`.

7. Eine gespeicherte Szene aktivieren — `scene.example_02`.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein eingebundenes Abspielgerät, zum Beispiel einen Lautsprecher.
- Eine gespeicherte Szene mit den gewünschten Geräteeinstellungen.
- Ein eingebundenes Gerät mit einem passenden Ereignis als Auslöser.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
