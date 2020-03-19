# jugendstadtplan
  *beste projekt*
  
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

```# docker-compose up```

**nativ**:
```
$ pipenv install
$ pipenv shell
$ python manage.py runserver 0:8000
```
*(nur eins von beidem ist nötig)*

Die Seite ist dann unter http://localhost:8000 zu erreichen.

## Links zu guter Dokumentation

Nicht, dass ich das alles gelesen hätte. Ich dachte nur es wär vielleicht nützlich das hier verlinkt zu haben. Kann man ja immer erweitern, wenn man was nützliches findet.

**python:**

- [Python Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide) - grundlegender Einstieg
- [Hitchhiker's Guide to Python](https://docs.python-guide.org) - fortgeschrittenere Sachen, auch zu guter Einrichtung
- [Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/) - offizieller Python style guide

**django:**

- [offizelle Django Doku](https://docs.djangoproject.com/en/3.0/)
- [unittests](https://docs.docker.com/install/#supported-platforms) - Dokumentation für die automatisierten Tests, die übrigens nach jedem push / pull request auf den Masterbranch ausgeführt werden

**docker:**

- [offizelle Docker Doku](https://docs.docker.com)
- [offiziele docker-compose doku](https://docs.docker.com/compose/)
- [Installationsanleitungen](https://docs.docker.com/install/#supported-platforms)

**github actions:**
- [offizielle GitHub Actions Doku](https://help.github.com/en/actions) - unsere CI
