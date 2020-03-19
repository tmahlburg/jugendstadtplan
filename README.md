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
