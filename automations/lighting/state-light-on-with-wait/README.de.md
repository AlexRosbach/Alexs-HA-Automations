# Licht einschalten · mit Wartebedingung im Ablauf

[English](README.md) · **Deutsch**

[Licht](../../../README.de.md#lighting) → [Einschalten](../../../README.de.md#lighting-on)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Auf einen von 2 Auslösern warten (bis zu 5 min; bei Ablauf stoppen) → den ersten passenden Zweig ausführen: Licht mit 100 % Helligkeit einschalten; Übergang: 3 s; Farbwerte: 255, 255, 255 (ausgewählte Schritte; 2 weitere Aktionen ausgelassen). Starteinstellungen: von Zustand: `off`; zu Zustand: `on`.

## Wann startet sie?

- **1.** Zustandsänderung: `binary_sensor.example_24`; von Zustand: `off`; zu Zustand: `on`

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. 2 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

2. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Dein ArbeitsPC ist online. Office Modus aktivieren ?”; Nachrichtentitel: “Office Modus ?”.

3. Auf einen dieser Auslöser warten:

   - Ereignis: Ereignisname: nicht erhalten
   - Ereignis: Ereignisname: nicht erhalten

   Zeitgrenze: 00:05:00 (Zeitformat). Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.

4. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Formelprüfung: Formel: “\{\{ wait.trigger.event.example\_05.action == variable\_24 \}\}”

   1. Licht einschalten — `DEVICE_27`, `DEVICE_28`; Helligkeit: 100%; Übergang: 3 s; Farbwerte: 255, 255, 255.

   Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`restart`: Ein neuer Auslöser stoppt den laufenden Durchlauf und startet neu, sofern die Bedingungen der Automation erfüllt sind.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Die Geräte und die Aktion, die du selbst ergänzen möchtest.
- Lampen, die Home Assistant steuern kann.
- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
