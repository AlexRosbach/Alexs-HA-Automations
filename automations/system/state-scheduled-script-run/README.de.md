# Ein vorhandenes Skript ausführen

[English](README.md) · **Deutsch**

[Weitere Abläufe und Geräteaktionen](../../../README.de.md#system) → [Eigene Skripte](../../../README.de.md#system-scripts)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Wiederholen für jeden Listeneintrag: Bedingungen prüfen; bei falsch diesen Ablauf stoppen. Starteinstellungen: um 10:00:00 / Zustandsänderung.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Feste Uhrzeit: um 10:00:00
- **2.** Zustandsänderung: `sensor.example_25`, `sensor.example_26`, `sensor.example_27`, `sensor.example_28`, `sensor.example_29`, `sensor.example_30`

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Für jeden Listeneintrag wiederholen; Anzahl Einträge: 6.

   1. Prüfen: Formelprüfung: Formel: “\{% set e=repeat.item.sensor %\}\{% set v=states\(e\)\|float\(-1\) %\}\{% set u=state\_attr\(e,'unit\_of\_measurement'\) %\}\{\{ v &gt;= 0 and \(v &lt;= 0 if repeat.item.prefilter else \(\(u=='%' and v&lt;=10\) or \(u=='h' and v&lt;=168\)\)\) \}\}”. Falls falsch, den aktuellen Ablauf hier stoppen.

   2. Ein eigenes Skript ausführen — `script.example_01`.

## Wenn sie erneut ausgelöst wird

`queued`: Neue Durchläufe warten in einer Warteschlange und laufen in Eingangsreihenfolge. Sie werden nur eingereiht, wenn die Bedingungen beim Auslösen erfüllt sind. Grenze für laufende und wartende Durchläufe: 10.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein vorhandenes Home-Assistant-Skript, also eine gespeicherte Folge von Aktionen.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
