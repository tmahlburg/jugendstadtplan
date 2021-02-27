# HOWTO: Development

In diesem HOWTO wird erklärt, wie man das Projekt lokal auf seinem eigenen Rechner zu Entwicklungszwecken ausführen kann. Außerdem wird erklärt, wie die Testsuite ausgeführt wird

## Benötigte Software

- python3
- pip
- pipenv

## Ausführung

**Repo holen:**
```
$ git clone https://github.com/tmahlburg/jugendstadtplan.git  # oder:
$ git clone git@github.com:tmahlburg/jugendstadtplan.git

$ cd jugendstadtplan
```

**Ausführung**:
```
$ pipenv install
$ pipenv shell
$ python3 manage.py migrate
$ ./manage.sh setup_admin
$ python3 manage.py runserver
```

Die Seite ist dann unter http://localhost:8000 zu erreichen. Außerdem wird ein Nutzer mit den Anmeldedaten admin:admin angelegt.

**ACHTUNG**: Diese Art das Projekt auszuführen ist NUR FÜR ENTWICKLUNGSZWECKE gedacht!

## Tests

Die Ausführung der Tests erfolgt über den Befehl (vorrausgesetzt man befindet sich noch in der ```pipenv``` shell):
```
$ python3 manage.py test
```
