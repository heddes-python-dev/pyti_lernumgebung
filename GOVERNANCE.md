# Projektverantwortung und Review

Pyti wird derzeit von einem Maintainer-Konto betreut. Die aktuelle
Repository-Verantwortung liegt bei
[@heddes-python-dev](https://github.com/heddes-python-dev). Dieses Konto ist
für die Entscheidung über Pull Requests, Releases und die Koordination von
Sicherheitsmeldungen zuständig. Weitere Maintainer werden ausdrücklich im
Repository benannt, sobald sie diese Verantwortung übernehmen.

## Pull Requests

- Änderungen werden über Pull Requests nach `master` vorgeschlagen.
- Der Maintainer prüft Zweck, Umfang, Tests und mögliche Nebenwirkungen und
  fordert bei Bedarf Anpassungen an.
- Die CI muss für alle Matrix-Jobs erfolgreich sein, bevor eine Änderung
  angenommen wird.
- Sicherheitsrelevante Änderungen brauchen zusätzlich eine gezielte
  Sicherheitsprüfung. Die CI oder ein Code-Review allein ist keine
  Sicherheitsfreigabe.
- Die direkte Änderung von `master` ist für Beiträge nicht vorgesehen.

GitHub-Branch-Protection ist derzeit nicht aktiviert. Die Review- und
CI-Anforderungen sind damit der dokumentierte Prozess, werden aber technisch
nicht durch GitHub erzwungen. Da es aktuell nur einen Maintainer gibt, wird
eine verpflichtende zweite Freigabe erst eingerichtet, wenn eine zweite
unabhängige Person die Maintainer-Verantwortung übernehmen kann.

## Releases

Der Maintainer entscheidet über Versionierung und Veröffentlichung. Ein
Release soll erst erstellt werden, wenn die Tests auf der CI-Matrix
erfolgreich sind. Die Release-Notizen sollen Nutzeränderungen, getestete
Plattformen, bekannte Einschränkungen und notwendige Systemvoraussetzungen
aufführen. Sicherheitsfixes werden abgestimmt mit der betroffenen Version
veröffentlicht; ihre Verfügbarkeit wird in den Release-Notizen kenntlich
gemacht.

## Verantwortung für Sicherheit

Der Maintainer koordiniert vertrauliche Meldungen, bestätigt sie nach
Möglichkeit zeitnah und stimmt Untersuchung, Behebung und Veröffentlichung
mit der meldenden Person ab. Weil derzeit keine unabhängige interne
Sicherheitsprüfung verfügbar ist, wird die offene Freigabe für nicht
vertrauenswürdige Skripte und breiten Schuleinsatz nicht durch einen
gewöhnlichen Pull-Request-Review ersetzt.

Siehe [SECURITY.md](SECURITY.md) für den vertraulichen Meldeweg.
