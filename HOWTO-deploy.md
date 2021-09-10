# HOWTO: Deployment

In diesem HOWTO wird eklärt, wie man das Projekt auf einem Server installiert und ausführt.

## Holen

Mit ```git```:
```
$ git clone https://github.com/tmahlburg/jugendstadtplan.git  # oder:
$ git clone git@github.com:tmahlburg/jugendstadtplan.git

$ cd jugendstadtplan
```
Mit ```wget```:
```
$ wget https://github.com/tmahlburg/jugendstadtplan/archive/refs/heads/master.zip
$ unzip master

$ cd master
```

## Inhalt der statischen Seiten ändern

Der Inhalt der Seiten ```Über``` und ```Impressum``` kann in den Dateien ```jugendstadtplan/templates/about.html``` und ```jugendstadtplan/templates/impressum.html``` geändert werden.

## Abhängigkeiten

Installiere certbot, python3-certbot-nginx, nginx und pipenv3.

## nginx

Ändere den Pfad in der ```nginx.conf``` zum Pfad, der dem Pfad zum Projekt entspricht, trage den gewünschten Domainnamen ein und kopiere die Datei in /etc/nginx/conf.d/:

```
# rm /etc/nginx/conf.d/sites-enabled/default
# cp nginx.conf /etc/nginx/conf.d/
```

Lade deine nginx-Konfiguration neu.

```
# nginx -s reload # ODER
# systemctl restart nginx
```

## gunicorn

Wechsle in das pipenv:
```
$ pipenv install # only needed the first time
$ pipenv shell
```
Jetzt muss die Datenbank migriert, die statischen Dateien gesammelt und ein Nutzeraccount erstellt werden:
```
$ ./manage.sh setup_prod
```
Bevor das Projekt ausgeführt werden kann, muss noch die Datei ```prod.env``` mit einem SECRET_KEY und den ALLOWED_HOSTS gefüllt werden. Außerdem kann hier eingestellt werden, auf welche Koordinaten die Karte zentriert sein soll. Danach kann einfach der Server ausgeführt werden, und das Projekt ist erreichbar!
```
$ ./manage.sh run_gunicorn
```

## let's encrypt

Generiere ein Zertifikat für die gewünschte Domain:
```
# certbot --nginx
```
Unter Umständen muss zuvor noch ```/usr/sbin/``` dem ```PATH``` hinzugefügt werden. Das so erstellte Zertifikat läuft nach sechs Monaten ab. Danach kann das Skript ```renew_cert.sh``` einfach ausgeführt werden, um das Zertifikat zu aktualisieren.

## systemd service

Diesem Repo liegt außerdem eine systemd-service-datei bei: ```jugendstadtplan.service```. Auf kompatiblen Platformen kann diese in ```/etc/systemd/system``` kopiert werden und dann, nachdem die korrekten Pfade eingetragen wurden, mit
```
# systemctl start jugendstadtplan
```
gestartet werden. Mit
```
# systemctl enable jugendstadtplan
```
wird der Service bei jedem Start des Servers mitgestartet. Mit
```
# systemctl restart jugendstadtplan
```
kann der Service neugestartet werden, z.B. nach einem Update.
