# Einen Saugroboter starten · mit Wartezeit im Ablauf

[English](README.md) · **Deutsch**

[Saugroboter](../../../README.de.md#cleaning) → [Starten](../../../README.de.md#cleaning-start)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Warten für 3 s → Einen Saugroboter starten (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Starteinstellungen: Zustandsänderung. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Zustandsänderung: `sensor.example_08`; zu Zustand: nicht erhalten
- **2.** Zustandsänderung: `sensor.example_20`; zu Zustand: nicht erhalten

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Formelprüfung: Formel: “\{\{ states\('vacuum.example\_02'\) == 'paused' and \(states\('sensor.example\_08'\) == 'water\_tank\_dry' or states\('sensor.example\_20'\) == 'washing\_paused'\) \}\}”.

## Konkreter Ablauf

1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Wasser fehlt. Ich stelle auf Nur-person um person starte den Lauf person.”; Nachrichtentitel: “person Wohnzimmer”.

2. Eine Nachricht an ein eigenes Ziel senden — `notify.example_02`; Nachrichtentext: “Wasser fehlt. Ich stelle auf Nur-person um person starte den Lauf person.”; Nachrichtentitel: “person Wohnzimmer”.

3. Eine Geräteoption auswählen — `select.example_02`; gewählte Option: “sweeping”; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

4. Warten für 00:00:03 (Zeitformat).

5. Einen Saugroboter starten — `vacuum.example_02`.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Ein Gerät mit einer in Home Assistant auswählbaren Option.
- Einen in Home Assistant eingebundenen Saugroboter.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
