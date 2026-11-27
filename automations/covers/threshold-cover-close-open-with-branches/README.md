# Eine Abdeckung öffnen und schließen · mit Bedingungen im Ablauf

[Rollläden und Abdeckungen](../../../README.md#covers) → [Öffnen und schließen](../../../README.md#covers-open-close)

[Alle Vorlagen ansehen](../../../README.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.md)

## Was macht diese Vorlage?

Die Vorlage verbindet folgende Funktionen:

- Eine Abdeckung öffnen und schließen.
- Gespeicherte Ein/Aus-Werte ändern.
- Einen Schalter einschalten.

## Wann startet sie?

- Wenn ein Messwert eine eingestellte Grenze überschreitet oder unterschreitet.

Die genauen Geräte, Werte und Bedingungen legst du beim Einrichten selbst fest.

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Ein passendes Gerät, zum Beispiel einen Rollladen oder ein Rollo.
- Einen Ein/Aus-Helfer: ein gespeicherter Schalterwert in Home Assistant.
- Einen Schalter oder eine schaltbare Steckdose in Home Assistant.
- Einen passenden Sensor oder anderen Zahlenwert in Home Assistant und die gewünschte Messwertgrenze.

## Was muss ich anpassen?

1. Öffne die [YAML-Vorlage](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
