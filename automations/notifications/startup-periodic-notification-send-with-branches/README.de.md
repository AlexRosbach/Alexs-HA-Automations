# Nachrichten senden · mit Bedingungen im Ablauf

[English](README.md) · **Deutsch**

[Nachrichten und Hinweise](../../../README.de.md#notifications) → [Nachrichten versenden](../../../README.de.md#notifications-messages)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Eine Wettervorhersage abrufen → Zwischenwerte vorbereiten → 1 weiterer Schritt (siehe Ablauf). Starteinstellungen: Minuten: 10 / Home-Assistant-Ereignis. Vor den Aktionen werden Bedingungen geprüft.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Wiederholter Zeitplan: Minuten: 10
- **2.** Home-Assistant-Ereignis: Ereignis: `start`

## Was muss vorher erfüllt sein?

Bevor die Aktionen starten: alle folgenden: Formelprüfung: Formel: “\{\{ 7 &lt;= now\(\).hour &lt;= 21 \}\}”; Formelprüfung: Formel: “\{% set last = this.attributes.last\_triggered %\} \{\{ last is none or \(now\(\) - last\).total\_seconds\(\) &gt; 7200 \}\}”.

## Konkreter Ablauf

1. Eine Wettervorhersage abrufen — `weather.example_01`; Rückgabe für spätere Schritte speichern.

2. 10 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

3. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Formelprüfung: Formel: “\{\{ variable\_49 \| bool \}\}”

   1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Forecast: max \{\{ variable\_44 \}\} °C, UV \{\{ variable\_45 \}\}, min. Bewoelkung \{\{ variable\_46 \}\} %. Innen: Schlafzimmer \{\{ variable\_40 \}\} °C, Haus \{\{ variable\_47 \}\} °C. Solar Resttag \{\{ variable\_48 \}\} kWh. \{\{ variable\_43 \}\}”; Nachrichtentitel: “Proaktiver Hitzeschutz”.

   2. Eine Nachricht an ein eigenes Ziel senden — `notify.example_02`; Nachrichtentext: “Forecast: max \{\{ variable\_44 \}\} °C, UV \{\{ variable\_45 \}\}, min. Bewoelkung \{\{ variable\_46 \}\} %. Innen: Schlafzimmer \{\{ variable\_40 \}\} °C, Haus \{\{ variable\_47 \}\} °C. Solar Resttag \{\{ variable\_48 \}\} kWh. \{\{ variable\_43 \}\}”; Nachrichtentitel: “Proaktiver Hitzeschutz”.

   Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`single`: Wird sie während eines laufenden Durchlaufs erneut ausgelöst, startet kein neuer Durchlauf.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Eine Wetteranbindung, die Vorhersagen bereitstellt.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
