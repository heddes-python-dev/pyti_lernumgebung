# Mitwirken an Pyti

Danke für dein Interesse, Pyti zu verbessern! Willkommen sind Fehlerberichte,
Ideen, Verbesserungen an der Dokumentation, neue Lernaufgaben und
Codebeiträge.

## Projekt forken und lokal einrichten

1. Melde dich bei GitHub an und erstelle über **Fork** eine Kopie von
   [heddes-python-dev/pyti_lernumgebung](https://github.com/heddes-python-dev/pyti_lernumgebung)
   in deinem eigenen GitHub-Konto.
2. Klone deinen Fork. Ersetze `<DEIN-GITHUB-NAME>` durch deinen GitHub-Namen:

   ```bash
   git clone https://github.com/<DEIN-GITHUB-NAME>/pyti_lernumgebung.git
   cd pyti_lernumgebung
   ```

3. Richte eine virtuelle Umgebung ein und installiere die Abhängigkeiten:

   ```bash
   python -m venv .venv
   ```

   Linux oder macOS:

   ```bash
   source .venv/bin/activate
   ```

   Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   Danach auf allen Plattformen:

   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

## Feature-Branch erstellen

Erstelle für jede Änderung einen eigenen Branch auf Basis von `master`:

```bash
git switch master
git pull origin master
git switch -c feature/kurze-beschreibung
```

Für Fehlerbehebungen kannst du statt `feature/` den Präfix `fix/` verwenden.
Nutze einen kurzen, aussagekräftigen Namen, zum Beispiel
`feature/level-hinweise` oder `fix/reset-button`.

Setze deine Änderung möglichst gezielt um und ergänze oder aktualisiere Tests,
wenn sich Verhalten ändert. Vermeide es, Zugangsdaten, persönliche Daten,
lokale Konfigurationen oder die virtuelle Umgebung einzuchecken.

## Änderungen prüfen

Führe vor dem Pull Request die Tests und grundlegenden Prüfungen aus:

```bash
python -m unittest discover -s tests -v
python -m compileall -q pyti_app tests docs *.py
git diff --check
```

Unter Linux ohne grafische Anzeige:

```bash
QT_QPA_PLATFORM=offscreen python -m unittest discover -s tests -v
```

Prüfe außerdem, dass keine Python-Datei die projektweite Grenze von
150 Zeilen überschreitet. Die Testsuite enthält dafür einen eigenen Test:

```bash
python -m unittest tests.test_module_sizes -v
```

## Pull Request öffnen

1. Committe deine Änderung mit einer kurzen, aussagekräftigen Nachricht.
2. Push den Branch zu deinem Fork:

   ```bash
   git push -u origin feature/kurze-beschreibung
   ```

3. Öffne auf GitHub einen Pull Request von deinem Branch nach
   `heddes-python-dev/pyti_lernumgebung:master`.
4. Beschreibe das Problem und die Lösung, nenne relevante Tests und füge bei
   sichtbaren Änderungen nach Möglichkeit einen Screenshot hinzu.

Bei einem Fehlerbericht helfen eine genaue Beschreibung der Schritte zur
Wiederholung, das Betriebssystem und die Python-Version. Teile keine
Passwörter, Tokens oder sonstigen sensiblen Daten.

## Sicherheitshinweis

Pyti führt Lernskripte mit normalem Python im Anwendungsprozess aus und ist
keine Sandbox. Führe nur Skripte aus, denen du vertraust. Melde vermutete
Sicherheitsprobleme nicht als öffentliches Issue mit ausnutzbaren Details;
kontaktiere zuerst die Projektverantwortlichen über GitHub.
