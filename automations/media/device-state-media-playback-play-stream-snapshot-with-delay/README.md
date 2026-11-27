# Medien und Kameras steuern · mit Wartezeit im Ablauf

[Musik, Medien und Kameras](../../../README.md#media) → [Kamerabild live anzeigen](../../../README.md#media-camera-live)

[Alle Vorlagen ansehen](../../../README.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.md)

## Was macht diese Vorlage?

Die Vorlage verbindet folgende Funktionen:

- Ein Kamerabild live anzeigen.
- Ein Kamerabild speichern.
- Einen gespeicherten Ein/Aus-Wert einschalten.
- Medien abspielen.
- Nachrichten senden.

## Wann startet sie?

- Wenn ein Gerät ein Ereignis meldet.
- Wenn sich ein Wert oder Zustand ändert.

Die genauen Geräte, Werte und Bedingungen legst du beim Einrichten selbst fest.

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Eine eingebundene Kamera mit der benötigten Bild- oder Videofunktion.
- Einen Ein/Aus-Helfer: ein gespeicherter Schalterwert in Home Assistant.
- Ein eingebundenes Abspielgerät, zum Beispiel einen Lautsprecher.
- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Ein eingebundenes Gerät mit einem passenden Ereignis als Auslöser.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne die [YAML-Vorlage](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
