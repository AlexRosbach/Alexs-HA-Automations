# Durchsagen und Sprachausgabe nutzen

[English](README.md) · **Deutsch**

[Sprache und Durchsagen](../../../README.de.md#voice) → [Durchsagen und Vorlesen](../../../README.de.md#voice-announcements)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

7 Pfade parallel ausführen.

## Wann startet sie?

- **1.** Auslösertyp nicht erhalten: `binary_sensor.example_26`; zu Zustand: nicht erhalten

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Diese Pfade parallel starten. Ihre Ausführungsreihenfolge ist nicht festgelegt.

   **Paralleler Pfad 1:**

   1. Aktionstyp nicht erhalten; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

   **Paralleler Pfad 2:**

   1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_04`; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

   **Paralleler Pfad 3:**

   1. Einen Hinweis in Home Assistant anzeigen; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

   **Paralleler Pfad 4:**

   1. Eine Durchsage abspielen — `assist_satellite.example_02`; Nachrichtentext: nicht erhalten; Ankündigungston: ja; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

   **Paralleler Pfad 5:**

   1. Eine Durchsage abspielen — `assist_satellite.example_03`; Nachrichtentext: nicht erhalten; Ankündigungston: ja; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

   **Paralleler Pfad 6:**

   1. Eine Durchsage abspielen — `assist_satellite.example_01`; Nachrichtentext: nicht erhalten; Ankündigungston: ja; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

   **Paralleler Pfad 7:**

   1. Einen Text vorlesen lassen — `tts.example_01`, nicht erhalten; Nachrichtentext: nicht erhalten; Sprache der Ausgabe: nicht erhalten; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein in Home Assistant eingerichtetes Sprachgerät.
- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Home Assistant für die Anzeige der Hinweise.
- Eine eingerichtete Sprachausgabe und ein passendes Abspielgerät.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
