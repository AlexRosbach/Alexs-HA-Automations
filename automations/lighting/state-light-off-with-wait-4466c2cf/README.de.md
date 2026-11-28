# Licht ausschalten · mit Wartebedingung im Ablauf — Variante B

[English](README.md) · **Deutsch**

[Licht](../../../README.de.md#lighting) → [Ausschalten](../../../README.de.md#lighting-off)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Auf einen von 2 Auslösern warten (bis zu 15 min; bei Ablauf weiter) → Licht ausschalten (ausgewählte Schritte; 9 weitere Aktionen ausgelassen). Starteinstellungen: Dauer 30 min. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

- **1.** Zustandsänderung: `sensor.example_22`; zu Zustand: nicht erhalten; Dauer 00:30:00 (Zeitformat)

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Formelprüfung: Formel: “\{\{ is\_state\('switch.example\_08','IDENTIFIER\_160'\) or expand\(\['light.example\_10', 'light.example\_11', 'light.example\_12', 'light.example\_18', 'light.example\_19', 'light.example\_20'\]\)\|selectattr\('state','eq','IDENTIFIER\_160'\)\|list\|length&gt;0 \}\}”; Formelprüfung: Formel: “\{\{ as\_timestamp\(now\(\)\) - as\_timestamp\(states\('input\_datetime.example\_01'\),0\)&gt;7200 \}\}”.

## Konkreter Ablauf

1. Ein Datum oder eine Uhrzeit speichern — `input_datetime.example_01`; gespeicherte Zeit: “\{\{ now\(\).timestamp\(\) \}\}”.

2. 2 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

3. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Du bist seit 30 Minuten im Schlafzimmer. Soll ich das Büro person ausschalten?”; Nachrichtentitel: “Büro ausschalten?”.

4. Auf einen dieser Auslöser warten:

   - Ereignis: Ereignisname: nicht erhalten
   - Ereignis: Ereignisname: nicht erhalten

   Zeitgrenze: 00:15:00 (Zeitformat). Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

5. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “clear\_notification”.

6. Prüfen: Formelprüfung: Formel: “\{\{ wait.trigger is not none and wait.trigger.event.example\_05.action==variable\_58 \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

7. Prüfen: Zustandsprüfung: `sensor.example_22`; Zustand: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

8. Prüfen: Zustandsprüfung: `binary_sensor.example_27`; Zustand: `off`. Falls falsch, den aktuellen Ablauf hier stoppen.

9. Licht ausschalten — `light.example_10`, `light.example_11`, `light.example_12`, `light.example_18`, `light.example_19`, `light.example_20`.

10. Ein eigenes Skript ausführen — `script.example_07`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

11. Wenn alle folgenden: Zustandsprüfung: `switch.example_08`; Zustand: `on`:

    **Dann:**

    1. Ein eigenes Skript ausführen — `script.example_08`.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Die Geräte und die Aktion, die du selbst ergänzen möchtest.
- Einen Helfer, der ein Datum oder eine Uhrzeit speichert.
- Lampen, die Home Assistant steuern kann.
- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Ein vorhandenes Home-Assistant-Skript, also eine gespeicherte Folge von Aktionen.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
