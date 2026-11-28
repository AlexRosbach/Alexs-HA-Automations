# Eine Aufgabenliste lesen und bearbeiten · mit Bedingungen im Ablauf

[English](README.md) · **Deutsch**

[Aufgabenlisten und Erinnerungen](../../../README.de.md#tasks) → [Einträge bearbeiten](../../../README.de.md#tasks-edit)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Eine Aufgabenliste abfragen; Aufgabenstatus: `needs_action` → wiederholen für jeden Listeneintrag: Zwischenwerte vorbereiten. Starteinstellungen: Minuten: 0 / Home-Assistant-Ereignis.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Wiederholter Zeitplan: Minuten: 0
- **2.** Home-Assistant-Ereignis: Ereignis: `start`

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Eine Aufgabenliste abfragen — `todo.example_01`; Aufgabenstatus: `needs_action`; Rückgabe für spätere Schritte speichern.

2. Für jeden Listeneintrag wiederholen; Anzahl Einträge: 4.

   1. 9 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   2. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Formelprüfung: Formel: “\{\{ variable\_04 not in \['unknown', 'unavailable', 'none', 'None', ''\] and level &lt;= threshold and not variable\_39 \}\}”

      1. Ein eigenes Skript ausführen — `script.example_01`.

      2. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “\{\{ variable\_38 \}\} hat \{\{ variable\_04 \}\}% Akku. Bitte laden oder Batterie wechseln.”; Nachrichtentitel: “Akku kritisch”.

      **Zweig 2:** alle folgenden: Formelprüfung: Formel: “\{\{ variable\_04 not in \['unknown', 'unavailable', 'none', 'None', ''\] and level &gt; threshold and variable\_39 \}\}”

      1. Einen Eintrag in einer Aufgabenliste ändern — `todo.example_01`; Aufgabenstatus: `completed`; Aufgabeneintrag: “\{\{ variable\_23.uid \}\}”.

      Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Ein vorhandenes Home-Assistant-Skript, also eine gespeicherte Folge von Aktionen.
- Eine in Home Assistant eingerichtete Aufgabenliste.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
