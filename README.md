# Home Assistant – Ideen für dein Smart Home

Licht automatisch schalten, die Heizung einstellen oder eine Nachricht aufs Handy schicken: Hier findest du **Vorlagen und leicht erklärte Beispiele** für solche Abläufe in Home Assistant.

**[Erste Automation Schritt für Schritt](how-to/get-started.md)** · **[Alle Vorlagen ansehen](#automation-catalogue)**

> **Vor dem Start:** Die Dateien sind Vorlagen zum Nachbauen. Echte Geräte und private Angaben wurden durch Platzhalter ersetzt. Manche Auslöser, Bedingungen und Formeln fehlen noch. Du ergänzt sie für deinen eigenen Ablauf – nur die Gerätenamen auszutauschen reicht nicht immer.

## Neu bei Home Assistant? Fang hier an

Eine Automation besteht aus einer einfachen Idee:

> **Wenn** etwas passiert, **dann** soll Home Assistant etwas tun.
>
> Zum Beispiel: Wenn eine von dir gewählte Uhrzeit erreicht ist, schalte eine Lampe ein.

Mit der **[Schritt-für-Schritt-Anleitung](how-to/get-started.md)** baust du diese kleine Übung direkt in der Home-Assistant-Oberfläche. Anschließend kannst du sie mit Ideen aus der Sammlung erweitern.

## So nutzt du die Sammlung

1. **Idee auswählen.** Öffne unten einen Bereich, zum Beispiel „Licht“, und wähle die passende Aufgabe, etwa „Einschalten“ oder „Ausschalten“.
2. **Beschreibung lesen.** Jede Vorlage erklärt die vorgesehene Aufgabe, den Auslöser und die Stellen, die du anpassen musst.
3. **Mit deinen Geräten nachbauen und testen.** Ergänze den Ablauf in Home Assistant und prüfe ihn zunächst mit einem einzelnen Gerät.

### Drei Beispiele zum Anschauen

| Das möchtest du machen | Passende Vorlage |
| --- | --- |
| Licht ausschalten, wenn sich ein Zustand ändert | [Licht ausschalten](automations/lighting/state-light-off-22ac0c06/README.md) |
| Einen Schalter abhängig von einem Messwert ein- und wieder ausschalten | [Schalter nach Messwert steuern](automations/switches/threshold-switch-on-off-with-wait/README.md) |
| Einen Saugroboter zu einer festgelegten Zeit starten | [Saugroboter nach Zeitplan starten](automations/cleaning/scheduled-vacuum-start-7aa7e1d7/README.md) |

Die genauen Geräte, Zeiten und Bedingungen legst du selbst fest. Die dritte Vorlage setzt zum Beispiel voraus, dass dein Saugroboter bereits in Home Assistant eingerichtet ist.

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

**Welche Datei brauche ich?** Öffne zuerst die Beschreibung (`README.md`) eines Beispiels. Die Datei `automation.yaml` enthält den dazugehörigen Ablauf als Text. Die dritte Datei, `metadata.json`, wird für die automatische Übersicht verwendet.

<!-- catalogue:start -->

<a id="automation-catalogue"></a>

## Automationen im Überblick (136 Vorlagen)

Die Vorlagen sind in **13 Bereiche und 39 Unterbereiche** nach ihrer erkennbaren Funktion aufgeteilt.

Wähle unten einen Bereich und klappe ihn auf. Die Sprunglinks darin führen direkt zum gewünschten Unterbereich. Öffne anschließend eine Vorlage: Dort steht, was du brauchst und was du anpassen musst.

Manche Abläufe gibt es in mehreren Varianten. Die Buchstaben helfen beim Unterscheiden; sie stehen für unterschiedliche Konfigurationen, nicht für bestimmte Räume oder Geräte.

| Bereich | Vorlagen | Unterbereiche |
| --- | ---: | --- |
| [Heizung und Raumklima](#climate) | 18 | Temperatur einstellen · Heiz- und Kühlmodus · Heiz- und Klimaprofile |
| [Licht](#lighting) | 29 | Einschalten · Ausschalten · Umschalten · Ein- und Ausschalten · Szenen |
| [Lüfter und Luftreiniger](#ventilation) | 4 | Ein- und Ausschalten · Geschwindigkeit einstellen · Betriebsprofile auswählen |
| [Saugroboter](#cleaning) | 8 | Starten · Saugleistung einstellen · Bestimmte Bereiche reinigen |
| [Rollläden und Abdeckungen](#covers) | 3 | Schließen · Öffnen und schließen |
| [Musik, Medien und Kameras](#media) | 2 | Kamerabilder speichern · Kamerabild live anzeigen |
| [Schlösser und Zutritt](#access) | 2 | Schloss öffnen |
| [Aufgabenlisten und Erinnerungen](#tasks) | 13 | Aufgabenlisten abfragen · Einträge bearbeiten · Einträge entfernen |
| [Schalter und Steckdosen](#switches) | 16 | Einschalten · Ausschalten · Umschalten · Ein- und Ausschalten |
| [Sprache und Durchsagen](#voice) | 1 | Durchsagen und Vorlesen |
| [Nachrichten und Hinweise](#notifications) | 11 | Nachrichten versenden · Hinweise in Home Assistant |
| [Zähler und gespeicherte Werte](#helpers) | 6 | Virtuelle Schalter · Zähler verändern · Texte speichern |
| [Weitere Abläufe und Geräteaktionen](#system) | 23 | Eigene Skripte · Gerätefunktionen und Tasten · MQTT-Nachrichten · Andere Automationen schalten · Wetterdaten abrufen · Wartung und Protokolle · Noch einzurichtende Aktionen |

<a id="climate"></a>

<details>
<summary><strong>Heizung und Raumklima</strong> · 18 Vorlagen</summary>

**Direkt zu:** [Temperatur einstellen (9)](#climate-temperature) · [Heiz- und Kühlmodus (4)](#climate-modes) · [Heiz- und Klimaprofile (5)](#climate-profiles)

<a id="climate-temperature"></a>

#### Temperatur einstellen (9 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf — Variante A](automations/climate/device-climate-temperature-with-branches-54a60709/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf — Variante B](automations/climate/device-climate-temperature-with-branches-c104c302/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf](automations/climate/mixed-climate-temperature-with-branches/README.md) | Wenn sich ein Wert oder Zustand ändert; Zu einer eingestellten Uhrzeit; In einem regelmäßig wiederholten Zeitabstand |
| [Die gewünschte Raumtemperatur einstellen · mit Wartebedingung im Ablauf — Variante A](automations/climate/mixed-climate-temperature-with-wait-a3321799/README.md) | Wenn sich ein Wert oder Zustand ändert; Wenn eine selbst festgelegte Bedingung zutrifft; Zu einer eingestellten Uhrzeit |
| [Die gewünschte Raumtemperatur einstellen · mit Wartebedingung im Ablauf — Variante B](automations/climate/mixed-climate-temperature-with-wait-f1451717/README.md) | Wenn sich ein Wert oder Zustand ändert; Wenn eine selbst festgelegte Bedingung zutrifft; Zu einer eingestellten Uhrzeit |
| [Die gewünschte Raumtemperatur einstellen · mit Wartebedingung im Ablauf — Variante C](automations/climate/mixed-climate-temperature-with-wait-fc1f1012/README.md) | Wenn sich ein Wert oder Zustand ändert; Wenn eine selbst festgelegte Bedingung zutrifft; Zu einer eingestellten Uhrzeit |
| [Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf — Variante A](automations/climate/scheduled-climate-temperature-with-branches-47c2e215/README.md) | Zu einer eingestellten Uhrzeit |
| [Die gewünschte Raumtemperatur einstellen · mit Bedingungen im Ablauf — Variante B](automations/climate/scheduled-climate-temperature-with-branches-5aaa8edc/README.md) | Zu einer eingestellten Uhrzeit |
| [Die gewünschte Raumtemperatur einstellen · mit Wartebedingung im Ablauf](automations/climate/state-climate-temperature-with-wait/README.md) | Wenn sich ein Wert oder Zustand ändert |

<a id="climate-modes"></a>

#### Heiz- und Kühlmodus (4 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Heizung oder Klimaanlage einstellen · mit Bedingungen im Ablauf — Variante A](automations/climate/state-climate-mode-temperature-with-branches-049416bb/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Heizung oder Klimaanlage einstellen · mit Bedingungen im Ablauf — Variante B](automations/climate/state-climate-mode-temperature-with-branches-104d0276/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Heizung oder Klimaanlage einstellen · mit Bedingungen im Ablauf — Variante C](automations/climate/state-climate-mode-temperature-with-branches-6016b2ee/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Heizung oder Klimaanlage einstellen · mit Bedingungen im Ablauf — Variante D](automations/climate/state-climate-mode-temperature-with-branches-75cb761b/README.md) | Wenn sich ein Wert oder Zustand ändert |

<a id="climate-profiles"></a>

#### Heiz- und Klimaprofile (5 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante A](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-3b582a19/README.md) | Wenn sich ein Wert oder Zustand ändert; In einem regelmäßig wiederholten Zeitabstand |
| [Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante B](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-6037647c/README.md) | Wenn sich ein Wert oder Zustand ändert; In einem regelmäßig wiederholten Zeitabstand |
| [Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante C](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-b8c21183/README.md) | Wenn sich ein Wert oder Zustand ändert; In einem regelmäßig wiederholten Zeitabstand |
| [Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante D](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-d46bf28e/README.md) | Wenn sich ein Wert oder Zustand ändert; In einem regelmäßig wiederholten Zeitabstand |
| [Heizung oder Klimaanlage einstellen · mit Wartebedingung im Ablauf — Variante E](automations/climate/state-periodic-climate-mode-preset-temperature-with-wait-f9d2161c/README.md) | Wenn sich ein Wert oder Zustand ändert; In einem regelmäßig wiederholten Zeitabstand |


</details>

<a id="lighting"></a>

<details>
<summary><strong>Licht</strong> · 29 Vorlagen</summary>

**Direkt zu:** [Einschalten (2)](#lighting-on) · [Ausschalten (7)](#lighting-off) · [Umschalten (6)](#lighting-toggle) · [Ein- und Ausschalten (13)](#lighting-on-off) · [Szenen (1)](#lighting-scenes)

<a id="lighting-on"></a>

#### Einschalten (2 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Licht einschalten · mit Wartezeit im Ablauf](automations/lighting/state-light-on-with-delay/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Licht einschalten · mit Wartebedingung im Ablauf](automations/lighting/state-light-on-with-wait/README.md) | Wenn sich ein Wert oder Zustand ändert |

<a id="lighting-off"></a>

#### Ausschalten (7 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Licht ausschalten](automations/lighting/scheduled-light-off/README.md) | Zu einer eingestellten Uhrzeit |
| [Licht ausschalten — Variante A](automations/lighting/state-light-off-22ac0c06/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Licht ausschalten — Variante B](automations/lighting/state-light-off-7cb13cdd/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Licht ausschalten · mit Wartebedingung im Ablauf — Variante A](automations/lighting/state-light-off-with-wait-4dccd971/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Licht ausschalten · mit Wartebedingung im Ablauf — Variante B](automations/lighting/state-light-off-with-wait-6fcc8f29/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Licht ausschalten · mit Wartebedingung im Ablauf — Variante C](automations/lighting/state-light-off-with-wait-b05993d4/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Licht ausschalten · mit Wartebedingung im Ablauf — Variante D](automations/lighting/state-light-off-with-wait-b5e8441e/README.md) | Wenn sich ein Wert oder Zustand ändert |

<a id="lighting-toggle"></a>

#### Umschalten (6 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Licht zwischen Ein und Aus umschalten — Variante A](automations/lighting/device-light-toggle-3c5800f8/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Licht zwischen Ein und Aus umschalten — Variante B](automations/lighting/device-light-toggle-835102aa/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Licht zwischen Ein und Aus umschalten — Variante C](automations/lighting/device-light-toggle-8feb4762/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Licht zwischen Ein und Aus umschalten — Variante D](automations/lighting/device-light-toggle-f2e96056/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Licht einschalten oder umschalten · mit Bedingungen im Ablauf](automations/lighting/state-light-on-toggle-with-branches/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Licht zwischen Ein und Aus umschalten](automations/lighting/triggered-light-toggle/README.md) | Der Auslöser muss noch eingerichtet werden |

<a id="lighting-on-off"></a>

#### Ein- und Ausschalten (13 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante A](automations/lighting/device-light-on-off-with-branches-1c0d2b3a/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante B](automations/lighting/device-light-on-off-with-branches-5d21fa0b/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante C](automations/lighting/device-light-on-off-with-branches-6fe09721/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante D](automations/lighting/device-light-on-off-with-branches-c0980148/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante E](automations/lighting/device-light-on-off-with-branches-fc5d4c73/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf](automations/lighting/mqtt-light-on-off-with-branches/README.md) | Wenn eine MQTT-Nachricht ankommt |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante A](automations/lighting/state-light-on-off-with-branches-26b32a95/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante B](automations/lighting/state-light-on-off-with-branches-a4561b61/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf — Variante C](automations/lighting/state-light-on-off-with-branches-af2a0600/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Licht ein- und ausschalten · mit Wartebedingung im Ablauf — Variante A](automations/lighting/state-light-on-off-with-wait-bacb991b/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Licht ein- und ausschalten · mit Wartebedingung im Ablauf — Variante B](automations/lighting/state-light-on-off-with-wait-c1ab88d4/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Licht ein- und ausschalten · mit Wartebedingung im Ablauf](automations/lighting/template-light-on-off-with-wait/README.md) | Wenn eine selbst festgelegte Bedingung zutrifft |
| [Licht ein- und ausschalten · mit Bedingungen im Ablauf](automations/lighting/triggered-light-on-off-with-branches/README.md) | Der Auslöser muss noch eingerichtet werden |

<a id="lighting-scenes"></a>

#### Szenen (1 Vorlage)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Eine gespeicherte Szene aktivieren · mit Wartezeit im Ablauf](automations/lighting/device-scene-on-with-delay/README.md) | Wenn ein Gerät ein Ereignis meldet |


</details>

<a id="ventilation"></a>

<details>
<summary><strong>Lüfter und Luftreiniger</strong> · 4 Vorlagen</summary>

**Direkt zu:** [Ein- und Ausschalten (1)](#ventilation-power) · [Geschwindigkeit einstellen (2)](#ventilation-speed) · [Betriebsprofile auswählen (1)](#ventilation-profiles)

<a id="ventilation-power"></a>

#### Ein- und Ausschalten (1 Vorlage)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Lüfter ein- und ausschalten · mit Bedingungen im Ablauf](automations/ventilation/scheduled-fan-on-off-with-branches/README.md) | Zu einer eingestellten Uhrzeit |

<a id="ventilation-speed"></a>

#### Geschwindigkeit einstellen (2 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Lüfter einstellen](automations/ventilation/event-fan-on-speed/README.md) | Wenn ein festgelegtes Ereignis eintritt |
| [Lüfter einstellen · mit Bedingungen im Ablauf](automations/ventilation/periodic-fan-on-speed-with-branches/README.md) | In einem regelmäßig wiederholten Zeitabstand |

<a id="ventilation-profiles"></a>

#### Betriebsprofile auswählen (1 Vorlage)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Lüfter ein- und ausschalten sowie einstellen · mit Wartebedingung im Ablauf](automations/ventilation/state-fan-on-off-preset-with-wait/README.md) | Wenn sich ein Wert oder Zustand ändert |


</details>

<a id="cleaning"></a>

<details>
<summary><strong>Saugroboter</strong> · 8 Vorlagen</summary>

**Direkt zu:** [Starten (5)](#cleaning-start) · [Saugleistung einstellen (2)](#cleaning-power) · [Bestimmte Bereiche reinigen (1)](#cleaning-areas)

<a id="cleaning-start"></a>

#### Starten (5 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Einen Saugroboter starten](automations/cleaning/mixed-vacuum-start/README.md) | Wenn ein Messwert eine eingestellte Grenze überschreitet oder unterschreitet; Wenn sich ein Wert oder Zustand ändert; Zu einer eingestellten Uhrzeit |
| [Einen Saugroboter starten — Variante A](automations/cleaning/scheduled-vacuum-start-7aa7e1d7/README.md) | Zu einer eingestellten Uhrzeit |
| [Einen Saugroboter starten — Variante B](automations/cleaning/scheduled-vacuum-start-bc976c84/README.md) | Zu einer eingestellten Uhrzeit |
| [Einen Saugroboter starten · mit Bedingungen im Ablauf](automations/cleaning/state-vacuum-start-with-branches/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Einen Saugroboter starten · mit Wartezeit im Ablauf](automations/cleaning/state-vacuum-start-with-delay/README.md) | Wenn sich ein Wert oder Zustand ändert |

<a id="cleaning-power"></a>

#### Saugleistung einstellen (2 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Einen Saugroboter starten und die Saugleistung einstellen — Variante A](automations/cleaning/scheduled-vacuum-set-fan-speed-start-9e5f40a9/README.md) | Zu einer eingestellten Uhrzeit |
| [Einen Saugroboter starten und die Saugleistung einstellen — Variante B](automations/cleaning/scheduled-vacuum-set-fan-speed-start-e5d9d1cc/README.md) | Zu einer eingestellten Uhrzeit |

<a id="cleaning-areas"></a>

#### Bestimmte Bereiche reinigen (1 Vorlage)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Einen ausgewählten Bereich saugen lassen](automations/cleaning/device-dreame-vacuum-vacuum-clean-segment/README.md) | Wenn ein Gerät ein Ereignis meldet |


</details>

<a id="covers"></a>

<details>
<summary><strong>Rollläden und Abdeckungen</strong> · 3 Vorlagen</summary>

**Direkt zu:** [Schließen (1)](#covers-close) · [Öffnen und schließen (2)](#covers-open-close)

<a id="covers-close"></a>

#### Schließen (1 Vorlage)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Eine Abdeckung schließen · mit Bedingungen im Ablauf](automations/covers/threshold-template-cover-close-with-branches/README.md) | Wenn ein Messwert eine eingestellte Grenze überschreitet oder unterschreitet; Wenn eine selbst festgelegte Bedingung zutrifft |

<a id="covers-open-close"></a>

#### Öffnen und schließen (2 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Eine Abdeckung öffnen und schließen · mit Bedingungen im Ablauf](automations/covers/device-cover-close-open-with-branches/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Eine Abdeckung öffnen und schließen · mit Bedingungen im Ablauf](automations/covers/threshold-cover-close-open-with-branches/README.md) | Wenn ein Messwert eine eingestellte Grenze überschreitet oder unterschreitet |


</details>

<a id="media"></a>

<details>
<summary><strong>Musik, Medien und Kameras</strong> · 2 Vorlagen</summary>

**Direkt zu:** [Kamerabilder speichern (1)](#media-snapshots) · [Kamerabild live anzeigen (1)](#media-camera-live)

<a id="media-snapshots"></a>

#### Kamerabilder speichern (1 Vorlage)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Ein Kamerabild speichern · mit Wartezeit im Ablauf](automations/media/state-camera-snapshot-with-delay/README.md) | Wenn sich ein Wert oder Zustand ändert |

<a id="media-camera-live"></a>

#### Kamerabild live anzeigen (1 Vorlage)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Medien und Kameras steuern · mit Wartezeit im Ablauf](automations/media/device-state-media-playback-play-stream-snapshot-with-delay/README.md) | Wenn ein Gerät ein Ereignis meldet; Wenn sich ein Wert oder Zustand ändert |


</details>

<a id="access"></a>

<details>
<summary><strong>Schlösser und Zutritt</strong> · 2 Vorlagen</summary>

**Direkt zu:** [Schloss öffnen (2)](#access-open)

<a id="access-open"></a>

#### Schloss öffnen (2 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Ein Schloss öffnen · mit Wartebedingung im Ablauf](automations/access/state-lock-open-with-wait/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Ein Schloss öffnen](automations/access/state-tag-lock-open/README.md) | Wenn sich ein Wert oder Zustand ändert; Wenn ein Tag gescannt wird |


</details>

<a id="tasks"></a>

<details>
<summary><strong>Aufgabenlisten und Erinnerungen</strong> · 13 Vorlagen</summary>

**Direkt zu:** [Aufgabenlisten abfragen (9)](#tasks-read) · [Einträge bearbeiten (3)](#tasks-edit) · [Einträge entfernen (1)](#tasks-remove)

<a id="tasks-read"></a>

#### Aufgabenlisten abfragen (9 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf](automations/tasks/device-todo-read-with-branches/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante A](automations/tasks/scheduled-todo-read-with-branches-42ac304c/README.md) | Zu einer eingestellten Uhrzeit |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante B](automations/tasks/scheduled-todo-read-with-branches-8247970e/README.md) | Zu einer eingestellten Uhrzeit |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante A](automations/tasks/state-todo-read-with-branches-433b7d45/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante B](automations/tasks/state-todo-read-with-branches-46a1dac1/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante C](automations/tasks/state-todo-read-with-branches-ad85ca77/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf — Variante D](automations/tasks/state-todo-read-with-branches-c96c1391/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Eine Aufgabenliste abfragen · mit Wartezeit im Ablauf](automations/tasks/state-todo-read-with-delay/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Eine Aufgabenliste abfragen · mit Bedingungen im Ablauf](automations/tasks/threshold-state-todo-read-with-branches/README.md) | Wenn ein Messwert eine eingestellte Grenze überschreitet oder unterschreitet; Wenn sich ein Wert oder Zustand ändert |

<a id="tasks-edit"></a>

#### Einträge bearbeiten (3 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Eine Aufgabenliste lesen und bearbeiten · mit Bedingungen im Ablauf — Variante A](automations/tasks/periodic-todo-read-update-with-branches-67bcce5a/README.md) | In einem regelmäßig wiederholten Zeitabstand |
| [Eine Aufgabenliste lesen und bearbeiten · mit Bedingungen im Ablauf — Variante B](automations/tasks/periodic-todo-read-update-with-branches-79a8b952/README.md) | In einem regelmäßig wiederholten Zeitabstand |
| [Eine Aufgabenliste lesen und bearbeiten · mit Bedingungen im Ablauf — Variante C](automations/tasks/periodic-todo-read-update-with-branches-a6071dba/README.md) | In einem regelmäßig wiederholten Zeitabstand |

<a id="tasks-remove"></a>

#### Einträge entfernen (1 Vorlage)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Eine Aufgabenliste lesen und Einträge entfernen · mit Bedingungen im Ablauf](automations/tasks/periodic-todo-read-remove-with-branches/README.md) | In einem regelmäßig wiederholten Zeitabstand |


</details>

<a id="switches"></a>

<details>
<summary><strong>Schalter und Steckdosen</strong> · 16 Vorlagen</summary>

**Direkt zu:** [Einschalten (4)](#switches-on) · [Ausschalten (3)](#switches-off) · [Umschalten (4)](#switches-toggle) · [Ein- und Ausschalten (5)](#switches-on-off)

<a id="switches-on"></a>

#### Einschalten (4 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Einen Schalter einschalten · mit Wartezeit im Ablauf](automations/switches/mqtt-switch-on-with-delay/README.md) | Wenn eine MQTT-Nachricht ankommt |
| [Einen Schalter einschalten](automations/switches/state-switch-on/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Einen Schalter einschalten · mit Wartebedingung im Ablauf](automations/switches/state-template-switch-on-with-wait/README.md) | Wenn sich ein Wert oder Zustand ändert; Wenn eine selbst festgelegte Bedingung zutrifft |
| [Einen Schalter einschalten](automations/switches/template-switch-on/README.md) | Wenn eine selbst festgelegte Bedingung zutrifft |

<a id="switches-off"></a>

#### Ausschalten (3 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Einen Schalter ausschalten · mit Wartebedingung im Ablauf](automations/switches/state-switch-off-with-wait/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Einen Schalter ausschalten](automations/switches/template-switch-off/README.md) | Wenn eine selbst festgelegte Bedingung zutrifft |
| [Einen Schalter ausschalten · mit Wartebedingung im Ablauf](automations/switches/triggered-switch-off-with-wait/README.md) | Der Auslöser muss noch eingerichtet werden |

<a id="switches-toggle"></a>

#### Umschalten (4 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Einen Schalter zwischen Ein und Aus umschalten](automations/switches/device-switch-toggle/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Einen Schalter zwischen Ein und Aus umschalten](automations/switches/state-switch-toggle/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Einen Schalter zwischen Ein und Aus umschalten — Variante A](automations/switches/triggered-switch-toggle-24cc2d6e/README.md) | Der Auslöser muss noch eingerichtet werden |
| [Einen Schalter zwischen Ein und Aus umschalten — Variante B](automations/switches/triggered-switch-toggle-c9419015/README.md) | Der Auslöser muss noch eingerichtet werden |

<a id="switches-on-off"></a>

#### Ein- und Ausschalten (5 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Schalter ein- und ausschalten · mit Wartebedingung im Ablauf](automations/switches/state-periodic-switch-on-off-with-wait/README.md) | Wenn sich ein Wert oder Zustand ändert; In einem regelmäßig wiederholten Zeitabstand |
| [Schalter ein- und ausschalten · mit Bedingungen im Ablauf](automations/switches/state-switch-on-off-with-branches/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Schalter ein- und ausschalten · mit Wartezeit im Ablauf — Variante A](automations/switches/state-switch-on-off-with-delay-91d3deba/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Schalter ein- und ausschalten · mit Wartezeit im Ablauf — Variante B](automations/switches/state-switch-on-off-with-delay-d9a93573/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Schalter ein- und ausschalten · mit Wartebedingung im Ablauf](automations/switches/threshold-switch-on-off-with-wait/README.md) | Wenn ein Messwert eine eingestellte Grenze überschreitet oder unterschreitet |


</details>

<a id="voice"></a>

<details>
<summary><strong>Sprache und Durchsagen</strong> · 1 Vorlage</summary>

**Direkt zu:** [Durchsagen und Vorlesen (1)](#voice-announcements)

<a id="voice-announcements"></a>

#### Durchsagen und Vorlesen (1 Vorlage)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Durchsagen und Sprachausgabe nutzen](automations/voice/state-voice-announce-speak/README.md) | Wenn sich ein Wert oder Zustand ändert |


</details>

<a id="notifications"></a>

<details>
<summary><strong>Nachrichten und Hinweise</strong> · 11 Vorlagen</summary>

**Direkt zu:** [Nachrichten versenden (9)](#notifications-messages) · [Hinweise in Home Assistant (2)](#notifications-ha-notices)

<a id="notifications-messages"></a>

#### Nachrichten versenden (9 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Nachrichten senden — Variante A](automations/notifications/device-notification-send-4fffe63e/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Nachrichten senden — Variante B](automations/notifications/device-notification-send-6b699d26/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Nachrichten senden — Variante C](automations/notifications/device-notification-send-8e742eeb/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Nachrichten senden · mit Wartezeit im Ablauf](automations/notifications/device-notification-send-with-delay/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Nachrichten senden · mit Bedingungen im Ablauf](automations/notifications/periodic-notification-send-with-branches/README.md) | In einem regelmäßig wiederholten Zeitabstand |
| [Nachrichten senden — Variante A](automations/notifications/state-notification-send-0989a580/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Nachrichten senden — Variante B](automations/notifications/state-notification-send-3e58df61/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Nachrichten senden — Variante C](automations/notifications/state-notification-send-a0e2d0da/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Nachrichten senden](automations/notifications/state-scheduled-notification-send/README.md) | Wenn sich ein Wert oder Zustand ändert; Zu einer eingestellten Uhrzeit |

<a id="notifications-ha-notices"></a>

#### Hinweise in Home Assistant (2 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Nachrichten und Hinweise ausgeben — Variante A](automations/notifications/device-notifications-create-notify-42c8182d/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Nachrichten und Hinweise ausgeben — Variante B](automations/notifications/device-notifications-create-notify-713dfa68/README.md) | Wenn ein Gerät ein Ereignis meldet |


</details>

<a id="helpers"></a>

<details>
<summary><strong>Zähler und gespeicherte Werte</strong> · 6 Vorlagen</summary>

**Direkt zu:** [Virtuelle Schalter (4)](#helpers-switches) · [Zähler verändern (1)](#helpers-counters) · [Texte speichern (1)](#helpers-text)

<a id="helpers-switches"></a>

#### Virtuelle Schalter (4 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Einen gespeicherten Ein/Aus-Wert ausschalten](automations/helpers/scheduled-input-boolean-off/README.md) | Zu einer eingestellten Uhrzeit |
| [Gespeicherte Ein/Aus-Werte ändern · mit Bedingungen im Ablauf](automations/helpers/scheduled-input-boolean-on-off-with-branches/README.md) | Zu einer eingestellten Uhrzeit |
| [Gespeicherte Ein/Aus-Werte ändern · mit Wartezeit im Ablauf](automations/helpers/state-input-boolean-on-off-with-delay/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Gespeicherte Ein/Aus-Werte ändern · mit Bedingungen im Ablauf](automations/helpers/state-scheduled-input-boolean-on-off-with-branches/README.md) | Wenn sich ein Wert oder Zustand ändert; Zu einer eingestellten Uhrzeit |

<a id="helpers-counters"></a>

#### Zähler verändern (1 Vorlage)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Einen Zähler erhöhen](automations/helpers/device-counter-increment/README.md) | Wenn ein Gerät ein Ereignis meldet |

<a id="helpers-text"></a>

#### Texte speichern (1 Vorlage)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Einen Textwert speichern](automations/helpers/template-input-text-value/README.md) | Wenn eine selbst festgelegte Bedingung zutrifft |


</details>

<a id="system"></a>

<details>
<summary><strong>Weitere Abläufe und Geräteaktionen</strong> · 23 Vorlagen</summary>

**Direkt zu:** [Eigene Skripte (6)](#system-scripts) · [Gerätefunktionen und Tasten (1)](#system-device-controls) · [MQTT-Nachrichten (3)](#system-mqtt) · [Andere Automationen schalten (1)](#system-automations) · [Wetterdaten abrufen (1)](#system-weather) · [Wartung und Protokolle (1)](#system-maintenance) · [Noch einzurichtende Aktionen (10)](#system-unfinished)

<a id="system-scripts"></a>

#### Eigene Skripte (6 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Ein vorhandenes Skript ausführen](automations/system/event-script-run/README.md) | Wenn ein festgelegtes Ereignis eintritt |
| [Ein vorhandenes Skript ausführen · mit Bedingungen im Ablauf — Variante A](automations/system/mqtt-script-on-with-branches/README.md) | Wenn eine MQTT-Nachricht ankommt |
| [Ein vorhandenes Skript ausführen](automations/system/mqtt-script-run/README.md) | Wenn eine MQTT-Nachricht ankommt |
| [Ein vorhandenes Skript ausführen · mit Bedingungen im Ablauf — Variante B](automations/system/mqtt-script-run-with-branches/README.md) | Wenn eine MQTT-Nachricht ankommt |
| [Ein vorhandenes Skript ausführen](automations/system/periodic-script-run/README.md) | In einem regelmäßig wiederholten Zeitabstand |
| [Ein vorhandenes Skript ausführen](automations/system/state-scheduled-script-run/README.md) | Wenn sich ein Wert oder Zustand ändert; Zu einer eingestellten Uhrzeit |

<a id="system-device-controls"></a>

#### Gerätefunktionen und Tasten (1 Vorlage)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Mehrere Funktionen verbinden · mit Wartezeit im Ablauf](automations/system/state-system-press-select-option-with-delay/README.md) | Wenn sich ein Wert oder Zustand ändert |

<a id="system-mqtt"></a>

#### MQTT-Nachrichten (3 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Eine MQTT-Nachricht senden](automations/system/periodic-mqtt-publish/README.md) | In einem regelmäßig wiederholten Zeitabstand |
| [Eine MQTT-Nachricht senden — Variante A](automations/system/state-mqtt-publish-03a56ab8/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Eine MQTT-Nachricht senden — Variante B](automations/system/state-mqtt-publish-4d55a0f6/README.md) | Wenn sich ein Wert oder Zustand ändert |

<a id="system-automations"></a>

#### Andere Automationen schalten (1 Vorlage)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Andere Automationen aktivieren und deaktivieren · mit Wartezeit im Ablauf](automations/system/device-automation-on-off-with-delay/README.md) | Wenn ein Gerät ein Ereignis meldet |

<a id="system-weather"></a>

#### Wetterdaten abrufen (1 Vorlage)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Mehrere Funktionen verbinden · mit Wartezeit im Ablauf](automations/system/state-periodic-system-custom-action-get-forecasts-with-delay/README.md) | Wenn sich ein Wert oder Zustand ändert; In einem regelmäßig wiederholten Zeitabstand |

<a id="system-maintenance"></a>

#### Wartung und Protokolle (1 Vorlage)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Mehrere Funktionen verbinden](automations/system/periodic-system-reload-config-entry-write/README.md) | In einem regelmäßig wiederholten Zeitabstand |

<a id="system-unfinished"></a>

#### Noch einzurichtende Aktionen (10 Vorlagen)

| Vorlage | Wann startet sie? |
| --- | --- |
| [Eigene Aktion einrichten — Variante A](automations/system/device-generic-action-15407118/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Eigene Aktion einrichten — Variante B](automations/system/device-generic-action-15407118-a/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Eigene Aktion einrichten — Variante C](automations/system/device-generic-action-ddc77372/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Eigene Aktion einrichten — Variante D](automations/system/device-generic-action-f594a0ff/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Eigene Aktion einrichten · mit Bedingungen im Ablauf](automations/system/device-generic-action-with-branches/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Eigene Aktion einrichten · mit Wartebedingung im Ablauf — Variante A](automations/system/device-generic-action-with-wait-31e6d1d6/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Eigene Aktion einrichten · mit Wartebedingung im Ablauf — Variante B](automations/system/device-generic-action-with-wait-4ebede39/README.md) | Wenn ein Gerät ein Ereignis meldet |
| [Eigene Aktion einrichten · mit Bedingungen im Ablauf](automations/system/periodic-generic-action-with-branches/README.md) | In einem regelmäßig wiederholten Zeitabstand |
| [Eigene Aktion einrichten](automations/system/state-generic-action/README.md) | Wenn sich ein Wert oder Zustand ändert |
| [Eigene Aktion einrichten](automations/system/triggered-generic-action/README.md) | Der Auslöser muss noch eingerichtet werden |


</details>

<!-- catalogue:end -->

## Fragen beim Einrichten?

In der **[Anleitung für den Einstieg](how-to/get-started.md)** findest du die Menüpunkte in Home Assistant, eine Erklärung der Platzhalter und Hilfe beim Testen.

Ein grüner GitHub-Haken bestätigt die Prüfungen dieser Sammlung. Ob eine angepasste Vorlage mit deinen Geräten funktioniert, prüfst du in deinem Home Assistant.

<details>
<summary><strong>Für Mitwirkende: Dokumentation und Prüfungen pflegen</strong></summary>

Die Übersicht und die Beschreibungen werden automatisch erzeugt. Die technischen Ordnernamen bleiben stabil; die Texte für Leser werden aus geprüften, allgemeinen Angaben erstellt.

```sh
python -m pip install -r requirements-dev.txt
python scripts/catalogue.py --write
python scripts/catalogue.py --check
```

- [Eine Vorlage dokumentieren](how-to/document-an-automation.md)
- [Datenschutz und Sicherheitsprüfungen](how-to/security-and-privacy.md)
- [Checkliste für automatisierte Beiträge](how-to/agent-documentation-checklist.md)

Die GitHub-Prüfungen laufen bei jedem neuen oder wieder geöffneten Pull Request, bei neuen Commits, beim Wechsel zwischen Entwurf und Review sowie bei Änderungen an Titel, Beschreibung oder Zielbranch.

</details>
