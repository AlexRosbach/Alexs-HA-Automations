# Einen Schalter ausschalten · mit Wartebedingung im Ablauf

[English](README.md) · **Deutsch**

[Schalter und Steckdosen](../../../README.de.md#switches) → [Ausschalten](../../../README.de.md#switches-off)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Warten auf einen Wert unter 8 (bis zu 10 min; bei Ablauf weiter) → wenn die eingestellten Bedingungen erfüllt sind: (Einen Schalter ausschalten); sonst: (Einen Hinweis in Home Assistant anzeigen; Nachrichtentext: “Das sichere person wurde nicht bestätigt. person muss offline sein person die Steckdose 60 Sekunden IDENTIFIER\_25 …“; Nachrichtentitel: “person-Steckdose bleibt an”) (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

Diese Datei enthält keine Auslöser-Definition.

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Zustandsprüfung: `sensor.example_23`; Zustand: nicht erhalten.

## Konkreter Ablauf

1. 1 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

2. Eine vorbereitete Web-Anfrage ausführen — `rest_command.example_01`; nur Simulation: nein; Fortsetzung nach unterstützten Aktionsfehlern eingestellt; Rückgabe für spätere Schritte speichern.

3. Wenn alle folgenden: Formelprüfung: Formel: “\{\{ variable\_57 is not defined or variable\_57.status \!= 202 or not variable\_57.content.accepted \}\}”:

   **Dann:**

   1. Einen Hinweis in Home Assistant anzeigen; Nachrichtentext: “Das sichere person wurde nicht bestätigt. person muss offline sein person die Steckdose 60 Sekunden IDENTIFIER\_25 person 8 W mit aktuellen Messwerten melden. Bitte person oder person Programme prüfen.”; Nachrichtentitel: “person-Steckdose bleibt an”.

   2. Diesen Durchlauf stoppen mit einem Fehler.

4. Auf einen dieser Auslöser warten:

   - Überschreiten oder Unterschreiten eines Zahlenwerts: `sensor.example_24`; unter 8; Dauer 00:01:00 (Zeitformat)

   Zeitgrenze: 00:10:00 (Zeitformat). Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

5. Wenn alle folgenden: Formelprüfung: Formel: “\{\{ wait.completed and states\('sensor.example\_23'\) in \['unavailable','unknown'\] and is\_number\(states\('sensor.example\_24'\)\) and 0 &lt;= states\('sensor.example\_24'\) \| float &lt; 8 and as\_timestamp\(states.sensor.example\_24.last\_updated\) &gt; request\_time \| float and as\_timestamp\(now\(\)\) - as\_timestamp\(states.sensor.example\_24.last\_reported\) &lt; 90 \}\}”:

   **Dann:**

   1. Einen Schalter ausschalten — `switch.example_15`.

   **Sonst:**

   1. Einen Hinweis in Home Assistant anzeigen; Nachrichtentext: “Das sichere person wurde nicht bestätigt. person muss offline sein person die Steckdose 60 Sekunden IDENTIFIER\_25 person 8 W mit aktuellen Messwerten melden. Bitte person oder person Programme prüfen.”; Nachrichtentitel: “person-Steckdose bleibt an”.

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
