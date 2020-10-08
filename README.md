# Sibill
Prueba Técnica que consiste en hacer una pequeña API Rest con Django

* Version 3.0.0

### Requisitos previos

Para este proyecto es necesario tener instalado:
* Python 3.7
* PostgreSql 9.6
* Virtualenv


### Instalación

Clonamos el proyecto.

```
$ git clone https://github.com/jelkinsp/sibill.git
```

Activamos el entorno virtual.

```
$ virtualenv -p python3.7 venv
$ source /venv/bin/activate
```
Instalamos las librerias necesarias.

```
$ pip install -r requirements.txt
```
y por ultimo introducimos los comandos para poder levantar Django.

```
$ python manage.py makemigrate
$ python manage.py sqlmigrate sibill_api 0005
$ python manage.py migrate
$ python manage.py runserver
```

## Tests

Los test de funcionalidad se encuentran en `sibill/test.py`

## Documentación

Se ha generado con `rest_framework_swagger` un endpoint con la documentacion **Openapi** de la Api Rest.
```
http://localhost:8000/sibill/openapi
```

## Construido con

* [Virtualenv] (https://virtualenv.pypa.io/en/latest/)
* [Django] (https://www.djangoproject.com/)
* [Django Rest] (https://www.django-rest-framework.org/)
* [Openapi] (https://swagger.io/specification/)

## Control de versiones

* [Gitflow] (https://www.gitflow.com/)

## Autor

* **Jose Luis Luengo Ramos - [jelkinsp] (https://github.com/jelkinsp)**

## Licencia

Este proyecto no está provisto de ningún tipo de licencia.

