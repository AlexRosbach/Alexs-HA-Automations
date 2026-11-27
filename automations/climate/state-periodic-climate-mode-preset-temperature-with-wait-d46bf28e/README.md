# Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante D

[Heizung und Raumklima](../../../README.md#climate) → [Heiz- und Klimaprofile](../../../README.md#climate-profiles)

[Alle Vorlagen ansehen](../../../README.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.md)

## Was macht diese Vorlage?

Die Vorlage verbindet folgende Funktionen:

- Heizung oder Klimaanlage einstellen.
- Einen Textwert speichern.

## Wann startet sie?

- Wenn sich ein Wert oder Zustand ändert.
- In einem regelmäßig wiederholten Zeitabstand.

Die genauen Geräte, Werte und Bedingungen legst du beim Einrichten selbst fest.

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein eingebundenes Thermostat oder eine Klimaanlage.
- Einen Helfer, der einen Textwert speichert.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne die [YAML-Vorlage](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
