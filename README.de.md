# Alex’ Home-Assistant-Automationen

[English](README.md) · **Deutsch**

Hi, ich bin Alex. Hier teile ich **Automationen aus meinem eigenen Home Assistant**. Wenn du Ideen für dein Smart Home suchst, schau dich um und lass dich für deine eigenen Abläufe inspirieren.

Die Sammlung enthält zum Beispiel Automationen für Licht, Heizung, Saugroboter und Benachrichtigungen. Jede Beschreibung erklärt den konkreten Ablauf, die Einstellungen und Bedingungen, damit du meine Idee nachvollziehen und auf deine Geräte übertragen kannst. **Tür- und Schlosssteuerung ist von dieser öffentlichen Sammlung ausgeschlossen.**

**[Meine Automationen entdecken](#automation-catalogue)** · **[Neu bei Home Assistant? Hier starten](how-to/get-started.de.md)**

> **Zu den geteilten Dateien:** Ich habe private Angaben aus meiner Einrichtung entfernt und durch Platzhalter ersetzt. Manche Auslöser, Bedingungen und Formeln müssen ebenfalls ergänzt oder neu aufgebaut werden. Die Dateien zeigen die Ideen hinter meinen Automationen; zum Nutzen brauchst du deine eigenen Einstellungen.

## Neu bei Home Assistant? Fang hier an

Eine Automation besteht aus einer einfachen Idee:

> **Wenn** etwas passiert, **dann** soll Home Assistant etwas tun.
>
> Zum Beispiel: Wenn eine von dir gewählte Uhrzeit erreicht ist, schalte eine Lampe ein.

Mit der **[Schritt-für-Schritt-Anleitung](how-to/get-started.de.md)** baust du diese kleine Übung direkt in der Home-Assistant-Oberfläche. Anschließend kannst du sie mit Ideen aus meinen Automationen erweitern.

## Mach aus einer Idee deinen eigenen Ablauf

1. **Idee auswählen.** Öffne unten einen Bereich, zum Beispiel „Licht“, und wähle die passende Aufgabe, etwa „Einschalten“ oder „Ausschalten“.
2. **Beschreibung lesen.** Jede Automation erklärt die vorgesehene Aufgabe, den Auslöser und die Stellen, die du anpassen musst.
3. **Mit deinen Geräten nachbauen und testen.** Ergänze den Ablauf in Home Assistant und prüfe ihn zunächst mit einem einzelnen Gerät.

### Drei meiner Automationen zum Anschauen

| Das steckt in der geteilten Automation | Den konkreten Ablauf ansehen |
| --- | --- |
| Ein Zustand muss 30 Minuten bestehen; nach einer zusätzlichen Bedingung wird das Licht mit 15 Sekunden Übergang ausgeschaltet | [Ablauf zum Ausschalten des Lichts](automations/lighting/state-light-off-2689ab79/README.de.md) |
| Oberer Sensorgrenzwert 10, Schalter einschalten, auf einen Wert unter 5 mit maximal 60 Minuten Wartezeit warten, danach ausschalten | [Schalter mit zwei Grenzwerten](automations/switches/threshold-switch-on-off-with-wait/README.de.md) |
| Temperaturwerte 24 und 21 mit einer Wartezeit von bis zu 3 Stunden dazwischen, ergänzt um Licht-, Medien- und Helferaktionen | [Kombinierter Klimaablauf](automations/climate/state-climate-temperature-with-wait/README.de.md) |

Die Beschreibungen nennen Werte, die in den geteilten Dateien erhalten sind. Jede Seite zeigt auch, welche Auslöserdetails, Bedingungen oder Formeln beim früheren Export entfernt wurden. Fehlende Angaben werden nicht geraten; sie müssen aus der ursprünglichen Automation ergänzt oder für deine eigene Einrichtung festgelegt werden.

<a id="begriffe-kurz-erklaert"></a>

## Die wichtigsten Begriffe – kurz erklärt

| Begriff | Einfach erklärt |
| --- | --- |
| **Automation** | Ein Ablauf, den Home Assistant automatisch startet. |
| **Auslöser** | Der Startschuss: zum Beispiel eine Uhrzeit oder ein geänderter Sensorwert. |
| **Bedingung** | Eine zusätzliche Voraussetzung: zum Beispiel „nur wenn es dunkel ist“. |
| **Aktion** | Was passieren soll: zum Beispiel eine Lampe einschalten. |
| **Entität** | Eine einzelne Funktion oder ein Messwert, etwa eine Lampe oder ein Temperatursensor. |
| **Platzhalter** | Ein Beispielwert, den du durch deine eigene Einstellung ersetzt. |
| **YAML** | Die Textform der Einstellungen. In dieser Sammlung steht sie in `automation.yaml`. |

**Namen und Nachrichten:** Ursprüngliche Entitäts-IDs werden immer durch neutrale Platzhalter ersetzt. Normale Benachrichtigungstexte dürfen nur bleiben, wenn sie keine privaten Angaben enthalten; persönliche Namen, identifizierende Handymodelle und Zugangsdaten werden bereinigt. Bereits fehlende Texte lassen sich aus den geteilten Dateien nicht zurückholen.

**Welche Datei brauche ich?** Öffne zuerst die deutsche Beschreibung (`README.de.md`) eines Beispiels. `README.md` enthält dieselbe Anleitung auf Englisch. Die Datei `automation.yaml` enthält den Ablauf als Text; `metadata.json` wird für die automatische Übersicht verwendet.

<!-- catalogue:start -->

<a id="automation-catalogue"></a>

## Automationen im Überblick (126 Automationen)

Die geteilten Automationen sind in **11 Bereiche und 35 Unterbereiche** nach ihrer erkennbaren Funktion aufgeteilt.

Wähle unten einen Bereich und klappe ihn auf. Die Sprunglinks darin führen direkt zum gewünschten Unterbereich. Öffne anschließend ein Beispiel: Dort steht, was es macht und wie du es an dein Zuhause anpassen kannst.

Manche Abläufe gibt es in mehreren Varianten. Die Buchstaben helfen beim Unterscheiden; sie stehen für unterschiedliche Konfigurationen, nicht für bestimmte Räume oder Geräte.

| Bereich | Automationen | Unterbereiche |
| --- | ---: | --- |
| [Heizung und Raumklima](#climate) | 18 | Temperatur einstellen · Heiz- und Kühlmodus · Heiz- und Klimaprofile |
| [Licht](#lighting) | 29 | Einschalten · Ausschalten · Umschalten · Ein- und Ausschalten · Szenen |
| [Lüfter und Luftreiniger](#ventilation) | 4 | Ein- und Ausschalten · Geschwindigkeit einstellen · Betriebsprofile auswählen |
| [Saugroboter](#cleaning) | 8 | Starten · Saugleistung einstellen · Bestimmte Bereiche reinigen |
| [Musik, Medien und Kameras](#media) | 2 | Kamerabilder speichern · Kamerabild live anzeigen |
| [Aufgabenlisten und Erinnerungen](#tasks) | 13 | Aufgabenlisten abfragen · Einträge bearbeiten · Einträge entfernen |
| [Schalter und Steckdosen](#switches) | 15 | Einschalten · Ausschalten · Umschalten · Ein- und Ausschalten |
| [Sprache und Durchsagen](#voice) | 1 | Durchsagen und Vorlesen |
| [Nachrichten und Hinweise](#notifications) | 9 | Nachrichten versenden · Hinweise in Home Assistant |
| [Zähler und gespeicherte Werte](#helpers) | 5 | Virtuelle Schalter · Zähler verändern · Texte speichern |
| [Weitere Abläufe und Geräteaktionen](#system) | 22 | Eigene Skripte · MQTT-Nachrichten · Andere Automationen schalten · Wetterdaten abrufen · Wartung und Protokolle · Noch einzurichtende Aktionen |

<a id="climate"></a>

<details>
<summary><strong>Heizung und Raumklima</strong> · 18 Automationen</summary>

**Direkt zu:** [Temperatur einstellen (9)](#climate-temperature) · [Heiz- und Kühlmodus (4)](#climate-modes) · [Heiz- und Klimaprofile (5)](#climate-profiles)

<a id="climate-temperature"></a>

#### Temperatur einstellen (9 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf — Variante A](automations/climate/device-climate-temperature-with-branches-7e7eb3e2/README.de.md) | Wiederholen bis Bedingungen erfüllt sind: Temperatur auf 5 setzen; Heiz-/Kühlmodus: `off` → wiederholen bis Bedingungen erfüllt sind: Temperatur auf 5 setzen; Heiz-/Kühlmodus: `off` → wenn die eingestellten Bedingungen erfüllt sind: (Temperatur auf 21 setzen; Heiz-/Kühlmodus: `heat_cool`) → 1 weiterer Schritt (siehe Ablauf). Starteinstellungen: Geräteereignis. |
| [Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf — Variante B](automations/climate/device-climate-temperature-with-branches-8526ac3c/README.de.md) | Wiederholen bis Bedingungen erfüllt sind: Temperatur auf 5 setzen; Heiz-/Kühlmodus: `off` → wiederholen bis Bedingungen erfüllt sind: Temperatur auf 5 setzen; Heiz-/Kühlmodus: `off` → wenn die eingestellten Bedingungen erfüllt sind: (Temperatur auf 21 setzen; Heiz-/Kühlmodus: `heat_cool`) → 1 weiterer Schritt (siehe Ablauf). Starteinstellungen: Geräteereignis. |
| [Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf](automations/climate/mixed-climate-temperature-with-branches/README.de.md) | Bedingungen prüfen; bei falsch diesen Ablauf stoppen → wenn Zustand: `on`; 2 weitere Prüfungen: (Die gewünschte Raumtemperatur einstellen) → Einen gespeicherten Ein/Aus-Wert ausschalten. Starteinstellungen: um 18:00:00 / Home-Assistant-Ereignis; 2 weitere Auslöser in den Details. Vor den Aktionen werden Bedingungen geprüft. |
| [Die gewünschte Raumtemperatur einstellen · mit Wartebedingung im Ablauf — Variante A](automations/climate/mixed-climate-temperature-with-wait-7131e10a/README.de.md) | Zwischenwerte vorbereiten → den ersten passenden Zweig ausführen: Zwischenwerte vorbereiten → Einen Textwert speichern → 7 weitere Schritte / Zwischenwerte vorbereiten → Bedingungen prüfen; bei falsch diesen Ablauf stoppen → 6 weitere Schritte; 4 weitere Zweige. Starteinstellungen: von Zustand: `off`; zu Zustand: `on` / zu Zustand: `on`; Dauer 2 min; 4 weitere Auslöser in den Details. Vor den Aktionen werden Bedingungen geprüft. |
| [Die gewünschte Raumtemperatur einstellen · mit Wartebedingung im Ablauf — Variante B](automations/climate/mixed-climate-temperature-with-wait-96c66e3c/README.de.md) | Zwischenwerte vorbereiten → den ersten passenden Zweig ausführen: Zwischenwerte vorbereiten → Einen Textwert speichern → 8 weitere Schritte / Zwischenwerte vorbereiten → Bedingungen prüfen; bei falsch diesen Ablauf stoppen → 7 weitere Schritte; 4 weitere Zweige. Starteinstellungen: von Zustand: `off`; zu Zustand: `on` / zu Zustand: `on`; Dauer 2 min; 4 weitere Auslöser in den Details. Vor den Aktionen werden Bedingungen geprüft. |
| [Die gewünschte Raumtemperatur einstellen · mit Wartebedingung im Ablauf — Variante C](automations/climate/mixed-climate-temperature-with-wait-dc257811/README.de.md) | Zwischenwerte vorbereiten → den ersten passenden Zweig ausführen: Zwischenwerte vorbereiten → Einen Textwert speichern → 7 weitere Schritte / Zwischenwerte vorbereiten → Bedingungen prüfen; bei falsch diesen Ablauf stoppen → 6 weitere Schritte; 4 weitere Zweige. Starteinstellungen: von Zustand: `off`; zu Zustand: `on` / zu Zustand: `on`; Dauer 2 min; 4 weitere Auslöser in den Details. Vor den Aktionen werden Bedingungen geprüft. |
| [Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf — Variante A](automations/climate/scheduled-climate-temperature-with-branches-168b082a/README.de.md) | Einen Textwert speichern → wenn Zustand: `off`; 2 weitere Prüfungen: (Einen Textwert speichern → Einen Zahlenwert speichern → 2 weitere Schritte). Starteinstellungen: um 06:45:00. Vor den Aktionen werden Bedingungen geprüft. |
| [Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf — Variante B](automations/climate/scheduled-climate-temperature-with-branches-9653956b/README.de.md) | Wenn nach 22:00:00: (Temperatur auf 5 setzen); sonst: (Temperatur auf 20 setzen). Starteinstellungen: um 21:30:00 / um 08:00:00. |
| [Die gewünschte Raumtemperatur einstellen · mit Wartebedingung im Ablauf](automations/climate/state-climate-temperature-with-wait/README.de.md) | Temperatur auf 24 setzen; Heiz-/Kühlmodus: `heat` → warten auf von Zustand: `on`; zu Zustand: `off` (bis zu 3 h; bei Ablauf weiter) → Temperatur auf 21 setzen; Heiz-/Kühlmodus: `auto` (ausgewählte Schritte; 10 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `on`. |

<a id="climate-modes"></a>

#### Heiz- und Kühlmodus (4 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Heizung oder Klimaanlage einstellen · mit Bedingungen im Ablauf — Variante A](automations/climate/state-climate-mode-temperature-with-branches-1362a589/README.de.md) | Den ersten passenden Zweig ausführen: Temperatur auf 5 setzen → Den Heiz- oder Kühlbetrieb einstellen; Heiz-/Kühlmodus: `off` / Den Heiz- oder Kühlbetrieb einstellen; Heiz-/Kühlmodus: `heat_cool` → Temperatur auf 21 setzen. Starteinstellungen: zu Zustand: `on` / zu Zustand: `off`. |
| [Heizung oder Klimaanlage einstellen · mit Bedingungen im Ablauf — Variante B](automations/climate/state-climate-mode-temperature-with-branches-49dd9c68/README.de.md) | Den ersten passenden Zweig ausführen: Bedingungen prüfen; bei falsch diesen Ablauf stoppen → Temperatur auf 5 setzen → 1 weiterer Schritt / Bedingungen prüfen; bei falsch diesen Ablauf stoppen → Den Heiz- oder Kühlbetrieb einstellen; Heiz-/Kühlmodus: `heat_cool` → 1 weiterer Schritt. Starteinstellungen: zu Zustand: `on` / zu Zustand: `off`. |
| [Heizung oder Klimaanlage einstellen · mit Bedingungen im Ablauf — Variante C](automations/climate/state-climate-mode-temperature-with-branches-c150b970/README.de.md) | Den ersten passenden Zweig ausführen: Bedingungen prüfen; bei falsch diesen Ablauf stoppen → Temperatur auf 5 setzen → 1 weiterer Schritt / Den Heiz- oder Kühlbetrieb einstellen; Heiz-/Kühlmodus: `heat_cool` → Temperatur auf 21 setzen. Starteinstellungen: zu Zustand: `on`, `off`. |
| [Heizung oder Klimaanlage einstellen · mit Bedingungen im Ablauf — Variante D](automations/climate/state-climate-mode-temperature-with-branches-d74bbc99/README.de.md) | Den ersten passenden Zweig ausführen: Temperatur auf 5 setzen → Den Heiz- oder Kühlbetrieb einstellen; Heiz-/Kühlmodus: `off`; sonst: Den Heiz- oder Kühlbetrieb einstellen; Heiz-/Kühlmodus: `heat_cool` → Temperatur auf 21 setzen. Starteinstellungen: zu Zustand: `on`, `off`. Vor den Aktionen werden Bedingungen geprüft. |

<a id="climate-profiles"></a>

#### Heiz- und Klimaprofile (5 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante A](automations/climate/mixed-climate-mode-preset-temperature-with-wait-0e58eb87/README.de.md) | Den ersten passenden Zweig ausführen: wenn die eingestellten Bedingungen erfüllt sind: (Einen Textwert speichern) → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen; Profil: “Default”) → 2 weitere Schritte / Den Heiz- oder Kühlbetrieb einstellen → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen; Profil: “\{\{ variable\_61.p \}\}”) → 3 weitere Schritte (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `on`, `off` / Dauer 10 s; 3 weitere Auslöser in den Details. |
| [Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante B](automations/climate/mixed-climate-mode-preset-temperature-with-wait-21fde419/README.de.md) | Den ersten passenden Zweig ausführen: wenn die eingestellten Bedingungen erfüllt sind: (Einen Textwert speichern) → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen; Profil: “Default”) → 2 weitere Schritte / Den Heiz- oder Kühlbetrieb einstellen → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen; Profil: “\{\{ variable\_61.p \}\}”) → 3 weitere Schritte (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `on`, `off` / Dauer 10 s; 3 weitere Auslöser in den Details. |
| [Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante C](automations/climate/mixed-climate-mode-preset-temperature-with-wait-4cd824a5/README.de.md) | Den ersten passenden Zweig ausführen: wenn die eingestellten Bedingungen erfüllt sind: (Einen Textwert speichern) → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen; Profil: “Default”) → 2 weitere Schritte / Den Heiz- oder Kühlbetrieb einstellen → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen; Profil: “\{\{ variable\_61.p \}\}”) → 3 weitere Schritte (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `on`, `off` / Dauer 10 s; 3 weitere Auslöser in den Details. |
| [Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante D](automations/climate/mixed-climate-mode-preset-temperature-with-wait-740a14ea/README.de.md) | Den ersten passenden Zweig ausführen: wenn die eingestellten Bedingungen erfüllt sind: (Einen Textwert speichern) → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen; Profil: “Default”) → 2 weitere Schritte / Den Heiz- oder Kühlbetrieb einstellen → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen; Profil: “\{\{ variable\_61.p \}\}”) → 3 weitere Schritte (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `on`, `off` / Dauer 10 s; 3 weitere Auslöser in den Details. |
| [Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante E](automations/climate/mixed-climate-mode-preset-temperature-with-wait-a2a43d6f/README.de.md) | Den ersten passenden Zweig ausführen: wenn die eingestellten Bedingungen erfüllt sind: (Einen Textwert speichern) → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen; Profil: “Default”) → 2 weitere Schritte / Den Heiz- oder Kühlbetrieb einstellen → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen; Profil: “\{\{ variable\_61.p \}\}”) → 3 weitere Schritte (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `on`, `off` / Dauer 10 s; 3 weitere Auslöser in den Details. |


</details>

<a id="lighting"></a>

<details>
<summary><strong>Licht</strong> · 29 Automationen</summary>

**Direkt zu:** [Einschalten (2)](#lighting-on) · [Ausschalten (7)](#lighting-off) · [Umschalten (6)](#lighting-toggle) · [Ein- und Ausschalten (13)](#lighting-on-off) · [Szenen (1)](#lighting-scenes)

<a id="lighting-on"></a>

#### Einschalten (2 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Licht einschalten · mit Wartezeit im Ablauf](automations/lighting/state-light-on-with-delay/README.de.md) | Licht mit 5 % Helligkeit einschalten → wenn Zustand: `off`: (Einen Schalter einschalten → warten für 5 min → 1 weiterer Schritt). Starteinstellungen: von Zustand: `off`; zu Zustand: `on`. Vor den Aktionen werden Bedingungen geprüft. |
| [Licht einschalten · mit Wartebedingung im Ablauf](automations/lighting/state-light-on-with-wait/README.de.md) | Auf einen von 2 Auslösern warten (bis zu 5 min; bei Ablauf stoppen) → den ersten passenden Zweig ausführen: Licht mit 100 % Helligkeit einschalten; Übergang: 3 s; Farbwerte: 255, 255, 255 (ausgewählte Schritte; 2 weitere Aktionen ausgelassen). Starteinstellungen: von Zustand: `off`; zu Zustand: `on`. |

<a id="lighting-off"></a>

#### Ausschalten (7 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Licht ausschalten](automations/lighting/scheduled-light-off/README.de.md) | Licht ausschalten → Einen Schalter ausschalten → Einen Schalter ausschalten. Starteinstellungen: um 00:00:00. |
| [Licht ausschalten — Variante A](automations/lighting/state-light-off-2689ab79/README.de.md) | Licht ausschalten; Übergang: 15 s. Starteinstellungen: zu Zustand: `off`; Dauer 30 min. Vor den Aktionen werden Bedingungen geprüft. |
| [Licht ausschalten — Variante B](automations/lighting/state-light-off-b89a953e/README.de.md) | Licht ausschalten. Starteinstellungen: Zustandsänderung. |
| [Licht ausschalten · mit Wartebedingung im Ablauf — Variante A](automations/lighting/state-light-off-with-wait-2fed7c0d/README.de.md) | Warten für 30 min → auf einen von 2 Auslösern warten (bis zu 15 min; bei Ablauf weiter) (ausgewählte Schritte; 5 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `not_home`. |
| [Licht ausschalten · mit Wartebedingung im Ablauf — Variante B](automations/lighting/state-light-off-with-wait-4466c2cf/README.de.md) | Auf einen von 2 Auslösern warten (bis zu 15 min; bei Ablauf weiter) → Licht ausschalten (ausgewählte Schritte; 9 weitere Aktionen ausgelassen). Starteinstellungen: Dauer 30 min. Vor den Aktionen werden Bedingungen geprüft. |
| [Licht ausschalten · mit Wartebedingung im Ablauf — Variante C](automations/lighting/state-light-off-with-wait-5918e34f/README.de.md) | Auf einen von 11 Auslösern warten (bis zu 15 min; bei Ablauf weiter) (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `off`; Dauer 55 min. Vor den Aktionen werden Bedingungen geprüft. |
| [Licht ausschalten · mit Wartebedingung im Ablauf — Variante D](automations/lighting/state-light-off-with-wait-eea5f9f7/README.de.md) | Auf einen von 2 Auslösern warten (bis zu 15 min; bei Ablauf weiter) (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `off`; Dauer 55 min. Vor den Aktionen werden Bedingungen geprüft. |

<a id="lighting-toggle"></a>

#### Umschalten (6 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Licht zwischen Ein und Aus umschalten — Variante A](automations/lighting/device-light-toggle-18a63fca/README.de.md) | Licht zwischen Ein und Aus umschalten; Helligkeit: 76%. Starteinstellungen: Geräteereignis. |
| [Licht zwischen Ein und Aus umschalten — Variante B](automations/lighting/device-light-toggle-21f567de/README.de.md) | Licht zwischen Ein und Aus umschalten; Helligkeit: 76%; Übergang: 1 s. Starteinstellungen: Geräteereignis. |
| [Licht zwischen Ein und Aus umschalten — Variante C](automations/lighting/device-light-toggle-462e05e8/README.de.md) | Licht zwischen Ein und Aus umschalten; Helligkeit: 81%. Starteinstellungen: Geräteereignis. |
| [Licht zwischen Ein und Aus umschalten — Variante D](automations/lighting/device-light-toggle-4f78710c/README.de.md) | Licht zwischen Ein und Aus umschalten; Helligkeit: 76%; Übergang: 1 s. Starteinstellungen: Geräteereignis. |
| [Licht einschalten oder umschalten · mit Bedingungen im Ablauf](automations/lighting/state-light-on-toggle-with-branches/README.de.md) | Den ersten passenden Zweig ausführen: Licht einschalten; Helligkeitsänderung: 10% / Licht einschalten; Helligkeitsänderung: -10%; 1 weiterer Zweig. Starteinstellungen: Zustandsänderung. |
| [Licht zwischen Ein und Aus umschalten](automations/lighting/triggered-light-toggle/README.de.md) | Licht zwischen Ein und Aus umschalten; Helligkeit: 76%. |

<a id="lighting-on-off"></a>

#### Ein- und Ausschalten (13 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante A](automations/lighting/device-light-on-off-with-branches-66dd4021/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Licht ausschalten); sonst: (Licht mit 70 % Helligkeit einschalten). Starteinstellungen: Geräteereignis. |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante B](automations/lighting/device-light-on-off-with-branches-860faef0/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Licht ausschalten); sonst: (Licht mit 70 % Helligkeit einschalten). Starteinstellungen: Geräteereignis. |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante C](automations/lighting/device-light-on-off-with-branches-9071e735/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (den ersten passenden Zweig ausführen: Licht mit 86 % Helligkeit einschalten; Übergang: 1 s; Farbtemperatur: 4000 K → Ein eigenes Skript ausführen / Licht ausschalten; Übergang: 2 s → Ein eigenes Skript ausführen) → den ersten passenden Zweig ausführen: Einen Lüfter einschalten / Einen Lüfter ausschalten. Starteinstellungen: Geräteereignis. |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante D](automations/lighting/device-light-on-off-with-branches-a1b9296d/README.de.md) | Wenn unter 10: (Licht mit 5 % Helligkeit einschalten); sonst: (Licht ausschalten). Startgrenzen: unter 10 / über 10. |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante E](automations/lighting/device-light-on-off-with-branches-d6dc2cef/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Licht ausschalten); sonst: (Licht mit 70 % Helligkeit einschalten). Starteinstellungen: Geräteereignis. |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf](automations/lighting/mqtt-light-on-off-with-branches/README.de.md) | Den ersten passenden Zweig ausführen: Licht mit 76 % Helligkeit einschalten → Ein eigenes Skript ausführen → 2 weitere Schritte / wenn Zustand: `on`: (Ein vorhandenes Skript starten) → Ein eigenes Skript ausführen → 2 weitere Schritte. Starteinstellungen: MQTT-Nachricht. |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante A](automations/lighting/state-light-on-off-with-branches-140ac0ad/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Licht mit 70 % Helligkeit einschalten); sonst: (Licht ausschalten). Starteinstellungen: Zustandsänderung. |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante B](automations/lighting/state-light-on-off-with-branches-478eac65/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Licht mit 70 % Helligkeit einschalten → wenn Zustand: `on`: (Licht mit 100 % Helligkeit einschalten; Übergang: 3 s)); sonst: (Licht ausschalten → wenn Zustand: `on`: (Licht mit 10 % Helligkeit einschalten; Übergang: 30 s); sonst: (Licht ausschalten; Übergang: 5 s)). Starteinstellungen: Zustandsänderung. |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante C](automations/lighting/state-light-on-off-with-branches-6ba1b551/README.de.md) | Den ersten passenden Zweig ausführen: Einen Schalter einschalten → Licht einschalten / Einen Schalter ausschalten → wenn die eingestellten Bedingungen erfüllt sind: (Licht ausschalten). Starteinstellungen: von Zustand: `off`; zu Zustand: `on`; Dauer 1 min / zu Zustand: `off`; Dauer 5 min. Vor den Aktionen werden Bedingungen geprüft. |
| [Licht ein- und ausschalten · mit Wartebedingung im Ablauf — Variante A](automations/lighting/state-light-on-off-with-wait-de083b0a/README.de.md) | Auf einen von 2 Auslösern warten (bis zu 15 min; bei Ablauf stoppen) → den ersten passenden Zweig ausführen: wenn Zustand: `off`: (Einen Schalter einschalten) → Licht ausschalten; Übergang: 2 s → 4 weitere Schritte / Eine Nachricht an ein eigenes Ziel senden; Nachrichtentext: “Okay, ich mache nichts.”; Nachrichtentitel: “Filmmodus” → Eine Nachricht an ein eigenes Ziel senden; Nachrichtentext: “Okay, ich mache nichts.”; Nachrichtentitel: “Filmmodus” → 1 weiterer Schritt (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Starteinstellungen: von Zustand: `off`; zu Zustand: `on`; Dauer 10 s / von Zustand: `unavailable`; zu Zustand: `on`; Dauer 10 s. Vor den Aktionen werden Bedingungen geprüft. |
| [Licht ein- und ausschalten · mit Wartebedingung im Ablauf — Variante B](automations/lighting/state-light-on-off-with-wait-dff24f3d/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Licht mit 70 % Helligkeit einschalten → warten für 5 min → 2 weitere Schritte). Starteinstellungen: Zustandsänderung. |
| [Licht ein- und ausschalten · mit Wartebedingung im Ablauf](automations/lighting/template-light-on-off-with-wait/README.de.md) | Licht einschalten → auf eine Bedingung warten → Licht ausschalten (ausgewählte Schritte; 1 weitere Aktion ausgelassen). Starteinstellungen: Dauer 3 min. Vor den Aktionen werden Bedingungen geprüft. |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf](automations/lighting/triggered-light-on-off-with-branches/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Licht ausschalten); sonst: (Licht einschalten). |

<a id="lighting-scenes"></a>

#### Szenen (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Eine gespeicherte Szene aktivieren · mit Wartezeit im Ablauf](automations/lighting/device-scene-on-with-delay/README.de.md) | Warten für 1 s → Eine gespeicherte Szene aktivieren → warten für 52 s 700 ms (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). Starteinstellungen: Geräteereignis. |


</details>

<a id="ventilation"></a>

<details>
<summary><strong>Lüfter und Luftreiniger</strong> · 4 Automationen</summary>

**Direkt zu:** [Ein- und Ausschalten (1)](#ventilation-power) · [Geschwindigkeit einstellen (2)](#ventilation-speed) · [Betriebsprofile auswählen (1)](#ventilation-profiles)

<a id="ventilation-power"></a>

#### Ein- und Ausschalten (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Lüfter ein- und ausschalten · mit Bedingungen im Ablauf](automations/ventilation/scheduled-fan-on-off-with-branches/README.de.md) | Den ersten passenden Zweig ausführen: nach 03:00:00: Einen Lüfter einschalten / nach 03:30:00: Einen Lüfter ausschalten. Starteinstellungen: um 03:00:00 / um 03:30:00. |

<a id="ventilation-speed"></a>

#### Geschwindigkeit einstellen (2 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Lüfter einstellen](automations/ventilation/event-fan-on-speed/README.de.md) | Einen Lüfter einschalten → Lüftergeschwindigkeit auf 75 % setzen (ausgewählte Schritte; 2 weitere Aktionen ausgelassen). Starteinstellungen: Ereignis. |
| [Lüfter einstellen · mit Bedingungen im Ablauf](automations/ventilation/periodic-fan-on-speed-with-branches/README.de.md) | Zwischenwerte vorbereiten → 1 weiterer Schritt (siehe Ablauf). Starteinstellungen: Minuten: 0. Vor den Aktionen werden Bedingungen geprüft. |

<a id="ventilation-profiles"></a>

#### Betriebsprofile auswählen (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Lüfter ein- und ausschalten sowie einstellen · mit Wartebedingung im Ablauf](automations/ventilation/state-fan-on-off-preset-with-wait/README.de.md) | Den ersten passenden Zweig ausführen: Zwischenwerte vorbereiten → Einen Lüfter einschalten → 5 weitere Schritte / Zwischenwerte vorbereiten → Einen Lüfter einschalten → 5 weitere Schritte; 1 weiterer Zweig. Starteinstellungen: zu Zustand: `cleaning`. |


</details>

<a id="cleaning"></a>

<details>
<summary><strong>Saugroboter</strong> · 8 Automationen</summary>

**Direkt zu:** [Starten (5)](#cleaning-start) · [Saugleistung einstellen (2)](#cleaning-power) · [Bestimmte Bereiche reinigen (1)](#cleaning-areas)

<a id="cleaning-start"></a>

#### Starten (5 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Einen Saugroboter starten](automations/cleaning/mixed-vacuum-start/README.de.md) | Einen Saugroboter starten → Einen Zähler zurücksetzen. Starteinstellungen: über 2 / um 08:00:00; 1 weiterer Auslöser in den Details. Vor den Aktionen werden Bedingungen geprüft. |
| [Einen Saugroboter starten — Variante A](automations/cleaning/scheduled-vacuum-start-8bec92f6/README.de.md) | Eine Geräteoption auswählen; gewählte Option: “Silent” → Einen Saugroboter starten. Starteinstellungen: um 03:00:00. |
| [Einen Saugroboter starten — Variante B](automations/cleaning/scheduled-vacuum-start-dd1999b3/README.de.md) | Einen Saugroboter starten. Starteinstellungen: um 09:30:00. |
| [Einen Saugroboter starten · mit Bedingungen im Ablauf](automations/cleaning/state-vacuum-start-with-branches/README.de.md) | Wenn Zustand: `not_home`; 1 weitere Prüfung: (wenn Zustand: `off`: (Eine Nachricht senden; Nachrichtentext: “Keiner zuhause. Es wird sauber gemacht.”; Nachrichtentitel: “Staubsauger” → Einen gespeicherten Ein/Aus-Wert einschalten → 1 weiterer Schritt)). Starteinstellungen: Zustandsänderung. |
| [Einen Saugroboter starten · mit Wartezeit im Ablauf](automations/cleaning/state-vacuum-start-with-delay/README.de.md) | Warten für 3 s → Einen Saugroboter starten (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Starteinstellungen: Zustandsänderung. Vor den Aktionen werden Bedingungen geprüft. |

<a id="cleaning-power"></a>

#### Saugleistung einstellen (2 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Einen Saugroboter starten und die Saugleistung einstellen — Variante A](automations/cleaning/scheduled-vacuum-set-fan-speed-start-47446c20/README.de.md) | Die Saugleistung einstellen; Saug-/Geschwindigkeitsstufe: “max” → Einen Saugroboter starten. Starteinstellungen: um 09:30:00. |
| [Einen Saugroboter starten und die Saugleistung einstellen — Variante B](automations/cleaning/scheduled-vacuum-set-fan-speed-start-d5c5adae/README.de.md) | Die Saugleistung einstellen; Saug-/Geschwindigkeitsstufe: “20” → Einen Saugroboter starten. Starteinstellungen: um 13:00:00. Vor den Aktionen werden Bedingungen geprüft. |

<a id="cleaning-areas"></a>

#### Bestimmte Bereiche reinigen (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Einen ausgewählten Bereich saugen lassen](automations/cleaning/device-dreame-vacuum-vacuum-clean-segment/README.de.md) | Einen ausgewählten Bereich saugen lassen; Reinigungsdurchgänge: 1. Starteinstellungen: Geräteereignis. |


</details>

<a id="media"></a>

<details>
<summary><strong>Musik, Medien und Kameras</strong> · 2 Automationen</summary>

**Direkt zu:** [Kamerabilder speichern (1)](#media-snapshots) · [Kamerabild live anzeigen (1)](#media-camera-live)

<a id="media-snapshots"></a>

#### Kamerabilder speichern (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Ein Kamerabild speichern · mit Wartezeit im Ablauf](automations/media/state-camera-snapshot-with-delay/README.de.md) | Ein Kamerabild speichern → warten für 1 s (ausgewählte Schritte; 6 weitere Aktionen ausgelassen). Starteinstellungen: von Zustand: `off`; zu Zustand: `on`. |

<a id="media-camera-live"></a>

#### Kamerabild live anzeigen (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Medien und Kameras steuern · mit Wartezeit im Ablauf](automations/media/device-state-media-playback-play-stream-snapshot-with-delay/README.de.md) | Wenn Zustand: `off`: (Medien abspielen → warten für 2 s 500 ms → 1 weiterer Schritt) → Ein Kamerabild speichern → warten für 1 s (ausgewählte Schritte; 5 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `on` / Zustandsänderung; 1 weiterer Auslöser in den Details. |


</details>

<a id="tasks"></a>

<details>
<summary><strong>Aufgabenlisten und Erinnerungen</strong> · 13 Automationen</summary>

**Direkt zu:** [Aufgabenlisten abfragen (9)](#tasks-read) · [Einträge bearbeiten (3)](#tasks-edit) · [Einträge entfernen (1)](#tasks-remove)

<a id="tasks-read"></a>

#### Aufgabenlisten abfragen (9 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf](automations/tasks/device-todo-read-with-branches/README.de.md) | Eine Aufgabenliste abfragen; Aufgabenstatus: `needs_action` (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). Starteinstellungen: Geräteereignis. |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante A](automations/tasks/scheduled-todo-read-with-branches-614bee92/README.de.md) | Eine Aufgabenliste abfragen; Aufgabenstatus: `needs_action` → Zwischenwerte vorbereiten → wenn die eingestellten Bedingungen erfüllt sind: (Ein eigenes Skript ausführen). Starteinstellungen: um 06:00:00; Wochentage: `wed`. |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante B](automations/tasks/scheduled-todo-read-with-branches-9416b616/README.de.md) | Eine Aufgabenliste abfragen; Aufgabenstatus: `needs_action` → Zwischenwerte vorbereiten → wenn die eingestellten Bedingungen erfüllt sind: (Ein eigenes Skript ausführen). Starteinstellungen: um 06:00:00; Wochentage: `fri`, `mon`. |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante A](automations/tasks/state-todo-read-with-branches-1d409d5f/README.de.md) | Eine Aufgabenliste abfragen; Aufgabenstatus: `needs_action` (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Starteinstellungen: Zustandsänderung. Vor den Aktionen werden Bedingungen geprüft. |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante B](automations/tasks/state-todo-read-with-branches-20f42e51/README.de.md) | Eine Aufgabenliste abfragen; Aufgabenstatus: `needs_action` (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `unavailable`; Dauer 2 min. |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante C](automations/tasks/state-todo-read-with-branches-29774ed7/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Eine Nachricht senden; Nachrichtentext: “Geschirrspüler ist an \!”; Nachrichtentitel: “🍽️ Geschirrspüler”) → wenn die eingestellten Bedingungen erfüllt sind: (Eine Nachricht senden; Nachrichtentext: “Geschirrspüler ist IDENTIFIER\_104 \!”; Nachrichtentitel: “🍽️ Geschirrspüler” → Eine Aufgabenliste abfragen; Aufgabenstatus: `needs_action` → 2 weitere Schritte). Starteinstellungen: Zustandsänderung. |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante D](automations/tasks/state-todo-read-with-branches-2eb2b24e/README.de.md) | Eine Aufgabenliste abfragen; Aufgabenstatus: `needs_action` (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Starteinstellungen: Zustandsänderung. Vor den Aktionen werden Bedingungen geprüft. |
| [Eine Aufgabenliste abfragen · mit Wartezeit im Ablauf](automations/tasks/state-todo-read-with-delay/README.de.md) | Einen Zähler erhöhen → warten für 1 s → wenn über 20: (Eine Aufgabenliste abfragen; Aufgabenstatus: `needs_action` → Zwischenwerte vorbereiten → 5 weitere Schritte). Starteinstellungen: von Zustand: `off`; zu Zustand: `on`; Dauer 3 s. Vor den Aktionen werden Bedingungen geprüft. |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf](automations/tasks/threshold-state-todo-read-with-branches/README.de.md) | Den ersten passenden Zweig ausführen: Einen gespeicherten Ein/Aus-Wert einschalten / Einen gespeicherten Ein/Aus-Wert ausschalten → Eine Nachricht an ein eigenes Ziel senden; Nachrichtentext: “Die Waschmaschine ist IDENTIFIER\_104.”; Nachrichtentitel: “Waschmaschine” → 4 weitere Schritte. Starteinstellungen: über 10; Dauer 2 min / unter 5; Dauer 20 min; 1 weiterer Auslöser in den Details. |

<a id="tasks-edit"></a>

#### Einträge bearbeiten (3 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Eine Aufgabenliste lesen und bearbeiten · mit Bedingungen im Ablauf — Variante A](automations/tasks/periodic-todo-read-update-with-branches-9bf67b03/README.de.md) | Eine Aufgabenliste abfragen; Aufgabenstatus: `needs_action` → Zwischenwerte vorbereiten → wiederholen für jeden Listeneintrag: Zwischenwerte vorbereiten. Starteinstellungen: Stunden: /1. |
| [Eine Aufgabenliste lesen und bearbeiten · mit Bedingungen im Ablauf — Variante B](automations/tasks/periodic-todo-read-update-with-branches-b915c5b1/README.de.md) | Eine Aufgabenliste abfragen → Zwischenwerte vorbereiten → wiederholen für jeden Listeneintrag: Zwischenwerte vorbereiten. Starteinstellungen: Stunden: /1. |
| [Eine Aufgabenliste lesen und bearbeiten · mit Bedingungen im Ablauf](automations/tasks/startup-periodic-todo-read-update-with-branches/README.de.md) | Eine Aufgabenliste abfragen; Aufgabenstatus: `needs_action` → wiederholen für jeden Listeneintrag: Zwischenwerte vorbereiten. Starteinstellungen: Minuten: 0 / Home-Assistant-Ereignis. |

<a id="tasks-remove"></a>

#### Einträge entfernen (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Eine Aufgabenliste lesen und Einträge entfernen · mit Bedingungen im Ablauf](automations/tasks/periodic-todo-read-remove-with-branches/README.de.md) | Eine Aufgabenliste abfragen → wiederholen für jeden Listeneintrag: Zwischenwerte vorbereiten (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). Starteinstellungen: Stunden: /1. |


</details>

<a id="switches"></a>

<details>
<summary><strong>Schalter und Steckdosen</strong> · 15 Automationen</summary>

**Direkt zu:** [Einschalten (4)](#switches-on) · [Ausschalten (3)](#switches-off) · [Umschalten (4)](#switches-toggle) · [Ein- und Ausschalten (4)](#switches-on-off)

<a id="switches-on"></a>

#### Einschalten (4 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Einen Schalter einschalten · mit Wartezeit im Ablauf](automations/switches/mqtt-switch-on-with-delay/README.de.md) | Wenn Zustand: `off`: (Einen Schalter einschalten → warten für 10 s) → Bedingungen prüfen; bei falsch diesen Ablauf stoppen → Ein eigenes Skript ausführen. Starteinstellungen: MQTT-Nachricht. |
| [Einen Schalter einschalten](automations/switches/state-switch-on/README.de.md) | Einen Schalter einschalten → Ein eigenes Skript ausführen. Starteinstellungen: Dauer 15 s. Vor den Aktionen werden Bedingungen geprüft. |
| [Einen Schalter einschalten · mit Wartebedingung im Ablauf](automations/switches/state-template-switch-on-with-wait/README.de.md) | Den ersten passenden Zweig ausführen: Einen gespeicherten Ein/Aus-Wert einschalten / Einen gespeicherten Ein/Aus-Wert ausschalten → Bedingungen prüfen; bei falsch diesen Ablauf stoppen → 4 weitere Schritte. Starteinstellungen: Dauer 8 min / Dauer 20 s. |
| [Einen Schalter einschalten](automations/switches/template-switch-on/README.de.md) | Einen Schalter einschalten. Starteinstellungen: Dauer 5 min. |

<a id="switches-off"></a>

#### Ausschalten (3 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Einen Schalter ausschalten · mit Wartebedingung im Ablauf](automations/switches/state-switch-off-with-wait/README.de.md) | Warten auf einen Wert über 7.999 oder 5 weitere Auslöser (bis zu 1 min; bei Ablauf weiter) → wenn Zustand: `on`; Dauer 3 min; 6 weitere Prüfungen: (Einen Schalter ausschalten) (ausgewählte Schritte; 2 weitere Aktionen ausgelassen). Starteinstellungen: zu Zustand: `unavailable`; Dauer 1 min. Vor den Aktionen werden Bedingungen geprüft. |
| [Einen Schalter ausschalten](automations/switches/template-switch-off/README.de.md) | Einen Schalter ausschalten. Starteinstellungen: Dauer 10 min. |
| [Einen Schalter ausschalten · mit Wartebedingung im Ablauf](automations/switches/triggered-switch-off-with-wait/README.de.md) | Warten auf einen Wert unter 8 (bis zu 10 min; bei Ablauf weiter) → wenn die eingestellten Bedingungen erfüllt sind: (Einen Schalter ausschalten); sonst: (Einen Hinweis in Home Assistant anzeigen; Nachrichtentext: “Das sichere person wurde nicht bestätigt. person muss offline sein person die Steckdose 60 Sekunden IDENTIFIER\_25 …“; Nachrichtentitel: “person-Steckdose bleibt an”) (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Vor den Aktionen werden Bedingungen geprüft. |

<a id="switches-toggle"></a>

#### Umschalten (4 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Einen Schalter zwischen Ein und Aus umschalten](automations/switches/device-switch-toggle/README.de.md) | Einen Schalter zwischen Ein und Aus umschalten. Starteinstellungen: Geräteereignis. |
| [Einen Schalter zwischen Ein und Aus umschalten](automations/switches/state-switch-toggle/README.de.md) | Einen Schalter zwischen Ein und Aus umschalten. Starteinstellungen: Zustandsänderung. |
| [Einen Schalter zwischen Ein und Aus umschalten — Variante A](automations/switches/triggered-switch-toggle-8229bc4f/README.de.md) | Einen Schalter zwischen Ein und Aus umschalten. |
| [Einen Schalter zwischen Ein und Aus umschalten — Variante B](automations/switches/triggered-switch-toggle-bb01f12e/README.de.md) | Einen Schalter zwischen Ein und Aus umschalten. |

<a id="switches-on-off"></a>

#### Ein- und Ausschalten (4 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Schalter ein- und ausschalten · mit Wartebedingung im Ablauf](automations/switches/mixed-switch-on-off-with-wait/README.de.md) | 3 Pfade parallel ausführen. Starteinstellungen: Zustandsänderung / Home-Assistant-Ereignis; 1 weiterer Auslöser in den Details. Vor den Aktionen werden Bedingungen geprüft. |
| [Schalter ein- und ausschalten · mit Bedingungen im Ablauf](automations/switches/state-switch-on-off-with-branches/README.de.md) | Den ersten passenden Zweig ausführen: Zustand: `on`: Einen Schalter einschalten / Zustand: `off`: Einen Schalter ausschalten. Starteinstellungen: zu Zustand: `on` / zu Zustand: `off`; Dauer 5 min. |
| [Schalter ein- und ausschalten · mit Wartezeit im Ablauf](automations/switches/state-switch-on-off-with-delay/README.de.md) | Den ersten passenden Zweig ausführen: Zustand: `on`: Einen Schalter einschalten → warten für 3 min → 2 weitere Schritte / Zustand: `off`: Bedingungen prüfen; bei falsch diesen Ablauf stoppen → Einen Schalter ausschalten. Starteinstellungen: zu Zustand: `on` / zu Zustand: `off`; Dauer 5 min. |
| [Schalter ein- und ausschalten · mit Wartebedingung im Ablauf](automations/switches/threshold-switch-on-off-with-wait/README.de.md) | Einen Schalter einschalten → warten auf einen Wert unter 5 (bis zu 60 min; bei Ablauf weiter) → Einen Schalter ausschalten. Startgrenzen: über 10. |


</details>

<a id="voice"></a>

<details>
<summary><strong>Sprache und Durchsagen</strong> · 1 Automation</summary>

**Direkt zu:** [Durchsagen und Vorlesen (1)](#voice-announcements)

<a id="voice-announcements"></a>

#### Durchsagen und Vorlesen (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Durchsagen und Sprachausgabe nutzen](automations/voice/state-voice-announce-speak/README.de.md) | 7 Pfade parallel ausführen. Starteinstellungen: zu Zustand: `on`. |


</details>

<a id="notifications"></a>

<details>
<summary><strong>Nachrichten und Hinweise</strong> · 9 Automationen</summary>

**Direkt zu:** [Nachrichten versenden (7)](#notifications-messages) · [Hinweise in Home Assistant (2)](#notifications-ha-notices)

<a id="notifications-messages"></a>

#### Nachrichten versenden (7 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Nachrichten senden — Variante A](automations/notifications/device-notification-send-48543cff/README.de.md) | Eine Nachricht senden; Nachrichtentext: “🚪Pass wegen den person auf \!\!”; Nachrichtentitel: “Die Haustür ist länger als 5 Minuten variable\_62\!\!\!”. Starteinstellungen: Dauer 5 min. |
| [Nachrichten senden — Variante B](automations/notifications/device-notification-send-6646dca6/README.de.md) | Einen Zähler zurücksetzen → Ein eigenes Skript ausführen → Eine Nachricht senden; Nachrichtentext: “Windelzähler wurde zurückgesetzt. Ein To‑Do person Leeren des Windeleimers wurde erstellt.”; Nachrichtentitel: “Windelzähler”. Starteinstellungen: Geräteereignis. |
| [Nachrichten senden · mit Wartezeit im Ablauf](automations/notifications/device-notification-send-with-delay/README.de.md) | Wiederholen bis Bedingungen erfüllt sind: Eine Nachricht senden; Nachrichtentext: “Technickschrank hat keinen Strom”. Startgrenzen: unter 5. |
| [Nachrichten senden · mit Bedingungen im Ablauf](automations/notifications/startup-periodic-notification-send-with-branches/README.de.md) | Eine Wettervorhersage abrufen → Zwischenwerte vorbereiten → 1 weiterer Schritt (siehe Ablauf). Starteinstellungen: Minuten: 10 / Home-Assistant-Ereignis. Vor den Aktionen werden Bedingungen geprüft. |
| [Nachrichten senden — Variante A](automations/notifications/state-notification-send-92ff0651/README.de.md) | Zwischenwerte vorbereiten → Eine Nachricht an ein eigenes Ziel senden; Nachrichtentext: “In folgenden Räumen sind Fenster variable\_62: \{\{ variable\_17 \}\}”; Nachrichtentitel: “🌧️ Regenalarm · \{\{ variable\_16 \}\}” → Eine Nachricht an ein eigenes Ziel senden; Nachrichtentext: “In folgenden Räumen sind Fenster variable\_62: \{\{ variable\_17 \}\}”; Nachrichtentitel: “🌧️ Regenalarm · \{\{ variable\_16 \}\}”. Starteinstellungen: zu Zustand: `on`. Vor den Aktionen werden Bedingungen geprüft. |
| [Nachrichten senden — Variante B](automations/notifications/state-notification-send-f0c37163/README.de.md) | Eine Nachricht senden; Nachrichtentext: “person wurde aktiviert.”. Starteinstellungen: von Zustand: `off`; zu Zustand: `on`. |
| [Nachrichten senden](automations/notifications/state-scheduled-notification-send/README.de.md) | Einen Textwert speichern → Eine Nachricht an ein eigenes Ziel senden; Nachrichtentext: “Bitte die Restmülltonne person. Über die Aktion kannst du bestätigen.”; Nachrichtentitel: “Restmüll morgen” → Eine Nachricht an ein eigenes Ziel senden; Nachrichtentext: “Bitte die Restmülltonne person. Über die Aktion kannst du bestätigen.”; Nachrichtentitel: “Restmüll morgen”. Starteinstellungen: um 20:00:00 / zu Zustand: `on`. Vor den Aktionen werden Bedingungen geprüft. |

<a id="notifications-ha-notices"></a>

#### Hinweise in Home Assistant (2 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Nachrichten und Hinweise ausgeben — Variante A](automations/notifications/device-notifications-create-notify-4a36cf99/README.de.md) | Eine Nachricht senden; Nachrichtentext: “Büro Balkontür steht seit mehr als 5 Minuten variable\_62.” → Einen Hinweis in Home Assistant anzeigen; Nachrichtentext: “Die Balkontür im Büro steht seit über 5 Minuten variable\_62.”; Nachrichtentitel: “Balkontür variable\_62”. Starteinstellungen: Dauer 5 min. |
| [Nachrichten und Hinweise ausgeben — Variante B](automations/notifications/device-notifications-create-notify-50bbe8ed/README.de.md) | Eine Nachricht senden; Nachrichtentext: “🚪Pass wegen den person auf \!\!”; Nachrichtentitel: “Die Tür in person Küche ist seit 2 Minuten variable\_62 \!” → Einen Hinweis in Home Assistant anzeigen; Nachrichtentext: “Die Tür in person Küche ist seit 2 Minuten variable\_62\! Pass auf die person auf\!”; Nachrichtentitel: “Tür in person Küche variable\_62”. Starteinstellungen: Dauer 2 min. |


</details>

<a id="helpers"></a>

<details>
<summary><strong>Zähler und gespeicherte Werte</strong> · 5 Automationen</summary>

**Direkt zu:** [Virtuelle Schalter (3)](#helpers-switches) · [Zähler verändern (1)](#helpers-counters) · [Texte speichern (1)](#helpers-text)

<a id="helpers-switches"></a>

#### Virtuelle Schalter (3 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Einen gespeicherten Ein/Aus-Wert ausschalten](automations/helpers/scheduled-input-boolean-off/README.de.md) | Einen gespeicherten Ein/Aus-Wert ausschalten. Starteinstellungen: um 23:55:00. |
| [Gespeicherte Ein/Aus-Werte ändern · mit Bedingungen im Ablauf](automations/helpers/scheduled-input-boolean-on-off-with-branches/README.de.md) | Wenn nach 18:00:00: (Einen gespeicherten Ein/Aus-Wert einschalten); sonst: (Einen gespeicherten Ein/Aus-Wert ausschalten). Starteinstellungen: um 20:00:00 / um 08:00:00. |
| [Gespeicherte Ein/Aus-Werte ändern · mit Bedingungen im Ablauf](automations/helpers/state-scheduled-input-boolean-on-off-with-branches/README.de.md) | Den ersten passenden Zweig ausführen: Einen gespeicherten Ein/Aus-Wert einschalten / Einen gespeicherten Ein/Aus-Wert ausschalten. Starteinstellungen: von Zustand: `off`; zu Zustand: `on` / von Zustand: `on`; zu Zustand: `off`; 1 weiterer Auslöser in den Details. |

<a id="helpers-counters"></a>

#### Zähler verändern (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Einen Zähler erhöhen](automations/helpers/device-counter-increment/README.de.md) | Einen Zähler erhöhen. Starteinstellungen: Dauer 8 s. |

<a id="helpers-text"></a>

#### Texte speichern (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Einen Textwert speichern](automations/helpers/template-input-text-value/README.de.md) | Einen Textwert speichern. Starteinstellungen: Dauer 3 min. Vor den Aktionen werden Bedingungen geprüft. |


</details>

<a id="system"></a>

<details>
<summary><strong>Weitere Abläufe und Geräteaktionen</strong> · 22 Automationen</summary>

**Direkt zu:** [Eigene Skripte (5)](#system-scripts) · [MQTT-Nachrichten (3)](#system-mqtt) · [Andere Automationen schalten (1)](#system-automations) · [Wetterdaten abrufen (1)](#system-weather) · [Wartung und Protokolle (1)](#system-maintenance) · [Noch einzurichtende Aktionen (11)](#system-unfinished)

<a id="system-scripts"></a>

#### Eigene Skripte (5 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Ein vorhandenes Skript ausführen](automations/system/event-script-run/README.de.md) | Ein eigenes Skript ausführen. Starteinstellungen: Ereignis. Vor den Aktionen werden Bedingungen geprüft. |
| [Ein vorhandenes Skript ausführen · mit Bedingungen im Ablauf](automations/system/mqtt-script-on-with-branches/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Ein vorhandenes Skript starten); sonst: (Ein vorhandenes Skript starten). Starteinstellungen: MQTT-Nachricht. |
| [Ein vorhandenes Skript ausführen](automations/system/mqtt-script-run/README.de.md) | Ein eigenes Skript ausführen. Starteinstellungen: MQTT-Nachricht. |
| [Ein vorhandenes Skript ausführen](automations/system/startup-periodic-script-run/README.de.md) | Ein eigenes Skript ausführen. Starteinstellungen: Minuten: 15 / Home-Assistant-Ereignis. |
| [Ein vorhandenes Skript ausführen](automations/system/state-scheduled-script-run/README.de.md) | Wiederholen für jeden Listeneintrag: Bedingungen prüfen; bei falsch diesen Ablauf stoppen. Starteinstellungen: um 10:00:00 / Zustandsänderung. |

<a id="system-mqtt"></a>

#### MQTT-Nachrichten (3 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Eine MQTT-Nachricht senden](automations/system/periodic-mqtt-publish/README.de.md) | Eine MQTT-Nachricht senden. Starteinstellungen: Minuten: /30. |
| [Eine MQTT-Nachricht senden](automations/system/startup-state-mqtt-publish/README.de.md) | Eine MQTT-Nachricht senden. Starteinstellungen: Zustandsänderung / Home-Assistant-Ereignis. |
| [Eine MQTT-Nachricht senden](automations/system/state-mqtt-publish/README.de.md) | Eine MQTT-Nachricht senden. Starteinstellungen: Zustandsänderung. Vor den Aktionen werden Bedingungen geprüft. |

<a id="system-automations"></a>

#### Andere Automationen schalten (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Andere Automationen aktivieren und deaktivieren · mit Wartezeit im Ablauf](automations/system/device-automation-on-off-with-delay/README.de.md) | Geräteaktion: `turn_off` → Eine andere Automation aktivieren → Eine andere Automation deaktivieren → 2 weitere Schritte (siehe Ablauf). Starteinstellungen: Geräteereignis. |

<a id="system-weather"></a>

#### Wetterdaten abrufen (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Mehrere Funktionen verbinden · mit Wartezeit im Ablauf](automations/system/state-periodic-system-custom-action-get-forecasts-with-delay/README.de.md) | Eine Wettervorhersage abrufen → Bedingungen prüfen; bei falsch diesen Ablauf stoppen → Zwischenwerte vorbereiten → 3 weitere Schritte (siehe Ablauf). Starteinstellungen: zu Zustand: `on`; Dauer 30 s / Dauer 30 s; 1 weiterer Auslöser in den Details. Vor den Aktionen werden Bedingungen geprüft. |

<a id="system-maintenance"></a>

#### Wartung und Protokolle (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Mehrere Funktionen verbinden](automations/system/periodic-system-reload-config-entry-write/README.de.md) | Einen Eintrag ins Systemprotokoll schreiben; Protokollstufe: `warning`; Nachrichtentext: “person Realtime hängt, lade Integration person. Letztes Update person sensor.example\_09: \{\{ states.sensor.exampl…“ → Eine Geräteanbindung neu laden. Starteinstellungen: Minuten: /10. Vor den Aktionen werden Bedingungen geprüft. |

<a id="system-unfinished"></a>

#### Noch einzurichtende Aktionen (11 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Eigene Aktion einrichten — Variante A](automations/system/device-generic-action-07b7476f/README.de.md) | Aktionstyp nicht erhalten. Starteinstellungen: Geräteereignis. |
| [Eigene Aktion einrichten — Variante B](automations/system/device-generic-action-2e3d4aa8/README.de.md) | Aktionstyp nicht erhalten. Starteinstellungen: Geräteereignis. Vor den Aktionen werden Bedingungen geprüft. |
| [Eigene Aktion einrichten — Variante C](automations/system/device-generic-action-384c7903/README.de.md) | Aktionstyp nicht erhalten. Starteinstellungen: Geräteereignis. Vor den Aktionen werden Bedingungen geprüft. |
| [Eigene Aktion einrichten — Variante D](automations/system/device-generic-action-f0b83fa0/README.de.md) | Aktionstyp nicht erhalten. Starteinstellungen: Geräteereignis. |
| [Eigene Aktion einrichten · mit Bedingungen im Ablauf](automations/system/device-generic-action-with-branches/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Geräteaktion: `turn_on` → Geräteaktion: `turn_on`); sonst: (Geräteaktion: `turn_off` → Geräteaktion: `turn_off`). Starteinstellungen: Geräteereignis. |
| [Eigene Aktion einrichten · mit Wartebedingung im Ablauf — Variante A](automations/system/device-generic-action-with-wait-1b7f707c/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (wenn unter 10: (Geräteaktion: `turn_on` → warten auf von Zustand: `on`; zu Zustand: `off` (bis zu 1 min; bei Ablauf weiter) → 1 weiterer Schritt)). Starteinstellungen: Geräteereignis. |
| [Eigene Aktion einrichten · mit Wartebedingung im Ablauf — Variante B](automations/system/device-generic-action-with-wait-9cf7bd31/README.de.md) | Geräteaktion: `turn_on` → warten auf einen Wert unter 60 → Geräteaktion: `turn_off`. Startgrenzen: über 60. |
| [Mehrere Funktionen verbinden · mit Bedingungen im Ablauf](automations/system/mqtt-system-action-custom-action-with-branches/README.de.md) | Den ersten passenden Zweig ausführen: Aktionstyp nicht erhalten; sonst: Ein eigenes Skript ausführen. Starteinstellungen: MQTT-Nachricht. |
| [Eigene Aktion einrichten · mit Bedingungen im Ablauf](automations/system/periodic-generic-action-with-branches/README.de.md) | Wenn unter 0.2: (Aktionstyp nicht erhalten); sonst: (Aktionstyp nicht erhalten). Starteinstellungen: Minuten: 10. |
| [Eigene Aktion einrichten](automations/system/state-generic-action/README.de.md) | Aktionstyp nicht erhalten. Starteinstellungen: Zustandsänderung. |
| [Eigene Aktion einrichten](automations/system/triggered-generic-action/README.de.md) | Blueprint-Logik liegt außerhalb der Datei. |


</details>

<!-- catalogue:end -->

## Fragen beim Einrichten?

In der **[Anleitung für den Einstieg](how-to/get-started.de.md)** findest du die Menüpunkte in Home Assistant, eine Erklärung der Platzhalter und Hilfe beim Testen.

Ein grüner GitHub-Haken bestätigt die Prüfungen dieser Sammlung. Ob eine angepasste Vorlage mit deinen Geräten funktioniert, prüfst du in deinem Home Assistant.

<details>
<summary><strong>Für Mitwirkende: Dokumentation und Prüfungen pflegen</strong></summary>

Die englische und die deutsche Übersicht sowie die Beschreibungen werden gemeinsam automatisch erzeugt. Die technischen Ordnernamen bleiben stabil; die Texte für Leser werden aus geprüften, allgemeinen Angaben erstellt.

```sh
python -m pip install -r requirements-dev.txt
python scripts/catalogue.py --write
python scripts/catalogue.py --check
```

- [Eine Vorlage dokumentieren (Englisch)](how-to/document-an-automation.md)
- [Datenschutz und Sicherheitsprüfungen (Englisch)](how-to/security-and-privacy.md)
- [Checkliste für automatisierte Beiträge (Englisch)](how-to/agent-documentation-checklist.md)

Die GitHub-Prüfungen laufen bei jedem neuen oder wieder geöffneten Pull Request, bei neuen Commits, beim Wechsel zwischen Entwurf und Review sowie bei Änderungen an Titel, Beschreibung oder Zielbranch.

</details>
