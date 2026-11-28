# Licht ausschalten · mit Wartebedingung im Ablauf — Variante C

[English](README.md) · **Deutsch**

[Licht](../../../README.de.md#lighting) → [Ausschalten](../../../README.de.md#lighting-off)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Auf einen von 11 Auslösern warten (bis zu 15 min; bei Ablauf weiter) (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `off`; Dauer 55 min. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

- **1.** Zustandsänderung: `binary_sensor.example_25`; zu Zustand: `off`; Dauer 00:55:00 (Zeitformat)

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: mindestens eine der folgenden [Zustandsprüfung: `light.example_02`; Zustand: `on`; Zustandsprüfung: `light.example_03`; Zustand: `on`; Zustandsprüfung: `switch.example_04`; Zustand: `on`].

## Konkreter Ablauf

1. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

2. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Seit 55 Minuten keine Bewegung. Soll ich alles ausschalten?”; Nachrichtentitel: “Wohnzimmer”.

3. Eine Nachricht an ein eigenes Ziel senden — `notify.example_02`; Nachrichtentext: “Seit 55 Minuten keine Bewegung. Soll ich alles ausschalten?”; Nachrichtentitel: “Wohnzimmer”.

4. Auf einen dieser Auslöser warten:

   - Ereignis: Ereignisname: nicht erhalten
   - Ereignis: Ereignisname: nicht erhalten
   - Zustandsänderung: `binary_sensor.example_25`; zu Zustand: `on`
   - Zustandsänderung: `binary_sensor.example_02`; zu Zustand: `on`
   - Zustandsänderung: `binary_sensor.example_26`; zu Zustand: `on`
   - Zustandsänderung: `binary_sensor.example_11`; zu Zustand: `on`
   - Zustandsänderung: `binary_sensor.example_01`; zu Zustand: `on`
   - Zustandsänderung: `binary_sensor.example_27`; zu Zustand: `on`
   - Zustandsänderung: `light.example_02`; zu Zustand: `on`
   - Zustandsänderung: `light.example_03`; zu Zustand: `on`
   - Zustandsänderung: `switch.example_04`; zu Zustand: `on`

   Zeitgrenze: 00:15:00 (Zeitformat). Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

5. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Formelprüfung: Formel: “\{\{ wait.trigger is not none and wait.trigger.platform == 'event' and wait.trigger.event.example\_05.action == 'WZ\_SHUTDOWN\_YES' \}\}”

   1. Licht ausschalten — `light.example_02`, `light.example_03`.

   2. **Deaktivierter Schritt:** Einen Schalter ausschalten — `switch.example_04`.

   3. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Alles klar. Wohnzimmer ist aus.”.

   4. Eine Nachricht an ein eigenes Ziel senden — `notify.example_02`; Nachrichtentext: “Alles klar. Wohnzimmer ist aus.”.

   **Zweig 2:** alle folgenden: Formelprüfung: Formel: “\{\{ wait.trigger is not none and wait.trigger.platform == 'event' and wait.trigger.event.example\_05.action == 'WZ\_SHUTDOWN\_NO' \}\}”

   1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Okay. Ich mache nichts.”.

   2. Eine Nachricht an ein eigenes Ziel senden — `notify.example_02`; Nachrichtentext: “Okay. Ich mache nichts.”.

   **Zweig 3:** alle folgenden: Formelprüfung: Formel: “\{\{ wait.trigger is not none and wait.trigger.platform == 'state' \}\}”

   1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Bewegung oder neue person erkannt. Ich lasse das Wohnzimmer an.”.

   2. Eine Nachricht an ein eigenes Ziel senden — `notify.example_02`; Nachrichtentext: “Bewegung oder neue person erkannt. Ich lasse das Wohnzimmer an.”.

   **Wenn kein Zweig passt:**

   1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Na gut. Wenn keiner antwortet, mach ich’s selbst. 😤”.

   2. Eine Nachricht an ein eigenes Ziel senden — `notify.example_02`; Nachrichtentext: “Na gut. Wenn keiner antwortet, mach ich’s selbst. 😤”.

   3. Licht ausschalten — `light.example_02`, `light.example_03`.

   4. Einen Schalter ausschalten — `switch.example_04`.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Die Geräte und die Aktion, die du selbst ergänzen möchtest.
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
