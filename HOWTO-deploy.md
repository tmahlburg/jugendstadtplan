# HOWTO: Deployment

In diesem HOWTO wird eklärt, wie man das Projekt auf einem Server installiert und ausführt.

## Holen

## Abhängigkeite

Installiere certbot, python3-certbot-nginx, nginx und pipenv3.

## nginx

Ändere den Pfad in der ```nginx.conf``` zum Pfad, der dem Pfad zum Projekt entspricht und kopiere die Datei in /etc/nginx/conf.d/:

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
Danach kann einfach der Server ausgeführt werden, und das Projekt ist erreichbar!
```
$ ./manage.sh run_gunicorn
```

## let's encrypt

Generiere ein Zertifikat für die gewünschte Domain:
```
# certbot --nginx
```
Unter Umständen muss zuvor noch ```/usr/sbin/``` dem ```PATH``` hinzugefügt werden.
