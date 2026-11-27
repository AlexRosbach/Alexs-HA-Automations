# Medien und Kameras steuern · mit Wartezeit im Ablauf

[English](README.md) · **Deutsch**

[Musik, Medien und Kameras](../../../README.de.md#media) → [Kamerabild live anzeigen](../../../README.de.md#media-camera-live)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Wenn die eingestellten Bedingungen erfüllt sind: (Medien abspielen → warten für 2 s 500 ms → 1 weiterer Schritt) → Ein Kamerabild speichern → warten für nicht erhalten (ausgewählte Schritte; 5 weitere Aktionen ausgelassen).

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Auslösertyp nicht erhalten: `binary_sensor.example_17`; von Zustand: ohne Wert (null); zu Zustand: nicht erhalten
- **2.** Auslösertyp nicht erhalten: `event.example_05`; zu Zustand: nicht erhalten; Attributname: nicht erhalten
- **3.** Auslösertyp nicht erhalten: `binary_sensor.example_17`; zu Zustand: nicht erhalten
- **4.** Auslösertyp nicht erhalten: `ENTITY_43`, `DEVICE_49`; Geräteereignis/-aktion: nicht erhalten

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Wenn alle folgenden: Bedingungstyp nicht erhalten: `input_boolean.example_09`; Zustand: nicht erhalten:

   **Dann:**

   1. Medien abspielen — `media_player.example_03`; Medienauswahl nicht erhalten.

   2. Warten für 2 s 500 ms.

   3. Medien abspielen — `media_player.example_03`; Medienauswahl nicht erhalten.

2. Ein Kamerabild speichern — `camera.example_01`; Dateiziel: nicht erhalten.

3. Warten für nicht erhalten.

4. Eine Nachricht an ein eigenes Ziel senden — `notify.example_04`; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

5. Aktionstyp nicht erhalten; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

6. Einen gespeicherten Ein/Aus-Wert einschalten — `input_boolean.example_03`, `input_boolean.example_04`.

7. Wenn alle folgenden: Bedingungstyp nicht erhalten: `media_player.example_04`; Zustand: nicht erhalten:

   **Dann:**

   1. Ein Kamerabild live anzeigen — `camera.example_01`; Stream-Format: nicht erhalten.

   2. Aktionstyp nicht erhalten; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

8. Aktionstyp nicht erhalten — `ENTITY_44`, `DEVICE_50`.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Eine eingebundene Kamera mit der benötigten Bild- oder Videofunktion.
- Einen Ein/Aus-Helfer: ein gespeicherter Schalterwert in Home Assistant.
- Ein eingebundenes Abspielgerät, zum Beispiel einen Lautsprecher.
- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Ein eingebundenes Gerät mit einem passenden Ereignis als Auslöser.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
