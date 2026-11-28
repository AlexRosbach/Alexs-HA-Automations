# Die gewünschte Raumtemperatur einstellen · mit Wartebedingung im Ablauf

[English](README.md) · **Deutsch**

[Heizung und Raumklima](../../../README.de.md#climate) → [Temperatur einstellen](../../../README.de.md#climate-temperature)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Temperatur auf 24 setzen; Heiz-/Kühlmodus: `heat` → warten auf von Zustand: `on`; zu Zustand: `off` (bis zu 3 h; bei Ablauf weiter) → Temperatur auf 21 setzen; Heiz-/Kühlmodus: `auto` (ausgewählte Schritte; 10 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `on`.

## Wann startet sie?

- **1.** Zustandsänderung: `input_boolean.example_03`; zu Zustand: `on`

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Einen gespeicherten Ein/Aus-Wert einschalten — `input_boolean.example_04`.

2. Licht einschalten — `light.example_01`; Helligkeit: 60%; Übergang: 2 s; Farbwerte: 200, 0, 255.

3. Einen Schalter ausschalten — `switch.example_01`, `switch.example_03`.

4. Eine andere Automation deaktivieren — `automation.example_05`, `automation.example_03`; laufende betroffene Aktionen stoppen: ja.

5. Die Lautstärke einstellen — `media_player.example_02`; Lautstärke (0–1): 0.2.

6. Medien abspielen — `media_player.example_02`; Medienauswahl nicht erhalten.

7. Die gewünschte Raumtemperatur einstellen — `climate.example_02`; Temperaturwert (Einheit nicht angegeben): 24; Heiz-/Kühlmodus: `heat`.

8. Auf einen dieser Auslöser warten:

   - Zustandsänderung: `input_boolean.example_03`; von Zustand: `on`; zu Zustand: `off`

   Zeitgrenze: 3 h. Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

9. Licht einschalten — `light.example_01`; Helligkeit: 60%; Übergang: 5 s; Farbtemperatur: 6500 K.

10. Eine andere Automation aktivieren — `automation.example_05`, `automation.example_03`.

11. Die gewünschte Raumtemperatur einstellen — `climate.example_02`; Temperaturwert (Einheit nicht angegeben): 21; Heiz-/Kühlmodus: `auto`.

12. Die Wiedergabe pausieren — `media_player.example_02`.

13. Einen gespeicherten Ein/Aus-Wert ausschalten — `input_boolean.example_04`.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Die anderen Automationen, die du damit starten oder schalten möchtest.
- Ein eingebundenes Thermostat oder eine Klimaanlage.
- Einen Ein/Aus-Helfer: ein gespeicherter Schalterwert in Home Assistant.
- Lampen, die Home Assistant steuern kann.
- Ein eingebundenes Abspielgerät, zum Beispiel einen Lautsprecher.
- Einen Schalter oder eine schaltbare Steckdose in Home Assistant.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
