# Pyti Inspector (externes Werkzeug)

Der Pyti Inspector ist ein eigenständiges Companion-Tool für Live-Telemetrie
und Zustandsanzeige. Er gehört nicht zum Pyti-Quellcode, wird nicht mit Pyti
installiert und ist keine Voraussetzung für die Lernumgebung. Die optionale
Anbindung verändert keine Dateien im Pyti-Projekt: Ein externer Launcher
instrumentiert den Interpreter nur während des laufenden Prozesses.

## Start

Installiere Pyti und den Inspector getrennt. Der verwendete Python-Interpreter
muss PySide6 und die Abhängigkeiten beider Anwendungen bereitstellen. Starte
beide Anwendungen über den Launcher des Inspector-Projekts:

```bash
python /pfad/zu/Pyti-Inspector/launch_pyti.py /pfad/zu/pyti_lernprogramm
```

Wähle danach in Pyti ein Level und starte ein Skript. Wird Pyti direkt mit
`python main.py` gestartet, wird keine Inspector-Telemetrie gesendet. Ist der
Inspector nicht erreichbar, läuft Pyti über den externen Launcher ohne
Telemetrie weiter.

## Angezeigte Daten

Während einer Skriptausführung kann der Inspector die ausgeführten
Skriptzeilen, Aktionen und Sensorergebnisse, JSON-taugliche lokale Variablen,
Roboterposition, Blickrichtung, Inventar, Beeper, Wände und Fehler empfangen.
Die Fehleranzeige enthält die Fehlerdetails und die zuletzt ausgeführte Zeile.
Es ist kein interaktiver Debugger: Die Anwendung pausiert nicht und bietet
keinen vollständigen, live inspizierbaren Python-Call-Stack.

Werte werden in begrenzte JSON-Snapshots umgewandelt; große Sammlungen und
komplexe Objekte sind daher gekürzt oder nur als Typ dargestellt. Der
Inspector kann nur Daten anzeigen, die der externe Adapter explizit sendet.

## Schnittstelle und Grenzen

Der Inspector lauscht lokal auf `127.0.0.1:8765` und verwendet ein
versioniertes JSON-Lines-Protokoll. Der Adapter unterstützt Pyti durch
temporäre In-Memory-Instrumentierung von `BefehlsInterpreter`. Pyti leitet
Zeilen-, Aktions- und Fehlerereignisse über seine lokale Sandbox-Brücke an
den Adapter weiter; das Skript im isolierten Kindprozess erhält selbst keinen
Netzwerkzugriff. Ohne den Launcher wird kein Telemetrie-Handler eingerichtet.

Der lokale Listener ist nicht authentifiziert und für die Nutzung auf dem
eigenen Rechner vorgesehen. Sende keine Passwörter, Tokens oder persönlichen
Daten über die Telemetrie. Der Inspector schafft keine zusätzliche
Sicherheitsgrenze. Pyti isoliert Skripte auf Linux mit bubblewrap; auf anderen
Betriebssystemen wird die Ausführung verweigert. Eine unabhängige
Sicherheitsprüfung der Sandbox steht noch aus. Starte nur Skripte, denen du
vertraust.

Die eigenständige Software, der Demo-Sender, das Protokoll und die
Installationshinweise befinden sich im separaten Projektverzeichnis
`Pyti-Inspector`; maßgeblich ist dessen README.
