# Lüfter ein- und ausschalten sowie einstellen · mit Wartebedingung im Ablauf

[English](README.md) · **Deutsch**

[Lüfter und Luftreiniger](../../../README.de.md#ventilation) → [Betriebsprofile auswählen](../../../README.de.md#ventilation-profiles)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Eine Automation aus Alex' Home-Assistant-Setup, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Den ersten passenden Zweig ausführen: Zwischenwerte vorbereiten → Einen Lüfter einschalten → 5 weitere Schritte / Zwischenwerte vorbereiten → Einen Lüfter einschalten → 5 weitere Schritte; 1 weiterer Zweig.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Auslösertyp nicht erhalten: `vacuum.example_06`; zu Zustand: nicht erhalten; Auslöser-Verweis: `ID_16`
- **2.** Auslösertyp nicht erhalten: `vacuum.example_05`; zu Zustand: nicht erhalten; Auslöser-Verweis: `ID_17`
- **3.** Auslösertyp nicht erhalten: `vacuum.example_02`; zu Zustand: nicht erhalten; Auslöser-Verweis: `ID_18`

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Auslöser-Verweis: `ID_16`

   1. 2 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   2. Einen Lüfter einschalten — `fan.example_02`.

   3. Ein Lüfterprofil auswählen — `fan.example_02`; Profil: nicht erhalten.

   4. Diese Pfade parallel starten. Ihre Ausführungsreihenfolge ist nicht festgelegt.

      **Paralleler Pfad 1:**

      1. Aktionstyp nicht erhalten; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

      **Paralleler Pfad 2:**

      1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_04`; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

   5. Auf einen dieser Auslöser warten:

      - Auslösertyp nicht erhalten: `vacuum.example_06`; von Zustand: nicht erhalten
      - Auslösertyp nicht erhalten: `vacuum.example_06`; von Zustand: nicht erhalten
      - Auslösertyp nicht erhalten: Ereignisname: nicht erhalten

      Zeitgrenze: nicht erhalten. Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

   6. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

      1. Eine Nachricht senden; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

      Kein Standardzweig eingestellt.

   7. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

      1. Einen Lüfter ausschalten — `fan.example_02`.

      **Zweig 2:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

      1. Ein Lüfterprofil auswählen — `fan.example_02`; Profil: nicht erhalten.

      **Wenn kein Zweig passt:**

      1. Ein Lüfterprofil auswählen — `fan.example_02`; Profil: nicht erhalten.

   **Zweig 2:** alle folgenden: Bedingungstyp nicht erhalten: Auslöser-Verweis: `ID_17`

   1. 2 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   2. Einen Lüfter einschalten — `fan.example_01`.

   3. Ein Lüfterprofil auswählen — `fan.example_01`; Profil: nicht erhalten.

   4. Diese Pfade parallel starten. Ihre Ausführungsreihenfolge ist nicht festgelegt.

      **Paralleler Pfad 1:**

      1. Aktionstyp nicht erhalten; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

      **Paralleler Pfad 2:**

      1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_04`; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

   5. Auf einen dieser Auslöser warten:

      - Auslösertyp nicht erhalten: `vacuum.example_05`; von Zustand: nicht erhalten
      - Auslösertyp nicht erhalten: `vacuum.example_05`; von Zustand: nicht erhalten
      - Auslösertyp nicht erhalten: Ereignisname: nicht erhalten

      Zeitgrenze: nicht erhalten. Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

   6. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

      1. Eine Nachricht senden; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

      Kein Standardzweig eingestellt.

   7. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

      1. Einen Lüfter ausschalten — `fan.example_01`.

      **Zweig 2:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

      1. Ein Lüfterprofil auswählen — `fan.example_01`; Profil: nicht erhalten.

      **Wenn kein Zweig passt:**

      1. Ein Lüfterprofil auswählen — `fan.example_01`; Profil: nicht erhalten.

   **Zweig 3:** alle folgenden: Bedingungstyp nicht erhalten: Auslöser-Verweis: `ID_18`

   1. 2 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   2. Einen Lüfter einschalten — `fan.example_03`.

   3. Ein Lüfterprofil auswählen — `fan.example_03`; Profil: nicht erhalten.

   4. Diese Pfade parallel starten. Ihre Ausführungsreihenfolge ist nicht festgelegt.

      **Paralleler Pfad 1:**

      1. Aktionstyp nicht erhalten; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

      **Paralleler Pfad 2:**

      1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_04`; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

   5. Auf einen dieser Auslöser warten:

      - Auslösertyp nicht erhalten: `vacuum.example_02`; von Zustand: nicht erhalten
      - Auslösertyp nicht erhalten: `vacuum.example_02`; von Zustand: nicht erhalten
      - Auslösertyp nicht erhalten: Ereignisname: nicht erhalten

      Zeitgrenze: nicht erhalten. Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

   6. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

      1. Eine Nachricht senden; Nachrichtentext: nicht erhalten; Nachrichtentitel: nicht erhalten.

      Kein Standardzweig eingestellt.

   7. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

      1. Einen Lüfter ausschalten — `fan.example_03`.

      **Zweig 2:** alle folgenden: Bedingungstyp nicht erhalten: Formel: nicht erhalten

      1. Ein Lüfterprofil auswählen — `fan.example_03`; Profil: nicht erhalten.

      **Wenn kein Zweig passt:**

      1. Ein Lüfterprofil auswählen — `fan.example_03`; Profil: nicht erhalten.

   Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`parallel`: Jeder neue Auslöser kann einen eigenen Durchlauf neben bereits laufenden Durchläufen starten. Grenze für laufende und wartende Durchläufe: 6.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Einen Lüfter oder Luftreiniger, den Home Assistant steuern kann.
- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
