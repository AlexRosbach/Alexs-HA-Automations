# Die gewünschte Raumtemperatur einstellen · mit Wartebedingung im Ablauf

[Heizung und Raumklima](../../../README.md#climate) → [Temperatur einstellen](../../../README.md#climate-temperature)

[Alle Vorlagen ansehen](../../../README.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.md)

## Was macht diese Vorlage?

Die Vorlage verbindet folgende Funktionen:

- Andere Automationen aktivieren und deaktivieren.
- Die gewünschte Raumtemperatur einstellen.
- Gespeicherte Ein/Aus-Werte ändern.
- Licht einschalten.
- Die Medienwiedergabe steuern.
- Einen Schalter ausschalten.

## Wann startet sie?

- Wenn sich ein Wert oder Zustand ändert.

Die genauen Geräte, Werte und Bedingungen legst du beim Einrichten selbst fest.

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

1. Öffne die [YAML-Vorlage](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
