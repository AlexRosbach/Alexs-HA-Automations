# Einen Schalter ausschalten · mit Wartebedingung im Ablauf

[English](README.md) · **Deutsch**

[Schalter und Steckdosen](../../../README.de.md#switches) → [Ausschalten](../../../README.de.md#switches-off)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Warten auf einen Wert unter 8 (bei Ablauf weiter) → wenn die eingestellten Bedingungen erfüllt sind: (Einen Schalter ausschalten); sonst: (Einen Hinweis in Home Assistant anzeigen) (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

Diese Datei enthält keine Auslöser-Definition.

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Bedingungstyp nicht erhalten: `sensor.example_18`; Zustand: nicht erhalten.

## Konkreter Ablauf

1. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

2. Eine vorbereitete Web-Anfrage ausführen — `rest_command.example_01`; nur Simulation: nein; Fortsetzung nach unterstützten Aktionsfehlern eingestellt; Rückgabe für spätere Schritte speichern.

3. Wenn alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten:

   **Dann:**

   1. Einen Hinweis in Home Assistant anzeigen; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

   2. Diesen Durchlauf stoppen.

4. Auf einen dieser Auslöser warten:

   - Auslösertyp nicht erhalten: `sensor.example_19`; unter 8; Dauer nicht erhalten

   Zeitgrenze: nicht erhalten. Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

5. Wenn alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten:

   **Dann:**

   1. Einen Schalter ausschalten — `switch.example_15`.

   **Sonst:**

   1. Einen Hinweis in Home Assistant anzeigen; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Home Assistant für die Anzeige der Hinweise.
- Eine vorbereitete Web-Anfrage, die in Home Assistant als REST-Befehl eingerichtet ist.
- Einen Schalter oder eine schaltbare Steckdose in Home Assistant.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
