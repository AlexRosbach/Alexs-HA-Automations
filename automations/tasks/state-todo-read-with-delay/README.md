# Eine Aufgabenliste abfragen · mit Wartezeit im Ablauf

[Aufgabenlisten und Erinnerungen](../../../README.md#tasks) → [Aufgabenlisten abfragen](../../../README.md#tasks-read)

[Alle Vorlagen ansehen](../../../README.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.md)

## Was macht diese Vorlage?

Die Vorlage verbindet folgende Funktionen:

- Einen Zähler erhöhen.
- Einen Zähler zurücksetzen.
- Nachrichten senden.
- Ein vorhandenes Skript ausführen.
- Eine Aufgabenliste abfragen.

## Wann startet sie?

- Wenn sich ein Wert oder Zustand ändert.

Die genauen Geräte, Werte und Bedingungen legst du beim Einrichten selbst fest.

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Einen Zähler-Helfer in Home Assistant.
- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Ein vorhandenes Home-Assistant-Skript, also eine gespeicherte Folge von Aktionen.
- Eine in Home Assistant eingerichtete Aufgabenliste.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne die [YAML-Vorlage](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
