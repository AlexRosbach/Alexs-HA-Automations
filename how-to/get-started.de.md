# Deine erste Automation mit Home Assistant

[English](get-started.md) · **Deutsch**

Eine Automation ist eine einfache Regel: **Wenn etwas passiert, soll Home Assistant etwas tun.** Zum Beispiel: Wenn eine von dir gewählte Uhrzeit erreicht ist, geht eine Lampe an.

Alex teilt Automationen aus seinem eigenen Home Assistant, um dir Ideen für deine Einrichtung zu geben. Aus den geteilten Dateien wurden echte Gerätenamen und private Angaben entfernt. Manche enthalten auch offene Auslöser, Bedingungen oder Formeln. Nimm die Idee, die dir gefällt, und baue sie mit deinen eigenen Einstellungen nach.

[Zurück zur Übersicht](../README.de.md#automation-catalogue)

## 1. Bereite ein Gerät zum Ausprobieren vor

Wähle zum Beispiel eine Lampe, die du in Home Assistant bereits manuell ein- und ausschalten kannst. Damit erkennst du sofort, ob deine neue Automation funktioniert.

Öffne dann die Beschreibung einer Vorlage. Achte auf diese drei Fragen:

| Frage | Beispiel |
| --- | --- |
| **Wann soll es losgehen?** | Zu einer von dir gewählten Uhrzeit. |
| **Muss vorher etwas stimmen?** | Für die erste Übung lassen wir diesen Teil leer. |
| **Was soll passieren?** | Die ausgewählte Lampe einschalten. |

In Home Assistant heißen diese Teile **Auslöser**, **Bedingung** und **Aktion**.

## 2. Erstelle die Automation über die Oberfläche

1. Öffne in Home Assistant **Einstellungen → Automatisierungen & Szenen**.
2. Wähle **Automatisierung erstellen → Neue Automatisierung**.
3. Füge einen **Auslöser** hinzu. Für diese Übung wählst du eine Uhrzeit, die ein paar Minuten in der Zukunft liegt.
4. Lass die **Bedingungen** für diese Übung leer.
5. Füge die Aktion **Licht einschalten** hinzu und wähle deine Testlampe als Ziel aus.
6. Speichere die Automation unter einem verständlichen Namen, etwa **„Testlampe zur gewählten Uhrzeit einschalten“**. Prüfe, dass sie aktiviert ist.

Damit hast du eine eigene kleine Automation erstellt. Du kannst danach weitere Schritte aus einer Vorlage ergänzen, etwa eine Wartezeit oder eine zweite Aktion. Füge sie einzeln hinzu und prüfe jeweils das Ergebnis.

Die Bezeichnungen können je nach Sprache und Home-Assistant-Version etwas abweichen. Die [offizielle Anleitung zum Automationseditor](https://www.home-assistant.io/docs/automation/editor/) zeigt die aktuellen Menüs.

## 3. Prüfe, ob der ganze Ablauf funktioniert

Schalte deine Testlampe zunächst aus. Warte dann auf die eingestellte Uhrzeit: Die Lampe sollte automatisch angehen.

Über das Menü **⋮ → Aktionen ausführen** kannst du die Aktionen auch direkt testen. Dabei werden der Auslöser und die Bedingungen am Anfang der Automation übersprungen. Bedingungen innerhalb der Aktionen gelten weiterhin. Dieser Knopf prüft deshalb nicht, ob deine Automation im Alltag im richtigen Moment startet.

Für den vollständigen Test löst du den eingestellten Auslöser tatsächlich aus. Wenn etwas nicht klappt, öffne die Automation und ihre **Spuren**. Dort zeigt Home Assistant Schritt für Schritt, was passiert ist. Die [offizielle Anleitung zum Testen](https://www.home-assistant.io/docs/automation/testing/) erklärt diese Ansicht.

Wenn du fertig geübt hast, passe die Uhrzeit an deinen gewünschten Ablauf an oder deaktiviere die Testautomation.

## Was bedeuten die Platzhalter in den Dateien?

Lesbare Beispielnamen wie `light.kitchen_ceiling` und `notify.mobile_app_phone` zeigen die Funktion eines Geräts. Das sind neutrale Beispiele: Wähle in deinem Home Assistant die passende eigene Entität. Normale Benachrichtigungstexte dürfen erhalten bleiben und von dir angepasst werden.

Einige ältere Dateien enthalten noch Platzhalter aus einem früheren Export. Sie markieren fehlende Informationen; aus dem Platzhalter lässt sich der ursprüngliche Text oder die Regel nicht zurückholen.

| Du siehst … | Das bedeutet … |
| --- | --- |
| `light.example_01` | Hier gehört die Kennung deiner eigenen Lampe hin. |
| `sensor.example_01` | Hier gehört die Kennung deines passenden Sensors hin. |
| `script.example_01` | Hier wird ein eigenes Skript aufgerufen. Dieses musst du bei dir auswählen oder selbst erstellen; es wird nicht mitgeliefert. |
| `input_boolean.example_01` | Hier wird ein virtueller Schalter verwendet. Solche Helfer müssen in deinem Home Assistant eingerichtet sein. |
| `DEVICE_01` oder `AREA_01` | Wähle dein eigenes Gerät oder deinen eigenen Bereich. |
| `REPLACE_WITH_YOUR_OWN_TEXT` | Hier fehlt ein Text oder eine Einstellung. Was benötigt wird, hängt von der Stelle ab. |
| `REPLACE_WITH_YOUR_OWN_SECRET` | Hier wird ein privater Zugangswert benötigt. Er gehört nur in deine lokale Einrichtung. |
| `value_template` mit einem Platzhalter | Hier fehlt eine Formel. Sie muss für deinen gewünschten Ablauf neu erstellt werden. |

Eine **Entität** ist eine einzelne Funktion oder ein einzelner Messwert in Home Assistant: etwa eine Lampe, ein Temperatursensor oder der Akkustand eines Geräts. Ihre Kennung heißt **Entitäts-ID**, zum Beispiel `light.example_01`.

Du findest deine eigenen Entitäten unter **Einstellungen → Geräte & Dienste → Entitäten**. Öffne den passenden Eintrag und seine Einstellungen, um die Entitäts-ID nachzusehen. Beim Nachbauen im visuellen Editor kannst du das Ziel direkt auswählen. Weitere Hinweise bietet die [offizielle Beschreibung zu Entitäten](https://www.home-assistant.io/docs/configuration/customizing-entities/).

## Wenn du lieber den YAML-Text anpassen möchtest

**YAML** ist die Textform einer Automation. In jedem Beispiel findest du sie in der Datei `automation.yaml`.

1. Öffne die Datei auf GitHub und kopiere ihren Inhalt.
2. Erstelle in Home Assistant eine **neue** Automation und öffne oben rechts **⋮ → In YAML bearbeiten**.
3. Füge den Inhalt dort ein. Ergänze alle fehlenden Auslöser, Bedingungen und Formeln und ersetze die Platzhalter durch deine eigenen Werte.
4. Speichere erst, wenn die Einstellungen vollständig sind, und teste den ganzen Ablauf wie oben beschrieben.

Wenn etwa hinter `trigger:` oder `condition:` noch `REPLACE_WITH_YOUR_OWN_TEXT` steht, fehlt ein Teil der Automationsregel. Nur die Gerätenamen auszutauschen reicht dann nicht. Nutze zum Einstieg die Oberfläche aus Schritt 2, um diesen Teil bewusst selbst festzulegen.

## Häufige Fragen

**Kann ich eine Datei unverändert übernehmen?**

Nein. Die Beispiele enthalten Platzhalter; manche enthalten zusätzlich unvollständige Regeln. Die Beschreibung hilft dir beim Nachbauen mit deinen Geräten.

**Warum gibt es mehrere ähnlich benannte Beispiele?**

Es gibt unterschiedliche Varianten eines ähnlichen Ablaufs. Öffne die Beschreibung und prüfe, welche Aktionen und Geräte du brauchst. Die Kennung am Ende mancher Ordnernamen dient nur der Unterscheidung.

**Bedeutet ein grüner GitHub-Haken, dass die Automation bei mir läuft?**

Der Haken zeigt, dass die Prüfungen dieser Sammlung bestanden sind, etwa auf private Angaben und eine passende Dokumentation. Ob deine Geräte, Auslöser und Bedingungen zusammenspielen, testest du in deinem Home Assistant.

**Was darf ich öffentlich teilen?**

Teile nur bereinigte Beispiele. Behalte Passwörter, Zugangstoken, private Adressen und deine ausgefüllte persönliche Konfiguration bei dir. Die [technischen Hinweise zum Datenschutz (Englisch)](security-and-privacy.md) erklären die Prüfungen für Beiträge zur Sammlung.
