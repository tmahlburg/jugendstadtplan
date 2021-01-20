# HOWTO: Deployment

In diesem HOWTO wird eklärt, wie man das Projekt auf einem Server installiert und ausführt.

## Holen

## Abhängigkeite

Installiere pipenv3 und nginx.

## nginx

Ändere den Pfad in der ```nginx.conf``` zum Pfad, der dem Pfad zum Projekt entspricht und kopiere die Datei in /etc/nginx/conf.d/:

```
# cp nginx.conf /etc/nginx/conf.d/
```

Lade deine nginx-Konfiguration neu.

```
# nginx -s reload
```

## gunicorn

Change into the pipenv:
```
$ pipenv install # only needed the first time
$ pipenv shell
```
After this, you can just run:
```
$ ./manage.sh run_gunicorn
```

## let's encrypt
