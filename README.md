# DSGVOIntegration


DSGVOIntegration ist ein einfacher Demonstrator für verschiedene Ansätze der
DSVO-konformen Intregration von Social-Media-Widgets in Websites.

In den Dateien **no-embed.html**, **und two-click-embed.html** und
**api-embed.html** im Ordner **templates** finden sich Beispiele für eine
Integration. 

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
Webserver wird gestartet auf Port 8010
```

## Windows

1. Falls nicht vorhanden, muß Python 2 oder 3 (https://www.python.org)
installiert werden
2. Im zweiten Schritt erfolgt die Installation des Python-Moduls **tweepy**.
Dazu öffen Sie die Eingabeaufforderung, bewegen sich in den Ordner, wo Python
installiert ist und geben folgendes ein:


```
C:\Python27>python.exe -m pip install tweepy
```

3. Anschließend laden Sie DSGVOIntegration von
https://github.com/e-teachingorg/DSGVOIntegration herunter (Clone or download,
Download ZIP), enpacken die ZIP-Datei, öffnen den Ordner **SGVOIntegration**

4. Mit einem Klick auf start.py sollte sich ein Fenster öffnen in dem folgendes
steht: Webserver wird gestartet auf Port 8010

# Start

Ein einfacher Webserver läuft nun auf Port 8010. Öffnen Sie einen Browser und
geben Sie folgende URL ein:

```
http://localhost:8010/
```

Sie sollte eine Twittertimeline mit Beispieldaten sehen


# Konfiguration

Im Ordner **dsgvointegration** finden Sie die Datei **config.py**.


## config.py

Wenn Sie beireits eine Twitter-App angemeldet haben, können Sie die
entspechenden Daten (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN,
ACCESS_TOKEN_SECRET) dort eingeben. Ansonsten müssen sie sich erst die
entspechenden Keys erstellen. Mehr auf https://developer.twitter.com/en/apps

Wenn Sie ihre Keys eingetragen haben, setzen Sie den Wert **REAL_TIMELINE**
auf **True** und starten die Anwendung erneut. Nun sollten die Tweets Ihrer
Timeline zu sehen sein.

```
REAL_TIMELINE = True
```

Außerdem können Sie in dieser Datei die PORT_NUMMER für den Webserver anpassen
 