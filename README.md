# get_all_backups

## Quickstart

Um das Skript zu starten muss [Python 3](https://www.python.org/downloads/) installiert sein.
Es kann auch sein, das einer der Module wie tqdm nicht installiert wurde. Dieses kann dann durch den Befehl 

```sh
pip install tqdm
pip install [Modulname]
```

über das Terminal installiert werden.  
Anschließend kann man die Datei in einen leeren Ordner ausführen. Es sollte dann ein Fenster mit einer Progressbar erscheinen.

## Serverliste bearbeiten

Die Serverliste ist eine json Datei. Hier können die FTP Daten in der Vorlage eingepflegt werden.

```json
{
    "Websitename": {
        "hostname": "",
        "username": "",
        "password": "",
        "root": ""
    },
    "Websitename": {
        "hostname": "",
        "username": "",
        "password": "",
        "root": ""
    },
    "Websitename": {
        "hostname": "",
        "username": "",
        "password": "",
        "root": ""
    }
}
```

## Fehlerbehebung

Das Programm erstellt nach durchlaufen automatische eine Logdatei im selben Ordner, in der Fehler hineingeschrieben werden.
