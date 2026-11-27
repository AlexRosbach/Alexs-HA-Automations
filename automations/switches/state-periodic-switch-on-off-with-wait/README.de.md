# Schalter ein- und ausschalten · mit Wartebedingung im Ablauf

[English](README.md) · **Deutsch**

[Schalter und Steckdosen](../../../README.de.md#switches) → [Ein- und Ausschalten](../../../README.de.md#switches-on-off)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

3 Pfade parallel ausführen. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Auslösertyp nicht erhalten: `person.example_02`, `person.example_01`, `input_boolean.example_06`; zu Zustand: ohne Wert (null); Auslöser-Verweis: `ID_11`
- **2.** Auslösertyp nicht erhalten: Ereignis: nicht erhalten; Auslöser-Verweis: `ID_04`
- **3.** Auslösertyp nicht erhalten: Minuten: nicht erhalten; Auslöser-Verweis: `ID_12`

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten.

## Konkreter Ablauf

1. Diese Pfade parallel starten. Ihre Ausführungsreihenfolge ist nicht festgelegt.

   **Paralleler Pfad 1:**

   1. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

      1. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

      2. Eine Gerätefunktion per Tastendruck auslösen — `button.example_02`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

      3. Eine Gerätefunktion per Tastendruck auslösen — `button.example_03`.

      4. Warten für nicht erhalten.

      5. Eine Gerätefunktion per Tastendruck auslösen — `button.example_02`.

      6. Einen Schalter einschalten — `switch.example_09`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

      **Wenn kein Zweig passt:**

      1. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

      2. Einen Schalter ausschalten — `switch.example_09`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

      3. Warten, bis eine Formel wahr ist; die Formel ist nicht erhalten.

         Zeitgrenze: nicht erhalten. Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.

      4. Eine Gerätefunktion per Tastendruck auslösen — `button.example_02`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

      5. Eine Gerätefunktion per Tastendruck auslösen — `button.example_04`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

   **Paralleler Pfad 2:**

   1. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

      1. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

      2. Eine Gerätefunktion per Tastendruck auslösen — `button.example_05`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

      3. Eine Gerätefunktion per Tastendruck auslösen — `button.example_06`.

      4. Warten für nicht erhalten.

      5. Eine Gerätefunktion per Tastendruck auslösen — `button.example_05`.

      6. Einen Schalter einschalten — `switch.example_10`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

      **Wenn kein Zweig passt:**

      1. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

      2. Einen Schalter ausschalten — `switch.example_10`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

      3. Warten, bis eine Formel wahr ist; die Formel ist nicht erhalten.

         Zeitgrenze: nicht erhalten. Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.

      4. Eine Gerätefunktion per Tastendruck auslösen — `button.example_05`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

      5. Eine Gerätefunktion per Tastendruck auslösen — `button.example_07`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

   **Paralleler Pfad 3:**

   1. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

      1. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

      2. Eine Gerätefunktion per Tastendruck auslösen — `button.example_08`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

      3. Eine Gerätefunktion per Tastendruck auslösen — `button.example_09`.

      4. Warten für nicht erhalten.

      5. Eine Gerätefunktion per Tastendruck auslösen — `button.example_08`.

      6. Einen Schalter einschalten — `switch.example_11`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

      **Wenn kein Zweig passt:**

      1. Prüfen: Bedingungstyp nicht erhalten: Formel: nicht erhalten. Falls falsch, den aktuellen Ablauf hier stoppen.

      2. Einen Schalter ausschalten — `switch.example_11`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

      3. Warten, bis eine Formel wahr ist; die Formel ist nicht erhalten.

         Zeitgrenze: nicht erhalten. Bei Ablauf der Zeitgrenze diesen Ablauf stoppen.

      4. Eine Gerätefunktion per Tastendruck auslösen — `button.example_08`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

      5. Eine Gerätefunktion per Tastendruck auslösen — `button.example_10`; Fortsetzung nach unterstützten Aktionsfehlern eingestellt.

## Wenn sie erneut ausgelöst wird

`restart`: Ein neuer Auslöser stoppt den laufenden Durchlauf und startet neu, sofern die Bedingungen der Automation erfüllt sind.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Eine Gerätefunktion, die Home Assistant als Taste bereitstellt.
- Einen Schalter oder eine schaltbare Steckdose in Home Assistant.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
