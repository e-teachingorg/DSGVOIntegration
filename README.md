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
in **api-embed.html** wird für den hier vorliegenden Demonstrator **Python**
und das Python-Modul **tweepy** benötigt.


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

3. Aschließend laden Sie DSGVOIntegration von
https://github.com/e-teachingorg/DSGVOIntegration herunter (Clone or download,
Download ZIP), enpacken die ZIP-Datei, öffnen den Ordner **SGVOIntegration**

4. Mit einem Klick auf start.py sollte sich ein Fenster öffnen in dem folgendes
steht: Webserver wird gestartet auf Port 8010
