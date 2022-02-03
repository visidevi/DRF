## Profundizando en Django

Este repositorio está diseñado para profundizar en los conceptos de django mientras se sigue el curso de open webinars Profundizando en Django.

Para empezar a desarrollar mejor este repositorio sigue las siguientes instrucciones.

### Getting Started

Asegurate de tener python >= 3.7

Lo primero es clonar el repositorio:

```bash
git clone https://github.com/juanbenitopr/ProfundizandoDjango.git
cd ProfundizandoDjango
```

Entonces instalamos las dependencias:

```bash
pip install -r requirements.txt
```

Ahora ya deberíamos tener todo lo necesario para empezar a desarrollar utilizando este proyecto.


### Componentes

El proyecto está divido en los siguientes componentes:

- **fetlix**: Directorio donde Django guarda toda la configuración.

- **series**: Aplicación que contiene toda la lógica de como gestiona fetlix las series.

- **users**: Aplicación de Django que contiene la lógica de gestión de usuarios del proyecto.

```

```
```
pip install -r  requirements.txt --extra-index-url https://pypi.python.org/simple
pip install djangorestframework-simplejwt --extra-index-url https://pypi.python.org/simple
pip install django-heroku --extra-index-url https://pypi.python.org/simple
pip install gunicorn --extra-index-url https://pypi.python.org/simple



```
Durante esta clase hemos visto una serie de comandos que os dejo aquí resumidos:

1. Crear fixtures de usuarios
`python [manage.py](http://manage.py/) dumpdata --format=json auth.user > fixtures/users.json`
python manage.py dumpdata --format=json auth.user > fixtures/users.json

2. Crear fixtures de series
`python [manage.py](http://manage.py/) dumpdata --format=json --pks 1 series.serie > fixtures/series.json`
python manage.py dumpdata --format=json --pks 1 series.serie > fixtures/series.json

3. crear fixtures de episodios
`python manage.py dumpdata --format=json --pks 1 series.episode >> fixtures/series.json`


Hay que ejecutarlas en el orden especificado. Para conseguir más información relativa a las fixtures de django podéis consultar:

https://docs.djangoproject.com/en/3.1/howto/initial-data/

https://code.djangoproject.com/wiki/Fixtures
```

### Coverage
```
coverage run manage.py test
coverage report -m
coverage run  --source='.' manage.py test
```
git add .
git commit -am "make it better"
git push heroku main