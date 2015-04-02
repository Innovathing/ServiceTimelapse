# ServiceTimelapse

Lance un timelapse avec les options spécifiées dans le fichier du daemon.

## Installation
Copier le fichier ```timelapse``` dans ```/etc/init.d/timelapse```.
On peut tester le service avec ```service timelapse start``` et ```service timelapse stop```.

## Lancer au démarrage
Une fois que le fichier ```/etc/init.d/timelapse``` existe, lancer ```insserv timelapse``` pour activer le service au démarrage. ```insserv -r timelapse``` pour l'enlever.
