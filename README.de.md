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
| Ein Zustand muss 30 Minuten bestehen; nach einer zusätzlichen Bedingung wird das Licht mit 15 Sekunden Übergang ausgeschaltet | [Ablauf zum Ausschalten des Lichts](automations/lighting/state-light-off-22ac0c06/README.de.md) |
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

**Namen und Nachrichten:** Verständliche, neutrale Entitätsnamen und normale Benachrichtigungstexte dürfen bleiben. Persönliche Namen, identifizierende Handymodelle und Zugangsdaten werden bereinigt. Bereits fehlende Texte lassen sich aus den geteilten Dateien nicht zurückholen.

**Welche Datei brauche ich?** Öffne zuerst die deutsche Beschreibung (`README.de.md`) eines Beispiels. `README.md` enthält dieselbe Anleitung auf Englisch. Die Datei `automation.yaml` enthält den Ablauf als Text; `metadata.json` wird für die automatische Übersicht verwendet.

<!-- catalogue:start -->

<a id="automation-catalogue"></a>

## Automationen im Überblick (131 Automationen)

Die geteilten Automationen sind in **11 Bereiche und 36 Unterbereiche** nach ihrer erkennbaren Funktion aufgeteilt.

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
| [Schalter und Steckdosen](#switches) | 16 | Einschalten · Ausschalten · Umschalten · Ein- und Ausschalten |
| [Sprache und Durchsagen](#voice) | 1 | Durchsagen und Vorlesen |
| [Nachrichten und Hinweise](#notifications) | 11 | Nachrichten versenden · Hinweise in Home Assistant |
| [Zähler und gespeicherte Werte](#helpers) | 6 | Virtuelle Schalter · Zähler verändern · Texte speichern |
| [Weitere Abläufe und Geräteaktionen](#system) | 23 | Eigene Skripte · Gerätefunktionen und Tasten · MQTT-Nachrichten · Andere Automationen schalten · Wetterdaten abrufen · Wartung und Protokolle · Noch einzurichtende Aktionen |

<a id="climate"></a>

<details>
<summary><strong>Heizung und Raumklima</strong> · 18 Automationen</summary>

**Direkt zu:** [Temperatur einstellen (9)](#climate-temperature) · [Heiz- und Kühlmodus (4)](#climate-modes) · [Heiz- und Klimaprofile (5)](#climate-profiles)

<a id="climate-temperature"></a>

#### Temperatur einstellen (9 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf — Variante A](automations/climate/device-climate-temperature-with-branches-54a60709/README.de.md) | Wiederholen bis Bedingungen erfüllt sind: Temperatur auf 5 setzen → wiederholen bis Bedingungen erfüllt sind: Temperatur auf 5 setzen → wenn die eingestellten Bedingungen erfüllt sind: (Temperatur auf 21 setzen) → 1 weiterer Schritt (siehe Ablauf). |
| [Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf — Variante B](automations/climate/device-climate-temperature-with-branches-c104c302/README.de.md) | Wiederholen bis Bedingungen erfüllt sind: Temperatur auf 5 setzen → wiederholen bis Bedingungen erfüllt sind: Temperatur auf 5 setzen → wenn die eingestellten Bedingungen erfüllt sind: (Temperatur auf 21 setzen) → 1 weiterer Schritt (siehe Ablauf). |
| [Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf](automations/climate/mixed-climate-temperature-with-branches/README.de.md) | Bedingungen prüfen; bei falsch diesen Ablauf stoppen → wenn die eingestellten Bedingungen erfüllt sind: (Die gewünschte Raumtemperatur einstellen) → Einen gespeicherten Ein/Aus-Wert ausschalten. Vor den Aktionen werden Bedingungen geprüft. |
| [Die gewünschte Raumtemperatur einstellen · mit Wartebedingung im Ablauf — Variante A](automations/climate/mixed-climate-temperature-with-wait-a3321799/README.de.md) | Zwischenwerte vorbereiten → den ersten passenden Zweig ausführen: Zwischenwerte vorbereiten → Einen Textwert speichern → 7 weitere Schritte / Zwischenwerte vorbereiten → Bedingungen prüfen; bei falsch diesen Ablauf stoppen → 6 weitere Schritte; 4 weitere Zweige. Vor den Aktionen werden Bedingungen geprüft. |
| [Die gewünschte Raumtemperatur einstellen · mit Wartebedingung im Ablauf — Variante B](automations/climate/mixed-climate-temperature-with-wait-f1451717/README.de.md) | Zwischenwerte vorbereiten → den ersten passenden Zweig ausführen: Zwischenwerte vorbereiten → Einen Textwert speichern → 8 weitere Schritte / Zwischenwerte vorbereiten → Bedingungen prüfen; bei falsch diesen Ablauf stoppen → 7 weitere Schritte; 4 weitere Zweige. Vor den Aktionen werden Bedingungen geprüft. |
| [Die gewünschte Raumtemperatur einstellen · mit Wartebedingung im Ablauf — Variante C](automations/climate/mixed-climate-temperature-with-wait-fc1f1012/README.de.md) | Zwischenwerte vorbereiten → den ersten passenden Zweig ausführen: Zwischenwerte vorbereiten → Einen Textwert speichern → 7 weitere Schritte / Zwischenwerte vorbereiten → Bedingungen prüfen; bei falsch diesen Ablauf stoppen → 6 weitere Schritte; 4 weitere Zweige. Vor den Aktionen werden Bedingungen geprüft. |
| [Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf — Variante A](automations/climate/scheduled-climate-temperature-with-branches-47c2e215/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Temperatur auf 5 setzen); sonst: (Temperatur auf 20 setzen). |
| [Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf — Variante B](automations/climate/scheduled-climate-temperature-with-branches-5aaa8edc/README.de.md) | Einen Textwert speichern → wenn die eingestellten Bedingungen erfüllt sind: (Einen Textwert speichern → Einen Zahlenwert speichern → 2 weitere Schritte). Vor den Aktionen werden Bedingungen geprüft. |
| [Die gewünschte Raumtemperatur einstellen · mit Wartebedingung im Ablauf](automations/climate/state-climate-temperature-with-wait/README.de.md) | Temperatur auf 24 setzen → auf einen weiteren Auslöser warten (bis zu 3 h; bei Ablauf weiter) → Temperatur auf 21 setzen (ausgewählte Schritte; 10 weitere Aktionen ausgelassen). |

<a id="climate-modes"></a>

#### Heiz- und Kühlmodus (4 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Heizung oder Klimaanlage einstellen · mit Bedingungen im Ablauf — Variante A](automations/climate/state-climate-mode-temperature-with-branches-049416bb/README.de.md) | Den ersten passenden Zweig ausführen: Bedingungen prüfen; bei falsch diesen Ablauf stoppen → Temperatur auf 5 setzen → 1 weiterer Schritt / Den Heiz- oder Kühlbetrieb einstellen → Temperatur auf 21 setzen. |
| [Heizung oder Klimaanlage einstellen · mit Bedingungen im Ablauf — Variante B](automations/climate/state-climate-mode-temperature-with-branches-104d0276/README.de.md) | Den ersten passenden Zweig ausführen: Bedingungen prüfen; bei falsch diesen Ablauf stoppen → Temperatur auf 5 setzen → 1 weiterer Schritt / Bedingungen prüfen; bei falsch diesen Ablauf stoppen → Den Heiz- oder Kühlbetrieb einstellen → 1 weiterer Schritt. |
| [Heizung oder Klimaanlage einstellen · mit Bedingungen im Ablauf — Variante C](automations/climate/state-climate-mode-temperature-with-branches-6016b2ee/README.de.md) | Den ersten passenden Zweig ausführen: Temperatur auf 5 setzen → Den Heiz- oder Kühlbetrieb einstellen; sonst: Den Heiz- oder Kühlbetrieb einstellen → Temperatur auf 21 setzen. Vor den Aktionen werden Bedingungen geprüft. |
| [Heizung oder Klimaanlage einstellen · mit Bedingungen im Ablauf — Variante D](automations/climate/state-climate-mode-temperature-with-branches-75cb761b/README.de.md) | Den ersten passenden Zweig ausführen: Temperatur auf 5 setzen → Den Heiz- oder Kühlbetrieb einstellen / Den Heiz- oder Kühlbetrieb einstellen → Temperatur auf 21 setzen. |

<a id="climate-profiles"></a>

#### Heiz- und Klimaprofile (5 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante A](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-3b582a19/README.de.md) | Den ersten passenden Zweig ausführen: wenn die eingestellten Bedingungen erfüllt sind: (Einen Textwert speichern) → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen) → 2 weitere Schritte / Den Heiz- oder Kühlbetrieb einstellen → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen) → 3 weitere Schritte (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). |
| [Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante B](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-6037647c/README.de.md) | Den ersten passenden Zweig ausführen: wenn die eingestellten Bedingungen erfüllt sind: (Einen Textwert speichern) → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen) → 2 weitere Schritte / Den Heiz- oder Kühlbetrieb einstellen → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen) → 3 weitere Schritte (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). |
| [Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante C](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-b8c21183/README.de.md) | Den ersten passenden Zweig ausführen: wenn die eingestellten Bedingungen erfüllt sind: (Einen Textwert speichern) → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen) → 2 weitere Schritte / Den Heiz- oder Kühlbetrieb einstellen → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen) → 3 weitere Schritte (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). |
| [Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante D](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-d46bf28e/README.de.md) | Den ersten passenden Zweig ausführen: wenn die eingestellten Bedingungen erfüllt sind: (Einen Textwert speichern) → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen) → 2 weitere Schritte / Den Heiz- oder Kühlbetrieb einstellen → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen) → 3 weitere Schritte (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). |
| [Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante E](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-f9d2161c/README.de.md) | Den ersten passenden Zweig ausführen: wenn die eingestellten Bedingungen erfüllt sind: (Einen Textwert speichern) → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen) → 2 weitere Schritte / Den Heiz- oder Kühlbetrieb einstellen → wenn die eingestellten Bedingungen erfüllt sind: (Ein Heiz- oder Klimaprofil auswählen) → 3 weitere Schritte (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). |


</details>

<a id="lighting"></a>

<details>
<summary><strong>Licht</strong> · 29 Automationen</summary>

**Direkt zu:** [Einschalten (2)](#lighting-on) · [Ausschalten (7)](#lighting-off) · [Umschalten (6)](#lighting-toggle) · [Ein- und Ausschalten (13)](#lighting-on-off) · [Szenen (1)](#lighting-scenes)

<a id="lighting-on"></a>

#### Einschalten (2 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Licht einschalten · mit Wartezeit im Ablauf](automations/lighting/state-light-on-with-delay/README.de.md) | Licht mit 5 % Helligkeit einschalten → wenn die eingestellten Bedingungen erfüllt sind: (Einen Schalter einschalten → warten für 5 min → 1 weiterer Schritt). Vor den Aktionen werden Bedingungen geprüft. |
| [Licht einschalten · mit Wartebedingung im Ablauf](automations/lighting/state-light-on-with-wait/README.de.md) | Auf einen von 2 Auslösern warten (bei Ablauf stoppen) → den ersten passenden Zweig ausführen: Licht mit 100 % Helligkeit einschalten; Übergang: 3 s (ausgewählte Schritte; 2 weitere Aktionen ausgelassen). |

<a id="lighting-off"></a>

#### Ausschalten (7 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Licht ausschalten](automations/lighting/scheduled-light-off/README.de.md) | Licht ausschalten → Einen Schalter ausschalten → Einen Schalter ausschalten. |
| [Licht ausschalten — Variante A](automations/lighting/state-light-off-22ac0c06/README.de.md) | Licht ausschalten; Übergang: 15 s. Starteinstellungen: Dauer 30 min. Vor den Aktionen werden Bedingungen geprüft. |
| [Licht ausschalten — Variante B](automations/lighting/state-light-off-7cb13cdd/README.de.md) | Licht ausschalten. |
| [Licht ausschalten · mit Wartebedingung im Ablauf — Variante A](automations/lighting/state-light-off-with-wait-4dccd971/README.de.md) | Auf einen von 11 Auslösern warten (bei Ablauf weiter) → den ersten passenden Zweig ausführen: Licht ausschalten → deaktiviert: Einen Schalter ausschalten → 2 weitere Schritte / Aktionstyp nicht erhalten → Eine Nachricht an ein eigenes Ziel senden; 1 weiterer Zweig; sonst: Aktionstyp nicht erhalten → Eine Nachricht an ein eigenes Ziel senden → 2 weitere Schritte (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Vor den Aktionen werden Bedingungen geprüft. |
| [Licht ausschalten · mit Wartebedingung im Ablauf — Variante B](automations/lighting/state-light-off-with-wait-6fcc8f29/README.de.md) | Auf einen von 2 Auslösern warten (bei Ablauf weiter) → den ersten passenden Zweig ausführen: Licht ausschalten → Ein eigenes Skript ausführen → 3 weitere Schritte / Aktionstyp nicht erhalten → Eine Nachricht an ein eigenes Ziel senden; sonst: Aktionstyp nicht erhalten → Eine Nachricht an ein eigenes Ziel senden → 3 weitere Schritte (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Vor den Aktionen werden Bedingungen geprüft. |
| [Licht ausschalten · mit Wartebedingung im Ablauf — Variante C](automations/lighting/state-light-off-with-wait-b05993d4/README.de.md) | Warten für 30 min → auf einen von 2 Auslösern warten (bei Ablauf weiter) → den ersten passenden Zweig ausführen: Licht ausschalten → Ein eigenes Skript ausführen → 3 weitere Schritte / Aktionstyp nicht erhalten → Eine Nachricht an ein eigenes Ziel senden; sonst: Aktionstyp nicht erhalten → Eine Nachricht an ein eigenes Ziel senden → 3 weitere Schritte (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). |
| [Licht ausschalten · mit Wartebedingung im Ablauf — Variante D](automations/lighting/state-light-off-with-wait-b5e8441e/README.de.md) | Auf einen von 2 Auslösern warten (bei Ablauf weiter) → Licht ausschalten (ausgewählte Schritte; 9 weitere Aktionen ausgelassen). Vor den Aktionen werden Bedingungen geprüft. |

<a id="lighting-toggle"></a>

#### Umschalten (6 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Licht zwischen Ein und Aus umschalten — Variante A](automations/lighting/device-light-toggle-3c5800f8/README.de.md) | Licht zwischen Ein und Aus umschalten; Helligkeit: 81%. |
| [Licht zwischen Ein und Aus umschalten — Variante B](automations/lighting/device-light-toggle-835102aa/README.de.md) | Licht zwischen Ein und Aus umschalten; Helligkeit: 76%. |
| [Licht zwischen Ein und Aus umschalten — Variante C](automations/lighting/device-light-toggle-8feb4762/README.de.md) | Licht zwischen Ein und Aus umschalten; Helligkeit: 76%; Übergang: 1 s. |
| [Licht zwischen Ein und Aus umschalten — Variante D](automations/lighting/device-light-toggle-f2e96056/README.de.md) | Licht zwischen Ein und Aus umschalten; Helligkeit: 76%; Übergang: 1 s. |
| [Licht einschalten oder umschalten · mit Bedingungen im Ablauf](automations/lighting/state-light-on-toggle-with-branches/README.de.md) | Den ersten passenden Zweig ausführen: Licht einschalten; Helligkeitsänderung: 10% / Licht einschalten; Helligkeitsänderung: -10%; 1 weiterer Zweig. |
| [Licht zwischen Ein und Aus umschalten](automations/lighting/triggered-light-toggle/README.de.md) | Licht zwischen Ein und Aus umschalten; Helligkeit: 76%. |

<a id="lighting-on-off"></a>

#### Ein- und Ausschalten (13 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante A](automations/lighting/device-light-on-off-with-branches-1c0d2b3a/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Licht ausschalten); sonst: (Licht mit 70 % Helligkeit einschalten). |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante B](automations/lighting/device-light-on-off-with-branches-5d21fa0b/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (den ersten passenden Zweig ausführen: Licht mit 86 % Helligkeit einschalten; Übergang: 1 s; Farbtemperatur: 4000 K → Ein eigenes Skript ausführen / Licht ausschalten; Übergang: 2 s → Ein eigenes Skript ausführen) → den ersten passenden Zweig ausführen: Einen Lüfter einschalten / Einen Lüfter ausschalten. |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante C](automations/lighting/device-light-on-off-with-branches-6fe09721/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Licht ausschalten); sonst: (Licht mit 70 % Helligkeit einschalten). |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante D](automations/lighting/device-light-on-off-with-branches-c0980148/README.de.md) | Wenn unter 10: (Licht mit 5 % Helligkeit einschalten); sonst: (Licht ausschalten). Startgrenzen: unter 10 / über 10. |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante E](automations/lighting/device-light-on-off-with-branches-fc5d4c73/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Licht ausschalten); sonst: (Licht mit 70 % Helligkeit einschalten). |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf](automations/lighting/mqtt-light-on-off-with-branches/README.de.md) | Den ersten passenden Zweig ausführen: Licht mit 76 % Helligkeit einschalten → Ein eigenes Skript ausführen → 2 weitere Schritte / wenn die eingestellten Bedingungen erfüllt sind: (Ein vorhandenes Skript starten) → Ein eigenes Skript ausführen → 2 weitere Schritte. |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante A](automations/lighting/state-light-on-off-with-branches-26b32a95/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Licht mit 70 % Helligkeit einschalten → wenn die eingestellten Bedingungen erfüllt sind: (Licht mit 100 % Helligkeit einschalten; Übergang: 3 s)); sonst: (Licht ausschalten → wenn die eingestellten Bedingungen erfüllt sind: (Licht mit 10 % Helligkeit einschalten; Übergang: 30 s); sonst: (Licht ausschalten; Übergang: 5 s)). |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante B](automations/lighting/state-light-on-off-with-branches-a4561b61/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Licht mit 70 % Helligkeit einschalten); sonst: (Licht ausschalten). |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante C](automations/lighting/state-light-on-off-with-branches-af2a0600/README.de.md) | Den ersten passenden Zweig ausführen: Einen Schalter einschalten → Licht einschalten / Einen Schalter ausschalten → wenn die eingestellten Bedingungen erfüllt sind: (Licht ausschalten). Starteinstellungen: Dauer 1 min / Dauer 5 min. Vor den Aktionen werden Bedingungen geprüft. |
| [Licht ein- und ausschalten · mit Wartebedingung im Ablauf — Variante A](automations/lighting/state-light-on-off-with-wait-bacb991b/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Licht mit 70 % Helligkeit einschalten → warten für 5 min → 2 weitere Schritte). |
| [Licht ein- und ausschalten · mit Wartebedingung im Ablauf — Variante B](automations/lighting/state-light-on-off-with-wait-c1ab88d4/README.de.md) | Auf einen von 2 Auslösern warten (bei Ablauf stoppen) → den ersten passenden Zweig ausführen: wenn die eingestellten Bedingungen erfüllt sind: (Einen Schalter einschalten) → Licht ausschalten; Übergang: 2 s → 4 weitere Schritte / Aktionstyp nicht erhalten → Eine Nachricht an ein eigenes Ziel senden → 1 weiterer Schritt (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Starteinstellungen: Dauer 10 s. Vor den Aktionen werden Bedingungen geprüft. |
| [Licht ein- und ausschalten · mit Wartebedingung im Ablauf](automations/lighting/template-light-on-off-with-wait/README.de.md) | Licht einschalten → auf eine Bedingung warten → Licht ausschalten (ausgewählte Schritte; 1 weitere Aktion ausgelassen). Vor den Aktionen werden Bedingungen geprüft. |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf](automations/lighting/triggered-light-on-off-with-branches/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Licht ausschalten); sonst: (Licht einschalten). |

<a id="lighting-scenes"></a>

#### Szenen (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Eine gespeicherte Szene aktivieren · mit Wartezeit im Ablauf](automations/lighting/device-scene-on-with-delay/README.de.md) | Warten für 1 s → Eine gespeicherte Szene aktivieren → warten für 52 s 700 ms (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). |


</details>

<a id="ventilation"></a>

<details>
<summary><strong>Lüfter und Luftreiniger</strong> · 4 Automationen</summary>

**Direkt zu:** [Ein- und Ausschalten (1)](#ventilation-power) · [Geschwindigkeit einstellen (2)](#ventilation-speed) · [Betriebsprofile auswählen (1)](#ventilation-profiles)

<a id="ventilation-power"></a>

#### Ein- und Ausschalten (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Lüfter ein- und ausschalten · mit Bedingungen im Ablauf](automations/ventilation/scheduled-fan-on-off-with-branches/README.de.md) | Den ersten passenden Zweig ausführen: Einen Lüfter einschalten / Einen Lüfter ausschalten. |

<a id="ventilation-speed"></a>

#### Geschwindigkeit einstellen (2 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Lüfter einstellen](automations/ventilation/event-fan-on-speed/README.de.md) | Einen Lüfter einschalten → Lüftergeschwindigkeit auf 75 % setzen (ausgewählte Schritte; 2 weitere Aktionen ausgelassen). |
| [Lüfter einstellen · mit Bedingungen im Ablauf](automations/ventilation/periodic-fan-on-speed-with-branches/README.de.md) | Zwischenwerte vorbereiten → den ersten passenden Zweig ausführen: Einen Lüfter einschalten → Lüftergeschwindigkeit auf 75 % setzen → 2 weitere Schritte / Aktionstyp nicht erhalten → Eine Nachricht an ein eigenes Ziel senden. Vor den Aktionen werden Bedingungen geprüft. |

<a id="ventilation-profiles"></a>

#### Betriebsprofile auswählen (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Lüfter ein- und ausschalten sowie einstellen · mit Wartebedingung im Ablauf](automations/ventilation/state-fan-on-off-preset-with-wait/README.de.md) | Den ersten passenden Zweig ausführen: Zwischenwerte vorbereiten → Einen Lüfter einschalten → 5 weitere Schritte / Zwischenwerte vorbereiten → Einen Lüfter einschalten → 5 weitere Schritte; 1 weiterer Zweig. |


</details>

<a id="cleaning"></a>

<details>
<summary><strong>Saugroboter</strong> · 8 Automationen</summary>

**Direkt zu:** [Starten (5)](#cleaning-start) · [Saugleistung einstellen (2)](#cleaning-power) · [Bestimmte Bereiche reinigen (1)](#cleaning-areas)

<a id="cleaning-start"></a>

#### Starten (5 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Einen Saugroboter starten](automations/cleaning/mixed-vacuum-start/README.de.md) | Einen Saugroboter starten → Einen Zähler zurücksetzen. Startgrenzen: über 2. Vor den Aktionen werden Bedingungen geprüft. |
| [Einen Saugroboter starten — Variante A](automations/cleaning/scheduled-vacuum-start-7aa7e1d7/README.de.md) | Einen Saugroboter starten. |
| [Einen Saugroboter starten — Variante B](automations/cleaning/scheduled-vacuum-start-bc976c84/README.de.md) | Eine Geräteoption auswählen → Einen Saugroboter starten. |
| [Einen Saugroboter starten · mit Bedingungen im Ablauf](automations/cleaning/state-vacuum-start-with-branches/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (wenn die eingestellten Bedingungen erfüllt sind: (Eine Nachricht senden → Einen gespeicherten Ein/Aus-Wert einschalten → 1 weiterer Schritt)). |
| [Einen Saugroboter starten · mit Wartezeit im Ablauf](automations/cleaning/state-vacuum-start-with-delay/README.de.md) | Warten für nicht erhalten → Einen Saugroboter starten (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Vor den Aktionen werden Bedingungen geprüft. |

<a id="cleaning-power"></a>

#### Saugleistung einstellen (2 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Einen Saugroboter starten und die Saugleistung einstellen — Variante A](automations/cleaning/scheduled-vacuum-set-fan-speed-start-9e5f40a9/README.de.md) | Die Saugleistung einstellen → Einen Saugroboter starten. |
| [Einen Saugroboter starten und die Saugleistung einstellen — Variante B](automations/cleaning/scheduled-vacuum-set-fan-speed-start-e5d9d1cc/README.de.md) | Die Saugleistung einstellen → Einen Saugroboter starten. Vor den Aktionen werden Bedingungen geprüft. |

<a id="cleaning-areas"></a>

#### Bestimmte Bereiche reinigen (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Einen ausgewählten Bereich saugen lassen](automations/cleaning/device-dreame-vacuum-vacuum-clean-segment/README.de.md) | Einen ausgewählten Bereich saugen lassen; Reinigungsdurchgänge: 1. |


</details>

<a id="media"></a>

<details>
<summary><strong>Musik, Medien und Kameras</strong> · 2 Automationen</summary>

**Direkt zu:** [Kamerabilder speichern (1)](#media-snapshots) · [Kamerabild live anzeigen (1)](#media-camera-live)

<a id="media-snapshots"></a>

#### Kamerabilder speichern (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Ein Kamerabild speichern · mit Wartezeit im Ablauf](automations/media/state-camera-snapshot-with-delay/README.de.md) | Ein Kamerabild speichern → warten für 1 s (ausgewählte Schritte; 6 weitere Aktionen ausgelassen). |

<a id="media-camera-live"></a>

#### Kamerabild live anzeigen (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Medien und Kameras steuern · mit Wartezeit im Ablauf](automations/media/device-state-media-playback-play-stream-snapshot-with-delay/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Medien abspielen → warten für 2 s 500 ms → 1 weiterer Schritt) → Ein Kamerabild speichern → warten für nicht erhalten (ausgewählte Schritte; 5 weitere Aktionen ausgelassen). |


</details>

<a id="tasks"></a>

<details>
<summary><strong>Aufgabenlisten und Erinnerungen</strong> · 13 Automationen</summary>

**Direkt zu:** [Aufgabenlisten abfragen (9)](#tasks-read) · [Einträge bearbeiten (3)](#tasks-edit) · [Einträge entfernen (1)](#tasks-remove)

<a id="tasks-read"></a>

#### Aufgabenlisten abfragen (9 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf](automations/tasks/device-todo-read-with-branches/README.de.md) | Eine Aufgabenliste abfragen (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante A](automations/tasks/scheduled-todo-read-with-branches-42ac304c/README.de.md) | Eine Aufgabenliste abfragen → Zwischenwerte vorbereiten → wenn die eingestellten Bedingungen erfüllt sind: (Ein eigenes Skript ausführen). |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante B](automations/tasks/scheduled-todo-read-with-branches-8247970e/README.de.md) | Eine Aufgabenliste abfragen → Zwischenwerte vorbereiten → wenn die eingestellten Bedingungen erfüllt sind: (Ein eigenes Skript ausführen). |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante A](automations/tasks/state-todo-read-with-branches-433b7d45/README.de.md) | Eine Aufgabenliste abfragen (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Starteinstellungen: Dauer 2 min. |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante B](automations/tasks/state-todo-read-with-branches-46a1dac1/README.de.md) | Eine Aufgabenliste abfragen (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Vor den Aktionen werden Bedingungen geprüft. |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante C](automations/tasks/state-todo-read-with-branches-ad85ca77/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Eine Nachricht senden) → wenn die eingestellten Bedingungen erfüllt sind: (Eine Nachricht senden → Eine Aufgabenliste abfragen → 2 weitere Schritte). |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante D](automations/tasks/state-todo-read-with-branches-c96c1391/README.de.md) | Eine Aufgabenliste abfragen (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Vor den Aktionen werden Bedingungen geprüft. |
| [Eine Aufgabenliste abfragen · mit Wartezeit im Ablauf](automations/tasks/state-todo-read-with-delay/README.de.md) | Einen Zähler erhöhen → warten für 1 s → wenn über 20: (Eine Aufgabenliste abfragen → Zwischenwerte vorbereiten → 5 weitere Schritte). Starteinstellungen: Dauer 3 s. Vor den Aktionen werden Bedingungen geprüft. |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf](automations/tasks/threshold-state-todo-read-with-branches/README.de.md) | Den ersten passenden Zweig ausführen: Einen gespeicherten Ein/Aus-Wert einschalten / Einen gespeicherten Ein/Aus-Wert ausschalten → Aktionstyp nicht erhalten → 4 weitere Schritte. Starteinstellungen: über 10; Dauer 2 min / unter 5; Dauer 20 min; 1 weiterer Auslöser in den Details. |

<a id="tasks-edit"></a>

#### Einträge bearbeiten (3 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Eine Aufgabenliste lesen und bearbeiten · mit Bedingungen im Ablauf — Variante A](automations/tasks/periodic-todo-read-update-with-branches-67bcce5a/README.de.md) | Eine Aufgabenliste abfragen → Zwischenwerte vorbereiten → wiederholen für jeden Listeneintrag: Zwischenwerte vorbereiten. |
| [Eine Aufgabenliste lesen und bearbeiten · mit Bedingungen im Ablauf — Variante B](automations/tasks/periodic-todo-read-update-with-branches-79a8b952/README.de.md) | Eine Aufgabenliste abfragen → wiederholen für jeden Listeneintrag: Zwischenwerte vorbereiten. |
| [Eine Aufgabenliste lesen und bearbeiten · mit Bedingungen im Ablauf — Variante C](automations/tasks/periodic-todo-read-update-with-branches-a6071dba/README.de.md) | Eine Aufgabenliste abfragen → Zwischenwerte vorbereiten → wiederholen für jeden Listeneintrag: Zwischenwerte vorbereiten. |

<a id="tasks-remove"></a>

#### Einträge entfernen (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Eine Aufgabenliste lesen und Einträge entfernen · mit Bedingungen im Ablauf](automations/tasks/periodic-todo-read-remove-with-branches/README.de.md) | Eine Aufgabenliste abfragen → wiederholen für jeden Listeneintrag: Zwischenwerte vorbereiten (ausgewählte Schritte; 4 weitere Aktionen ausgelassen). |


</details>

<a id="switches"></a>

<details>
<summary><strong>Schalter und Steckdosen</strong> · 16 Automationen</summary>

**Direkt zu:** [Einschalten (4)](#switches-on) · [Ausschalten (3)](#switches-off) · [Umschalten (4)](#switches-toggle) · [Ein- und Ausschalten (5)](#switches-on-off)

<a id="switches-on"></a>

#### Einschalten (4 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Einen Schalter einschalten · mit Wartezeit im Ablauf](automations/switches/mqtt-switch-on-with-delay/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Einen Schalter einschalten → warten für 10 s) → Bedingungen prüfen; bei falsch diesen Ablauf stoppen → Aktionstyp nicht erhalten. |
| [Einen Schalter einschalten](automations/switches/state-switch-on/README.de.md) | Einen Schalter einschalten → Ein eigenes Skript ausführen. Vor den Aktionen werden Bedingungen geprüft. |
| [Einen Schalter einschalten · mit Wartebedingung im Ablauf](automations/switches/state-template-switch-on-with-wait/README.de.md) | Den ersten passenden Zweig ausführen: Einen gespeicherten Ein/Aus-Wert einschalten / Einen gespeicherten Ein/Aus-Wert ausschalten → Bedingungen prüfen; bei falsch diesen Ablauf stoppen → 4 weitere Schritte. Starteinstellungen: Dauer 8 min / Dauer 20 s. |
| [Einen Schalter einschalten](automations/switches/template-switch-on/README.de.md) | Einen Schalter einschalten. |

<a id="switches-off"></a>

#### Ausschalten (3 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Einen Schalter ausschalten · mit Wartebedingung im Ablauf](automations/switches/state-switch-off-with-wait/README.de.md) | Warten auf einen Wert über 7.999 oder 5 weitere Auslöser (bei Ablauf weiter) → wenn die eingestellten Bedingungen erfüllt sind: (Einen Schalter ausschalten) (ausgewählte Schritte; 2 weitere Aktionen ausgelassen). Vor den Aktionen werden Bedingungen geprüft. |
| [Einen Schalter ausschalten](automations/switches/template-switch-off/README.de.md) | Einen Schalter ausschalten. |
| [Einen Schalter ausschalten · mit Wartebedingung im Ablauf](automations/switches/triggered-switch-off-with-wait/README.de.md) | Warten auf einen Wert unter 8 (bei Ablauf weiter) → wenn die eingestellten Bedingungen erfüllt sind: (Einen Schalter ausschalten); sonst: (Einen Hinweis in Home Assistant anzeigen) (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). Vor den Aktionen werden Bedingungen geprüft. |

<a id="switches-toggle"></a>

#### Umschalten (4 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Einen Schalter zwischen Ein und Aus umschalten](automations/switches/device-switch-toggle/README.de.md) | Einen Schalter zwischen Ein und Aus umschalten. |
| [Einen Schalter zwischen Ein und Aus umschalten](automations/switches/state-switch-toggle/README.de.md) | Einen Schalter zwischen Ein und Aus umschalten. |
| [Einen Schalter zwischen Ein und Aus umschalten — Variante A](automations/switches/triggered-switch-toggle-24cc2d6e/README.de.md) | Einen Schalter zwischen Ein und Aus umschalten. |
| [Einen Schalter zwischen Ein und Aus umschalten — Variante B](automations/switches/triggered-switch-toggle-c9419015/README.de.md) | Einen Schalter zwischen Ein und Aus umschalten. |

<a id="switches-on-off"></a>

#### Ein- und Ausschalten (5 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Schalter ein- und ausschalten · mit Wartebedingung im Ablauf](automations/switches/state-periodic-switch-on-off-with-wait/README.de.md) | 3 Pfade parallel ausführen. Vor den Aktionen werden Bedingungen geprüft. |
| [Schalter ein- und ausschalten · mit Bedingungen im Ablauf](automations/switches/state-switch-on-off-with-branches/README.de.md) | Den ersten passenden Zweig ausführen: Einen Schalter einschalten / Einen Schalter ausschalten. Starteinstellungen: Dauer 5 min. |
| [Schalter ein- und ausschalten · mit Wartezeit im Ablauf — Variante A](automations/switches/state-switch-on-off-with-delay-91d3deba/README.de.md) | Einen Schalter einschalten → warten für 10 min → Einen Schalter ausschalten. |
| [Schalter ein- und ausschalten · mit Wartezeit im Ablauf — Variante B](automations/switches/state-switch-on-off-with-delay-d9a93573/README.de.md) | Den ersten passenden Zweig ausführen: Einen Schalter einschalten → warten für 3 min → 2 weitere Schritte / Bedingungen prüfen; bei falsch diesen Ablauf stoppen → Einen Schalter ausschalten. Starteinstellungen: Dauer 5 min. |
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
| [Durchsagen und Sprachausgabe nutzen](automations/voice/state-voice-announce-speak/README.de.md) | 7 Pfade parallel ausführen. |


</details>

<a id="notifications"></a>

<details>
<summary><strong>Nachrichten und Hinweise</strong> · 11 Automationen</summary>

**Direkt zu:** [Nachrichten versenden (9)](#notifications-messages) · [Hinweise in Home Assistant (2)](#notifications-ha-notices)

<a id="notifications-messages"></a>

#### Nachrichten versenden (9 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Nachrichten senden — Variante A](automations/notifications/device-notification-send-4fffe63e/README.de.md) | Einen Zähler zurücksetzen → Ein eigenes Skript ausführen → Eine Nachricht senden. |
| [Nachrichten senden — Variante B](automations/notifications/device-notification-send-6b699d26/README.de.md) | Eine Nachricht an ein eigenes Ziel senden (ausgewählte Schritte; 3 weitere Aktionen ausgelassen). |
| [Nachrichten senden — Variante C](automations/notifications/device-notification-send-8e742eeb/README.de.md) | Eine Nachricht senden. Starteinstellungen: Dauer 5 min. |
| [Nachrichten senden · mit Wartezeit im Ablauf](automations/notifications/device-notification-send-with-delay/README.de.md) | Wiederholen bis Bedingungen erfüllt sind: Eine Nachricht senden. Startgrenzen: unter 5. |
| [Nachrichten senden · mit Bedingungen im Ablauf](automations/notifications/periodic-notification-send-with-branches/README.de.md) | Eine Wettervorhersage abrufen → Zwischenwerte vorbereiten → den ersten passenden Zweig ausführen: Aktionstyp nicht erhalten → Eine Nachricht an ein eigenes Ziel senden. Vor den Aktionen werden Bedingungen geprüft. |
| [Nachrichten senden — Variante A](automations/notifications/state-notification-send-0989a580/README.de.md) | Bedingungen prüfen; bei falsch diesen Ablauf stoppen → Eine eingerichtete Schaltfläche auslösen → Eine Nachricht senden. Vor den Aktionen werden Bedingungen geprüft. |
| [Nachrichten senden — Variante B](automations/notifications/state-notification-send-3e58df61/README.de.md) | Eine Nachricht senden. |
| [Nachrichten senden — Variante C](automations/notifications/state-notification-send-a0e2d0da/README.de.md) | Zwischenwerte vorbereiten → Aktionstyp nicht erhalten → Eine Nachricht an ein eigenes Ziel senden. Vor den Aktionen werden Bedingungen geprüft. |
| [Nachrichten senden](automations/notifications/state-scheduled-notification-send/README.de.md) | Einen Textwert speichern → Aktionstyp nicht erhalten → Eine Nachricht an ein eigenes Ziel senden. Vor den Aktionen werden Bedingungen geprüft. |

<a id="notifications-ha-notices"></a>

#### Hinweise in Home Assistant (2 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Nachrichten und Hinweise ausgeben — Variante A](automations/notifications/device-notifications-create-notify-42c8182d/README.de.md) | Eine Nachricht senden → Einen Hinweis in Home Assistant anzeigen. Starteinstellungen: Dauer 5 min. |
| [Nachrichten und Hinweise ausgeben — Variante B](automations/notifications/device-notifications-create-notify-713dfa68/README.de.md) | Eine Nachricht senden → Einen Hinweis in Home Assistant anzeigen. Starteinstellungen: Dauer 2 min. |


</details>

<a id="helpers"></a>

<details>
<summary><strong>Zähler und gespeicherte Werte</strong> · 6 Automationen</summary>

**Direkt zu:** [Virtuelle Schalter (4)](#helpers-switches) · [Zähler verändern (1)](#helpers-counters) · [Texte speichern (1)](#helpers-text)

<a id="helpers-switches"></a>

#### Virtuelle Schalter (4 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Einen gespeicherten Ein/Aus-Wert ausschalten](automations/helpers/scheduled-input-boolean-off/README.de.md) | Einen gespeicherten Ein/Aus-Wert ausschalten. |
| [Gespeicherte Ein/Aus-Werte ändern · mit Bedingungen im Ablauf](automations/helpers/scheduled-input-boolean-on-off-with-branches/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Einen gespeicherten Ein/Aus-Wert einschalten); sonst: (Einen gespeicherten Ein/Aus-Wert ausschalten). |
| [Gespeicherte Ein/Aus-Werte ändern · mit Wartezeit im Ablauf](automations/helpers/state-input-boolean-on-off-with-delay/README.de.md) | Einen gespeicherten Ein/Aus-Wert einschalten → warten für 180 s → Einen gespeicherten Ein/Aus-Wert ausschalten (ausgewählte Schritte; 1 weitere Aktion ausgelassen). Vor den Aktionen werden Bedingungen geprüft. |
| [Gespeicherte Ein/Aus-Werte ändern · mit Bedingungen im Ablauf](automations/helpers/state-scheduled-input-boolean-on-off-with-branches/README.de.md) | Den ersten passenden Zweig ausführen: Einen gespeicherten Ein/Aus-Wert einschalten / Einen gespeicherten Ein/Aus-Wert ausschalten. |

<a id="helpers-counters"></a>

#### Zähler verändern (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Einen Zähler erhöhen](automations/helpers/device-counter-increment/README.de.md) | Einen Zähler erhöhen. Starteinstellungen: Dauer 8 s. |

<a id="helpers-text"></a>

#### Texte speichern (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Einen Textwert speichern](automations/helpers/template-input-text-value/README.de.md) | Einen Textwert speichern. Vor den Aktionen werden Bedingungen geprüft. |


</details>

<a id="system"></a>

<details>
<summary><strong>Weitere Abläufe und Geräteaktionen</strong> · 23 Automationen</summary>

**Direkt zu:** [Eigene Skripte (6)](#system-scripts) · [Gerätefunktionen und Tasten (1)](#system-device-controls) · [MQTT-Nachrichten (3)](#system-mqtt) · [Andere Automationen schalten (1)](#system-automations) · [Wetterdaten abrufen (1)](#system-weather) · [Wartung und Protokolle (1)](#system-maintenance) · [Noch einzurichtende Aktionen (10)](#system-unfinished)

<a id="system-scripts"></a>

#### Eigene Skripte (6 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Ein vorhandenes Skript ausführen](automations/system/event-script-run/README.de.md) | Ein eigenes Skript ausführen. Vor den Aktionen werden Bedingungen geprüft. |
| [Ein vorhandenes Skript ausführen · mit Bedingungen im Ablauf — Variante A](automations/system/mqtt-script-on-with-branches/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Ein vorhandenes Skript starten); sonst: (Ein vorhandenes Skript starten). |
| [Ein vorhandenes Skript ausführen](automations/system/mqtt-script-run/README.de.md) | Ein eigenes Skript ausführen. |
| [Ein vorhandenes Skript ausführen · mit Bedingungen im Ablauf — Variante B](automations/system/mqtt-script-run-with-branches/README.de.md) | Den ersten passenden Zweig ausführen: Aktionstyp nicht erhalten; sonst: Ein eigenes Skript ausführen. |
| [Ein vorhandenes Skript ausführen](automations/system/periodic-script-run/README.de.md) | Ein eigenes Skript ausführen. |
| [Ein vorhandenes Skript ausführen](automations/system/state-scheduled-script-run/README.de.md) | Wiederholen für jeden Listeneintrag: Bedingungen prüfen; bei falsch diesen Ablauf stoppen. |

<a id="system-device-controls"></a>

#### Gerätefunktionen und Tasten (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Mehrere Funktionen verbinden · mit Wartezeit im Ablauf](automations/system/state-system-press-select-option-with-delay/README.de.md) | Eine Geräteoption auswählen → warten für nicht erhalten → Eine Gerätefunktion per Tastendruck auslösen. Vor den Aktionen werden Bedingungen geprüft. |

<a id="system-mqtt"></a>

#### MQTT-Nachrichten (3 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Eine MQTT-Nachricht senden](automations/system/periodic-mqtt-publish/README.de.md) | Eine MQTT-Nachricht senden. |
| [Eine MQTT-Nachricht senden — Variante A](automations/system/state-mqtt-publish-03a56ab8/README.de.md) | Eine MQTT-Nachricht senden. Vor den Aktionen werden Bedingungen geprüft. |
| [Eine MQTT-Nachricht senden — Variante B](automations/system/state-mqtt-publish-4d55a0f6/README.de.md) | Eine MQTT-Nachricht senden. |

<a id="system-automations"></a>

#### Andere Automationen schalten (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Andere Automationen aktivieren und deaktivieren · mit Wartezeit im Ablauf](automations/system/device-automation-on-off-with-delay/README.de.md) | Aktionstyp nicht erhalten → Eine andere Automation aktivieren → Eine andere Automation deaktivieren → 2 weitere Schritte (siehe Ablauf). |

<a id="system-weather"></a>

#### Wetterdaten abrufen (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Mehrere Funktionen verbinden · mit Wartezeit im Ablauf](automations/system/state-periodic-system-custom-action-get-forecasts-with-delay/README.de.md) | Eine Wettervorhersage abrufen → Bedingungen prüfen; bei falsch diesen Ablauf stoppen → Zwischenwerte vorbereiten → 3 weitere Schritte (siehe Ablauf). Vor den Aktionen werden Bedingungen geprüft. |

<a id="system-maintenance"></a>

#### Wartung und Protokolle (1 Automation)

| Automation | Was passiert? |
| --- | --- |
| [Mehrere Funktionen verbinden](automations/system/periodic-system-reload-config-entry-write/README.de.md) | Einen Eintrag ins Systemprotokoll schreiben → Eine Geräteanbindung neu laden. Vor den Aktionen werden Bedingungen geprüft. |

<a id="system-unfinished"></a>

#### Noch einzurichtende Aktionen (10 Automationen)

| Automation | Was passiert? |
| --- | --- |
| [Eigene Aktion einrichten — Variante A](automations/system/device-generic-action-15407118/README.de.md) | Aktionstyp nicht erhalten. |
| [Eigene Aktion einrichten — Variante B](automations/system/device-generic-action-15407118-a/README.de.md) | Aktionstyp nicht erhalten. |
| [Eigene Aktion einrichten — Variante C](automations/system/device-generic-action-ddc77372/README.de.md) | Aktionstyp nicht erhalten. Vor den Aktionen werden Bedingungen geprüft. |
| [Eigene Aktion einrichten — Variante D](automations/system/device-generic-action-f594a0ff/README.de.md) | Aktionstyp nicht erhalten. Vor den Aktionen werden Bedingungen geprüft. |
| [Eigene Aktion einrichten · mit Bedingungen im Ablauf](automations/system/device-generic-action-with-branches/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (Aktionstyp nicht erhalten → Aktionstyp nicht erhalten); sonst: (Aktionstyp nicht erhalten → Aktionstyp nicht erhalten). |
| [Eigene Aktion einrichten · mit Wartebedingung im Ablauf — Variante A](automations/system/device-generic-action-with-wait-31e6d1d6/README.de.md) | Wenn die eingestellten Bedingungen erfüllt sind: (wenn unter 10: (Aktionstyp nicht erhalten → auf einen weiteren Auslöser warten (bis zu 1 min; bei Ablauf weiter) → 1 weiterer Schritt)). |
| [Eigene Aktion einrichten · mit Wartebedingung im Ablauf — Variante B](automations/system/device-generic-action-with-wait-4ebede39/README.de.md) | Aktionstyp nicht erhalten → warten auf einen Wert unter 60 → Aktionstyp nicht erhalten. Startgrenzen: über 60. |
| [Eigene Aktion einrichten · mit Bedingungen im Ablauf](automations/system/periodic-generic-action-with-branches/README.de.md) | Wenn unter 0.2: (Aktionstyp nicht erhalten); sonst: (Aktionstyp nicht erhalten). |
| [Eigene Aktion einrichten](automations/system/state-generic-action/README.de.md) | Aktionstyp nicht erhalten. |
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
