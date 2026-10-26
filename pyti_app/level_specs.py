"""Lesbare Quelldaten für die 100 Standardlevel."""

LEVEL_SPECS = [
    ("Der erste Beeper", (0, 0), (4, 0), 0, "Gehe geradeaus und lerne moveForward()."),
    ("Der erste Dreh", (0, 4), (4, 1), 1, "Verbinde Geradeauslaufen mit einer ersten Drehung."),
    ("Eine Wand", (0, 2), (5, 2), 2, "Umgehe die einzelne Blockade."),
    ("Zwei Richtungen", (1, 1), (6, 4), 3, "Wechsle zwischen horizontalem und vertikalem Weg."),
    ("Die Ecke", (0, 5), (5, 0), 4, "Finde den Weg um die Eckbarriere."),
    ("Kleine Treppe", (0, 8), (6, 3), 5, "Folge dem Verlauf der Treppenwände."),
    ("Zickzack", (0, 0), (7, 4), 6, "Schlängle dich durch die versetzten Wände."),
    ("Die Gasse", (0, 6), (8, 6), 7, "Suche den Eingang zur freien Gasse."),
    ("Sackgasse", (1, 1), (8, 7), 8, "Erkenne die Sackgasse und nimm den Umweg."),
    ("Der Tunnel", (0, 5), (9, 5), 9, "Bleibe im schmalen Korridor auf Kurs."),
    ("Kreuzung", (2, 2), (9, 8), 10, "Wähle an mehreren Kreuzungen den richtigen Weg."),
    ("Umweg nach Norden", (0, 9), (8, 1), 11, "Umgehe die Barrieren und arbeite nach Norden."),
    ("Umweg nach Süden", (8, 0), (2, 10), 12, "Plane einen sicheren Weg nach Süden."),
    ("Das Karree", (2, 2), (10, 2), 13, "Umkreise den blockierten Innenbereich."),
    ("Das Kreuz", (4, 4), (0, 0), 14, "Entkomme aus dem Kreuzungsbereich und erreiche den Beeper."),
    ("Doppelter Korridor", (0, 2), (11, 8), 15, "Navigiere durch zwei hintereinanderliegende Korridore."),
    ("Die Spirale", (1, 1), (10, 10), 16, "Folge dem spiralförmigen Wandmuster nach innen."),
    ("Das Tor", (5, 12), (5, 1), 17, "Finde eine günstige Durchfahrt durch die Barriere."),
    ("Wand-Slalom", (0, 10), (12, 4), 18, "Weiche den versetzten Wänden im Slalom aus."),
    ("Das L-Labyrinth", (1, 10), (12, 1), 19, "Umgehe zwei lange L-förmige Hindernisse."),
    ("Drei Kammern", (0, 0), (12, 8), 20, "Durchquere drei getrennte Wandbereiche."),
    ("Der Haken", (2, 2), (1, 12), 21, "Finde den Ausgang aus dem hakenförmigen Aufbau."),
    ("Diagonale", (0, 12), (12, 0), 22, "Arbeite dich an der diagonalen Wandstruktur vorbei."),
    ("Die Schleife", (1, 1), (13, 11), 23, "Verlasse die Schleife und halte auf das Ziel zu."),
    ("Korridor-Netz", (0, 7), (13, 7), 24, "Wähle im Korridornetz die passende Abzweigung."),
    ("Der Innenhof", (7, 13), (7, 1), 25, "Durchquere den Innenhof ohne an einer Wand zu enden."),
    ("Vier Abzweigungen", (0, 0), (13, 13), 26, "Prüfe an jeder Abzweigung die freie Richtung."),
    ("Das Fenster", (2, 12), (12, 2), 27, "Nutze die Öffnungen im Fenster-Muster."),
    ("Schlangengänge", (0, 1), (13, 12), 28, "Folge den geschwungenen Gängen bis zum Ausgang."),
    ("Die Ringmauer", (1, 7), (13, 7), 29, "Finde die Lücke in der Ringmauer."),
    ("Doppelschleuse", (0, 13), (13, 0), 30, "Passiere zwei Schleusen mit jeweils einer Öffnung."),
    ("Das Raster", (1, 1), (13, 13), 31, "Überquere das dichte Raster Schritt für Schritt."),
    ("Labyrinth Bronze", (0, 0), (13, 9), 32, "Finde einen möglichst kurzen Weg durch das Labyrinth."),
    ("Labyrinth Silber", (2, 12), (12, 2), 34, "Nutze Sensoren, um Sackgassen zu erkennen."),
    ("Labyrinth Nord", (7, 13), (7, 0), 36, "Steige durch mehrere verschachtelte Korridore nach Norden."),
    ("Labyrinth Süd", (7, 0), (7, 13), 38, "Finde den Ausgang am anderen Ende des Labyrinths."),
    ("Das Irrgarten-Herz", (0, 7), (7, 7), 40, "Erreiche das Zentrum des großen Irrgartens."),
    ("Verlorene Kreuzung", (14, 14), (1, 1), 42, "Orientiere dich in einem dichten Kreuzungsnetz."),
    ("Die lange Schleife", (0, 14), (14, 0), 44, "Durchlaufe die lange Schleife ohne Abkürzung."),
    ("Labyrinth Gold", (1, 13), (13, 1), 46, "Finde im komplexen Muster den sicheren Zielkorridor."),
    ("Das große Labyrinth", (0, 0), (14, 14), 48, "Löse das vollständige Labyrinth mit Sensoren und Schleifen."),
    ("Meisterprüfung", (14, 14), (0, 0), 50, "Bewältige alle zuvor geübten Navigationsmuster."),
    ("Der letzte Korridor", (0, 7), (14, 7), 52, "Finde den versteckten Durchgang durch das Endspiel."),
    ("Vier Tore", (7, 14), (7, 0), 54, "Öffne gedanklich die vier Tore des Labyrinths."),
    ("Das Wendewerk", (0, 0), (14, 10), 56, "Plane viele Drehungen, ohne eine Sackgasse zu übersehen."),
    ("Die Tiefen", (14, 0), (0, 14), 58, "Dringe bis in die tiefste Kammer vor."),
    ("Labyrinth Diamant", (1, 1), (13, 13), 60, "Finde den Zielweg durch das nahezu vollständige Raster."),
    ("Der Endspurt", (0, 13), (14, 1), 62, "Halte trotz dichter Wände die Orientierung."),
    ("Meisterlabyrinth", (14, 14), (0, 0), 64, "Löse das anspruchsvollste bisherige Labyrinth."),
    ("Das große Finale", (0, 0), (14, 14), 66, "Finde den Weg zum letzten Beeper und beende die Lernstrecke."),
]

MAZE_MISSIONS = [
    ("Der erste Sprung", "Springe über die blockierte Verbindung im Labyrinth."),
    ("Sprung im Tunnel", "Nutze die Sprungstelle im schmalen Tunnel."),
    ("Die versperrte Ecke", "Finde den Umweg durch das Ecklabyrinth."),
    ("Kammerwechsel", "Verbinde die Kammern trotz blockierter Durchgänge."),
    ("Sprungkreuzung", "Wähle an der Kreuzung den passenden Sprung."),
    ("Der geheime Korridor", "Suche den versteckten Weg zwischen den Wänden."),
    ("Doppelte Abzweigung", "Prüfe jeden Abzweig, bevor du springst."),
    ("Der kurze Durchbruch", "Nutze den Sprung, ohne den Zielkorridor zu verfehlen."),
    ("Wand im Weg", "Überwinde die Wand im begehbaren Abschnitt."),
    ("Sprungprüfung Bronze", "Kombiniere Orientierung und Sprung im Labyrinth."),
    ("Das verschachtelte Tor", "Finde den Weg durch die ineinanderliegenden Gänge."),
    ("Das blockierte Tor", "Finde den Weg durch den blockierten Durchgang."),
    ("Korridorwechsel", "Wechsle sicher zwischen den schmalen Korridoren."),
    ("Die stille Kammer", "Finde die Verbindung aus der abgeschlossenen Kammer."),
    ("Sprungfolge", "Plane den Sprung, ohne die Orientierung zu verlieren."),
    ("Drei Wege", "Prüfe Sackgassen und wähle den passenden Durchgang."),
    ("Das versetzte Tor", "Nutze versetzte Sprungstellen im Labyrinth."),
    ("Die inneren Gänge", "Finde den Zugang zu den inneren Gängen."),
    ("Kreuz und Quer", "Verbinde die getrennten Bereiche mit gezielten Sprüngen."),
    ("Sprungprüfung Silber", "Löse das größere Labyrinth mit Sensoren und Sprüngen."),
    ("Die Kammerreihe", "Durchquere mehrere hintereinanderliegende Kammern."),
    ("Der lange Umweg", "Vergleiche Abzweigungen und halte den Zielkurs."),
    ("Das doppelte Raster", "Orientiere dich im dicht verzweigten Raster."),
    ("Verlorener Durchgang", "Finde den Durchgang zwischen den verschlossenen Gängen."),
    ("Der versiegelte Durchgang", "Finde den richtigen Sprung aus dem verschlungenen Gang."),
    ("Sprungnetz", "Nutze Sensoren, um Sprung und Richtungswechsel zu planen."),
    ("Der verschachtelte Irrgarten", "Finde aus den eng verzweigten Gängen zurück zum Ziel."),
    ("Kammerlabyrinth", "Durchquere die verzweigten Bereiche trotz blockierter Türen."),
    ("Die falsche Fährte", "Lass dich von Sackgassen nicht vom Ziel abbringen."),
    ("Sprungprüfung Gold", "Kombiniere längere Planung mit mehreren Sprüngen."),
    ("Die verschlungenen Gänge", "Folge den verwinkelten Korridoren bis zum Ziel."),
    ("Der verzweigte Pfad", "Finde das Ziel in den verzweigten Gängen."),
    ("Sprünge im Raster", "Unterscheide offene Korridore von blockierten Übergängen."),
    ("Die äußeren Gänge", "Durchlaufe die äußeren Korridore und finde den Zielweg."),
    ("Kreuzung der Kammern", "Wähle an jeder Kammerkreuzung einen sicheren Weg."),
    ("Das lange Tor", "Überwinde die Sprungstellen entlang des langen Korridors."),
    ("Der Irrgartenkern", "Finde den Weg durch die dicht verschachtelten Bereiche."),
    ("Verschachtelte Zonen", "Plane eine Route durch die ineinanderliegenden Labyrinthzonen."),
    ("Die letzte Abzweigung", "Prüfe die letzten Alternativen vor dem Ziel."),
    ("Sprungprüfung Diamant", "Löse das komplexe Raster mit einer durchdachten Sprungfolge."),
    ("Das große Sprunglabyrinth", "Nutze alle erlernten Strategien im großen Labyrinth."),
    ("Kammern ohne Karte", "Orientiere dich Schritt für Schritt durch unbekannte Kammern."),
    ("Der versperrte Zielweg", "Finde den Zielweg über mehrere Sprungübergänge."),
    ("Der lange Irrgarten", "Vermeide Sackgassen und plane die gesamte Route."),
    ("Sprungfolge Meister", "Kombiniere Sensoren, Schleifen und präzise Sprünge."),
    ("Das letzte Netz", "Finde im verzweigten Netz die Verbindung zum Ziel."),
    ("Meisterlabyrinth Nord", "Löse das große Nordlabyrinth mit mehreren Sprungbarrieren."),
    ("Meisterlabyrinth Süd", "Durchquere die verschachtelten Südkorridore."),
    ("Die finale Prüfung", "Setze Sensoren, Schleifen und Sprünge gezielt zusammen."),
    ("Das große Finale", "Bewältige das größte Labyrinth und erreiche den Ziel-Beeper."),
]


def level_nummer(index):
    if index == 100:
        return "1.0.0"
    if index < 10:
        return f"0.0.{index}"
    minor, patch = divmod(index - 10, 10)
    return f"0.{minor + 1}.{patch}"


def maze_level_specs():
    specs = []
    for index, (name, mission) in enumerate(MAZE_MISSIONS):
        stage, progress = divmod(index, 10)
        size = (4, 4, 4, 5, 5)[stage]
        jumps = (1, 1 + progress // 5, 2 + progress // 3,
                 4 + progress // 2, 6 + progress // 2)[stage]
        barrier = "Sprungbarriere" if jumps == 1 else "Sprungbarrieren"
        mission = f"{mission} Überwinde {jumps} {barrier} mit jump()."
        specs.append((name, size, jumps, mission))
    return specs
