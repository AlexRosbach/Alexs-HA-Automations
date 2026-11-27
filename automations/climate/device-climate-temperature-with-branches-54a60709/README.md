# Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf — Variante A

[Heizung und Raumklima](../../../README.md#climate) → [Temperatur einstellen](../../../README.md#climate-temperature)

[Alle Vorlagen ansehen](../../../README.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.md)

## Was macht diese Vorlage?

Die gewünschte Raumtemperatur einstellen.

## Wann startet sie?

- Wenn ein Gerät ein Ereignis meldet.

Die genauen Geräte, Werte und Bedingungen legst du beim Einrichten selbst fest.

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein eingebundenes Thermostat oder eine Klimaanlage.
- Ein eingebundenes Gerät mit einem passenden Ereignis als Auslöser.

## Was muss ich anpassen?

1. Öffne die [YAML-Vorlage](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
