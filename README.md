# DSGVOIntegration

DSGVOIntegration ist ein einfacher Demonstrator für verschiedene Ansätze der
DSVO-konformen Intregration von Social-Media-Bereichen in Websieten
(Social-Media-Widgets).

## Hintergrund

Für die Social-Media-Integration in Webseiten, z.B. in der Form von 
Teilen(Share)-Buttons oder dem Anzeigen einer Twitter-Timeline,
werden von den Betreibern sozialer Netzwerke Standard-Plug-ins zur
Verfügung gestellt. Das Problem: Bereits beim Besuch einer mit derartigen
Plug-ins ausgestatteten Webseite, werden Daten an die Betreiber der
entsprechenden sozialen Netzwerke übertragen - auch wenn die Webseitenbesucher
dort gar kein Konto haben, bzw. die Funktion gar nicht nutzen möchten. Dieses
sogenannte Tracking passiert oft unbewusst, ist meist unerwünscht und dazu
noch aus datenschutzrechtlicher Sicht hochproblematisch, da die Nutzenden
dafür oft keine Zustimmung erteilt haben.

## Umsetzungsbeispiele

DSGVOIntegration zeigt drei unterschiedlich komplexe Ansätze, bei denen keine
Daten an die Betreiber sozialer Netzwerke übertragen werden. Die Datei
**no-embed.html** zeigt ein Beispiel einer einfachen Verlinkung. In 
**two-click-embed.html** finden Sie die sogenannte Zwei-Klick-Lösung.
**api-embed.html** ist die komplexeste aber auch eleganteste Lösung zur
Anzeige von Social-Media-Inhalten. Dabei werden die Daten serverseitig über
eine API abgefragt und dann auf der Website eingebunden. Das Beipiel wurde
mithilfe von Python realisiert. Denkbar ist aber auch die Verwendung anderer
Sprachen, wie beispielsweise PHP.

Die Dateien **no-embed.html**, **und two-click-embed.html** und
**api-embed.html** befinden sich im Ordner **templates**.    


# Installation

Alle HTML-Dateien im Ordner Templates können einfach eingesehen werden.
**no-embed.html** und **two-click-embed.html** sind direkt im Browser
lauffähig. Es ist keine weitere Installation erforderlich. Für das Beispiel
in **api-embed.html** werden für den hier vorliegenden Demonstrator **Python**,
das Python-Modul **tweepy**, ein Twitter-Account und Keys für eine Twitter-App
benötigt.


## Ubuntu Linux

Unter Ubuntu ist Python in der Regel installiert, lediglich **tweepy** wird für
die Abfrage von Tweets benötigt.

```
sudo apt-get install python-tweepy
```

Anschließend kann mit **git** installiert und der Server mit der Eingabe von
**./start** gestartet werden.

```
git clone https://github.com/e-teachingorg/DSGVOIntegration.git
cd DSGVOIntegration
./start
```

Folgendes sollte zu sehen sein


```
./start
Webserver wird gestartet auf Port 10080
```

## Windows

1. Falls nicht vorhanden, muss Python 2 oder 3 (https://www.python.org)
installiert werden. Achten Sie darauf, bei der Installation
**Add Python to PATH** auszuwählen, damit Python später von einem beliebigen
Ort ausgeführt werden kann.

2. Im zweiten Schritt erfolgt die Installation des Python-Moduls **tweepy**.
Dazu öffnen Sie die Eingabeaufforderung (und falls Python nicht im PATH verfügbar
ist, bewegen sich in den Ordner, wo Python installiert ist), geben folgendes
ein und drücken Enter:


```
C:\Python27>python.exe -m pip install tweepy
```

3. Anschließend laden Sie DSGVOIntegration von
[der Projektseite](https://github.com/e-teachingorg/DSGVOIntegration)
herunter (Clone or download, Download ZIP), enpacken die ZIP-Datei, öffnen den
Ordner **SGVOIntegration**

4. Mit einem Klick auf start.py sollte sich ein Fenster öffnen in dem folgendes
steht: Webserver wird gestartet auf Port 10080

# Start

Ein einfacher Webserver läuft nun auf Port 10080. Öffnen Sie einen Browser und
geben Sie folgende URL ein:

```
http://localhost:10080/
```

Sie sollte eine Twittertimeline mit Beispieldaten sehen. Weitere Beispiele finden
Sie über folgende Adressen

```
http://localhost:10080/two-click-embed.html
http://localhost:10080/no-embed.html
```

# Konfiguration

Das Beispiel mit der Twitter-Timeline basiert auf der Nutzung von Daten direkt
von der Twitter-API. Auf diese Weise ist es möglich, eine Timeline auf einer
Website einzubinden, ohne das Widget von Twitter zu nutzen und damit auch keine
ungewollten Traker zu installieren. Um die API nutzen zu können, benötigen Sie
einen Account bei Twitter und müssen im
[Developper-Bereich bei Twitter](https://developer.twitter.com/en/apps) eine App
registrieren. Die dabei erhaltenen Keys werden in die Datei config.py eingetragen.

Im Ordner **dsgvointegration** finden Sie die Datei **config.py**.


## config.py

Wenn Sie bereits eine Twitter-App angemeldet haben, können Sie die
entspechenden Daten (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN,
ACCESS_TOKEN_SECRET) dort eingeben. Ansonsten müssen sie sich erst die
entspechenden Keys erstellen.

Wenn Sie Ihre Keys eingetragen haben, setzen Sie den Wert **REAL_TIMELINE**
auf **True** und starten die Anwendung erneut. Nun sollten die Tweets Ihrer
Timeline zu sehen sein. Achtung: Die Anzahl der Anfragen an die API ist
begrenzt! Falls Sie planen, dass Szenario in einem Produktivbetrieb einzusetzen,
müssen Sie die Ergebnisse der Anfragen zwischenspeichern und die Abfragen auf eine
Abfrage alle 15 Minuten begrenzen.

```
REAL_TIMELINE = True
```

Außerdem können Sie in der config.py die PORT_NUMMER für den Webserver anpassen
