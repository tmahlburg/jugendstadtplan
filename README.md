# jugendstadtplan
Diese Software befindet sich aktuell in der Betaphase. Eine gehostete Version ist unter [jugendstadtplan-greifswald.de](https://jugendstadtplan-greifswald.de) zu sehen.

## Vorraussetzungen

python3, pip, pipenv

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

Die Seite ist dann unter http://localhost:8000 zu erreichen. Außerdem wird ein user account mit den Anmeldedaten admin:admin angelegt. NUR FÜR ENTWICKLUNGSZWECKE!
