# Licht ein- und ausschalten · mit Wartebedingung im Ablauf — Variante B

[English](README.md) · **Deutsch**

[Licht](../../../README.de.md#lighting) → [Ein- und Ausschalten](../../../README.de.md#lighting-on-off)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Auf einen von 2 Auslösern warten (bei Ablauf stoppen) → den ersten passenden Zweig ausführen: wenn die eingestellten Bedingungen erfüllt sind: (Einen Schalter einschalten) → Licht ausschalten; Übergang: 2 s → 4 weitere Schritte / Aktionstyp nicht erhalten → Eine Nachricht an ein eigenes Ziel senden → 1 weiterer Schritt (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Starteinstellungen: Dauer 10 s. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Auslösertyp nicht erhalten: `media_player.example_04`; von Zustand: nicht erhalten; zu Zustand: nicht erhalten; Dauer 10 s
- **2.** Auslösertyp nicht erhalten: `media_player.example_04`; von Zustand: nicht erhalten; zu Zustand: nicht erhalten; Dauer 10 s
- **3.** Auslösertyp nicht erhalten: `remote.example_01`; von Zustand: nicht erhalten; zu Zustand: nicht erhalten; Dauer 10 s

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Bedingungstyp nicht erhalten: `media_player.example_04`; Zustand: nicht erhalten.

## Konkreter Ablauf

1. 6 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

2. Aktionstyp nicht erhalten; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

3. Eine Nachricht an ein eigenes Ziel senden — `notify.example_04`; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

4. Auf einen dieser Auslöser warten:

   - Auslösertyp nicht erhalten: Ereignisname: nicht erhalten
   - Auslösertyp nicht erhalten: Ereignisname: nicht erhalten

   Zeitgrenze: nicht erhalten. Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.

5. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

   1. Wenn alle folgenden: Bedingungstyp nicht erhalten: `binary_sensor.example_08`; Zustand: nicht erhalten:

      **Dann:**

      1. Einen Schalter einschalten — `switch.example_06`.

   2. Licht ausschalten — `light.example_13`; Übergang: 2 s.

   3. Licht einschalten — `light.example_14`; Helligkeit: 10%; Übergang: 2 s; Farbtemperatur: 2202 K.

   4. Aktionstyp nicht erhalten; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

   5. Eine Nachricht an ein eigenes Ziel senden — `notify.example_04`; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

   6. Warten für nicht erhalten.

   **Zweig 2:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

   1. Aktionstyp nicht erhalten; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

   2. Eine Nachricht an ein eigenes Ziel senden — `notify.example_04`; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

   3. Warten für nicht erhalten.

   Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Lampen, die Home Assistant steuern kann.
- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Einen Schalter oder eine schaltbare Steckdose in Home Assistant.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
