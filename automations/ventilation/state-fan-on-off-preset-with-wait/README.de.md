# Lüfter ein- und ausschalten sowie einstellen · mit Wartebedingung im Ablauf

[English](README.md) · **Deutsch**

[Lüfter und Luftreiniger](../../../README.de.md#ventilation) → [Betriebsprofile auswählen](../../../README.de.md#ventilation-profiles)

[Alle Automationen ansehen](../../../README.de.md#automation-catalogue) · [Schritt für Schritt einrichten](../../../how-to/get-started.de.md)

Ein anonymisiertes Home-Assistant-Beispiel, als Anregung geteilt.

Dies ist eine anonymisierte Kopie. Ersetze die Platzhalter und ergänze fehlende Abläufe, bevor du sie bei dir verwendest.

## Was macht dieses Beispiel?

Den ersten passenden Zweig ausführen: Zwischenwerte vorbereiten → Einen Lüfter einschalten → 5 weitere Schritte / Zwischenwerte vorbereiten → Einen Lüfter einschalten → 5 weitere Schritte; 1 weiterer Zweig. Starteinstellungen: zu Zustand: `cleaning`.

## Wann startet sie?

Jeder aktivierte Auslöser unten kann einen Durchlauf starten.

- **1.** Zustandsänderung: `vacuum.example_06`; zu Zustand: `cleaning`; Auslöser-Verweis: nicht erhalten
- **2.** Zustandsänderung: `vacuum.example_05`; zu Zustand: `cleaning`; Auslöser-Verweis: nicht erhalten
- **3.** Zustandsänderung: `vacuum.example_02`; zu Zustand: `cleaning`; Auslöser-Verweis: nicht erhalten

## Was muss vorher erfüllt sein?

Es sind keine übergeordneten Bedingungen eingestellt. Prüfungen innerhalb der Schritte gelten weiterhin.

## Konkreter Ablauf

1. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

   **Zweig 1:** alle folgenden: Auslöser-Verweis prüfen: Auslöser-Verweis: nicht erhalten

   1. 2 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   2. Einen Lüfter einschalten — `fan.example_02`.

   3. Ein Lüfterprofil auswählen — `fan.example_02`; Profil: “turbo”.

   4. Diese Pfade parallel starten. Ihre Ausführungsreihenfolge ist nicht festgelegt.

      **Paralleler Pfad 1:**

      1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Büro: Roboter läuft, person ist bis person Ende person Reinigung auf Turbo.”; Nachrichtentitel: “person Turbo”.

      **Paralleler Pfad 2:**

      1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_02`; Nachrichtentext: “Büro: Roboter läuft, person ist bis person Ende person Reinigung auf Turbo.”; Nachrichtentitel: “person Turbo”.

   5. Auf einen dieser Auslöser warten:

      - Zustandsänderung: `vacuum.example_06`; von Zustand: `cleaning`
      - Zustandsänderung: `vacuum.example_06`; von Zustand: `returning`
      - Ereignis: Ereignisname: nicht erhalten

      Zeitgrenze: 04:00:00 (Zeitformat). Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

   6. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Formelprüfung: Formel: “\{\{ wait.trigger is not none and wait.trigger.platform == 'event' \}\}”

      1. Eine Nachricht senden; Nachrichtentext: “Büro: person-Automatik für diese Roboter-Reinigung wurde abgebrochen.”; Nachrichtentitel: “person-Steuerung gestoppt”.

      Kein Standardzweig eingestellt.

   7. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Formelprüfung: Formel: “\{\{ previous\_fan\_state == 'IDENTIFIER\_159' \}\}”

      1. Einen Lüfter ausschalten — `fan.example_02`.

      **Zweig 2:** alle folgenden: Formelprüfung: Formel: “\{\{ previous\_fan\_preset not in \[none, 'unknown', 'unavailable', ''\] \}\}”

      1. Ein Lüfterprofil auswählen — `fan.example_02`; Profil: “\{\{ previous\_fan\_preset \}\}”.

      **Wenn kein Zweig passt:**

      1. Ein Lüfterprofil auswählen — `fan.example_02`; Profil: “auto”.

   **Zweig 2:** alle folgenden: Auslöser-Verweis prüfen: Auslöser-Verweis: nicht erhalten

   1. 2 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   2. Einen Lüfter einschalten — `fan.example_01`.

   3. Ein Lüfterprofil auswählen — `fan.example_01`; Profil: “turbo”.

   4. Diese Pfade parallel starten. Ihre Ausführungsreihenfolge ist nicht festgelegt.

      **Paralleler Pfad 1:**

      1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Schlafzimmer: Roboter läuft, person ist bis person Ende person Reinigung auf Turbo.”; Nachrichtentitel: “person Turbo”.

      **Paralleler Pfad 2:**

      1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_02`; Nachrichtentext: “Schlafzimmer: Roboter läuft, person ist bis person Ende person Reinigung auf Turbo.”; Nachrichtentitel: “person Turbo”.

   5. Auf einen dieser Auslöser warten:

      - Zustandsänderung: `vacuum.example_05`; von Zustand: `cleaning`
      - Zustandsänderung: `vacuum.example_05`; von Zustand: `returning`
      - Ereignis: Ereignisname: nicht erhalten

      Zeitgrenze: 04:00:00 (Zeitformat). Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

   6. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Formelprüfung: Formel: “\{\{ wait.trigger is not none and wait.trigger.platform == 'event' \}\}”

      1. Eine Nachricht senden; Nachrichtentext: “Schlafzimmer: person-Automatik für diese Roboter-Reinigung wurde abgebrochen.”; Nachrichtentitel: “person-Steuerung gestoppt”.

      Kein Standardzweig eingestellt.

   7. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Formelprüfung: Formel: “\{\{ previous\_fan\_state == 'IDENTIFIER\_159' \}\}”

      1. Einen Lüfter ausschalten — `fan.example_01`.

      **Zweig 2:** alle folgenden: Formelprüfung: Formel: “\{\{ previous\_fan\_preset not in \[none, 'unknown', 'unavailable', ''\] \}\}”

      1. Ein Lüfterprofil auswählen — `fan.example_01`; Profil: “\{\{ previous\_fan\_preset \}\}”.

      **Wenn kein Zweig passt:**

      1. Ein Lüfterprofil auswählen — `fan.example_01`; Profil: “auto”.

   **Zweig 3:** alle folgenden: Auslöser-Verweis prüfen: Auslöser-Verweis: nicht erhalten

   1. 2 Zwischenwerte vorbereiten; ihre Inhalte/Formeln sind nicht beschrieben.

   2. Einen Lüfter einschalten — `fan.example_03`.

   3. Ein Lüfterprofil auswählen — `fan.example_03`; Profil: “turbo”.

   4. Diese Pfade parallel starten. Ihre Ausführungsreihenfolge ist nicht festgelegt.

      **Paralleler Pfad 1:**

      1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_01`; Nachrichtentext: “Wohnzimmer: Roboter läuft, person ist bis person Ende person Reinigung auf Turbo.”; Nachrichtentitel: “person Turbo”.

      **Paralleler Pfad 2:**

      1. Eine Nachricht an ein eigenes Ziel senden — `notify.example_02`; Nachrichtentext: “Wohnzimmer: Roboter läuft, person ist bis person Ende person Reinigung auf Turbo.”; Nachrichtentitel: “person Turbo”.

   5. Auf einen dieser Auslöser warten:

      - Zustandsänderung: `vacuum.example_02`; von Zustand: `cleaning`
      - Zustandsänderung: `vacuum.example_02`; von Zustand: `returning`
      - Ereignis: Ereignisname: nicht erhalten

      Zeitgrenze: 04:00:00 (Zeitformat). Bei Ablauf der Zeitgrenze mit dem nächsten Schritt fortfahren.

   6. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Formelprüfung: Formel: “\{\{ wait.trigger is not none and wait.trigger.platform == 'event' \}\}”

      1. Eine Nachricht senden; Nachrichtentext: “Wohnzimmer: person-Automatik für diese Roboter-Reinigung wurde abgebrochen.”; Nachrichtentitel: “person-Steuerung gestoppt”.

      Kein Standardzweig eingestellt.

   7. Den ersten passenden Zweig ausführen; spätere Zweige dieser Auswahl werden übersprungen.

      **Zweig 1:** alle folgenden: Formelprüfung: Formel: “\{\{ previous\_fan\_state == 'IDENTIFIER\_159' \}\}”

      1. Einen Lüfter ausschalten — `fan.example_03`.

      **Zweig 2:** alle folgenden: Formelprüfung: Formel: “\{\{ previous\_fan\_preset not in \[none, 'unknown', 'unavailable', ''\] \}\}”

      1. Ein Lüfterprofil auswählen — `fan.example_03`; Profil: “\{\{ previous\_fan\_preset \}\}”.

      **Wenn kein Zweig passt:**

      1. Ein Lüfterprofil auswählen — `fan.example_03`; Profil: “auto”.

   Kein Standardzweig eingestellt.

## Wenn sie erneut ausgelöst wird

`parallel`: Jeder neue Auslöser kann einen eigenen Durchlauf neben bereits laufenden Durchläufen starten. Grenze für laufende und wartende Durchläufe: 6.

Wiederholte Entitätsverweise verbinden in diesen Schritten dasselbe Gerät oder denselben Wert. Namen wie `sensor.example_01` sind Platzhalter; neutrale beschreibende Namen können ebenfalls erhalten sein. Als „nicht erhalten“ markierte Angaben lassen sich aus diesem Beispiel nicht wiederherstellen.

Verhalten erklärt: [Aktionsabläufe](https://www.home-assistant.io/docs/automation/building-blocks/) · [Warten und Zeitgrenzen](https://www.home-assistant.io/building-blocks/wait_template/) · [Ausführungsmodi](https://www.home-assistant.io/docs/automation/modes/).

## Was brauche ich?

Home Assistant und die folgenden Geräte oder Funktionen:

- Einen Lüfter oder Luftreiniger, den Home Assistant steuern kann.
- Die Geräte und die Aktion, die du selbst ergänzen möchtest.
- Ein eingerichtetes Benachrichtigungsziel, zum Beispiel die Home-Assistant-App.
- Einen Wert oder Zustand, dessen Änderung den Ablauf starten soll, zum Beispiel von einem Gerät, Sensor oder Helfer.

## Was muss ich anpassen?

1. Öffne das [YAML-Beispiel](automation.yaml) und folge der [Schritt-für-Schritt-Anleitung](../../../how-to/get-started.de.md).
2. Ersetze die Platzhalter durch deine Geräte, Ziele und gewünschten Einstellungen. Angaben wie `example_…` oder `REPLACE_…` sind noch keine fertige Konfiguration.
3. Ergänze fehlende Auslöser, Bedingungen und Formeln. Einige dieser Angaben wurden beim ursprünglichen Export entfernt. Nur die Gerätenamen auszutauschen reicht dann nicht.
4. Prüfe die fertige Automation in Home Assistant und teste sie zunächst manuell mit einem unkritischen Gerät.
5. Teste danach einen echten Start über den eingerichteten Auslöser. So prüfst du auch die Bedingungen und den vollständigen Ablauf.

Deine Zugangsdaten und die fertig angepasste persönliche Konfiguration bleiben bei dir.
