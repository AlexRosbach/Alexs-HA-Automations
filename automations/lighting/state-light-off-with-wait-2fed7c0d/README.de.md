# Licht ausschalten · mit Wartebedingung im Ablauf — Variante A

[English](README.md) · **Deutsch**

[Licht](../../../README.de.md#lighting) → [Ausschalten](../../../README.de.md#lighting-off)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Warten für 30 min → auf einen von 2 Auslösern warten (bis zu 15 min; bei Ablauf weiter) (ausgewählte Schritte; 5 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `not_home`.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Zustandsänderung: `person.example_01`; zu Zustand: `not_home`
- **2.** Zustandsänderung: `person.example_02`; zu Zustand: `not_home`

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Warten für 30 min.

2. Prüfen: Zustandsprüfung: `person.example_01`; Zustand: `not_home`. Falls falsch, den aktuellen Ablauf hier stoppen.

3. Prüfen: Zustandsprüfung: `person.example_02`; Zustand: `not_home`. Falls falsch, den aktuellen Ablauf hier stoppen.

4. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Ihr seid seit 30 Minuten außer Haus. Soll ich alles ausschalten?”; Nachrichtentitel: “Haushalt”.

5. Eine Nachricht an ein eigenes Ziel senden — `notify.example_02`; Nachrichtentext: “Ihr seid seit 30 Minuten außer Haus. Soll ich alles ausschalten?”; Nachrichtentitel: “Haushalt”.

6. Auf einen dieser Auslöser warten:

   - Ereignis: Ereignisname: nicht erhalten
   - Ereignis: Ereignisname: nicht erhalten

   Zeitgrenze: 00:15:00 (Zeitformat). Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

7. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Formelprüfung: Formel: “\{\{ wait.trigger is not none and wait.trigger.event.example\_05.action == 'HH\_SHUTDOWN\_YES' \}\}”

   1. Licht ausschalten — `light.example_13`, `light.example_14`, `light.example_10`, `light.example_12`, `light.example_06`, `light.example_01`, `light.example_11`.

   2. Ein eigenes Skript ausführen — `script.example_07`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

   3. Einen Schalter ausschalten — `switch.example_08`.

   4. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Alles klar. Habe ausgeschaltet.”.

   5. Eine Nachricht an ein eigenes Ziel senden — `notify.example_02`; Nachrichtentext: “Alles klar. Habe ausgeschaltet.”.

   **Zweig 2:** alle folgenden: Formelprüfung: Formel: “\{\{ wait.trigger is not none and wait.trigger.event.example\_05.action == 'HH\_SHUTDOWN\_NO' \}\}”

   1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Okay. Ich mache nichts.”.

   2. Eine Nachricht an ein eigenes Ziel senden — `notify.example_02`; Nachrichtentext: “Okay. Ich mache nichts.”.

   **Wenn kein Zweig passt:**

   1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Na gut. Wenn keiner antwortet, mach ich’s halt selbst. 😤”.

   2. Eine Nachricht an ein eigenes Ziel senden — `notify.example_02`; Nachrichtentext: “Na gut. Wenn keiner antwortet, mach ich’s halt selbst. 😤”.

   3. Licht ausschalten — `light.example_13`, `light.example_14`, `light.example_10`, `light.example_12`, `light.example_01`, `light.example_11`.

   4. Ein eigenes Skript ausführen — `script.example_07`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

   5. Einen Schalter ausschalten — `switch.example_04`, `switch.example_08`.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Die Geräte und die Aktion, die du selbst ergänzen möchtest.
- Lampen, die Home Assistant steuern kann.
- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Ein vorhandenes Home-Assistant-Skript, also eine gespeicherte Folge von Aktionen.
- Einen Schalter oder eine schaltbare Steckdose in Home Assistant.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
