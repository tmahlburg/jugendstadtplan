# jugendstadtplan

## Vorraussetzungen
mit Docker: Docker, docker-compose

nativ: python3, pip3, pipenv

## Ausführung
**Repo holen:**
```
$ git clone https://github.com/tmahlburg/jugendstadtplan.git  # oder:
$ git clone git@github.com:tmahlburg/jugendstadtplan.git

$ cd jugendstadtplan
```
**Docker**:

```
# docker-compose up
```

**nativ**:
```
$ pipenv install
$ pipenv shell
$ python3 manage.py migrate
$ ./manage.sh setup_admin
$ python3 manage.py runserver
```
*(nur eins von beidem ist nötig)*

Die Seite ist dann unter http://localhost:8000 zu erreichen. Außerdem wird ein user account mit den Anmeldedaten admin:admin angelegt. NUR FÜR ENTWICKLUNGSZWECKE!

## Links

**python:**

- [Hitchhiker's Guide to Python](https://docs.python-guide.org) - fortgeschrittenere Sachen, auch zu guter Einrichtung

**django:**

- [Django Doku](https://docs.djangoproject.com/en/3.0/)
- [Django unittests](https://docs.djangoproject.com/en/3.0/topics/testing/)

**docker:**

- [Docker Doku](https://docs.docker.com)
- [docker-compose Doku](https://docs.docker.com/compose/)
- [Installationsanleitungen](https://docs.docker.com/install/#supported-platforms)

**github actions:**
- [offizielle GitHub Actions Doku](https://help.github.com/en/actions)
