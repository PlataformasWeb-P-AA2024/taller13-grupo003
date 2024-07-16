# taller13

## Creación de Servicio Web y Consumo vía Flask

### Revisar
- Ejemplo de servicios web con Django y Django-Rest [ejemplos]
- Ejemplo de consumo de servicios web desde flask [consumo-api]

### Ejemplos
* Usando curl
```
curl -H 'Accept: application/json; indent=4' -u user:pass http://127.0.0.1:8000/users/
curl -H 'Accept: application/json; indent=4' -iX POST -d 'telefono=1909091&tipo=personal&estudiante=http://127.0.0.1:8000/api/estudiantes/4/' -u user:pass 127.0.0.1:8000/api/numerost/
curl -iX PUT -d 'telefono=22909091&tipo=particular2&estudiante=http://127.0.0.1:8000/api/estudiantes/13/' -u user:pass http://127.0.0.1:8000/api/numerost/24/
curl -X DELETE -u user:pass http://127.0.0.1:8000/api/numerost/25/
curl -iX GET -u user:pass http://127.0.0.1:8000/api/numerost/24/

```

* Usando requests (librería de python)

```

# GET
import requests
r = requests.get("http://127.0.0.1:8000/api/estudiantes/", auth=('user', 'passs'))
r.content

# POST
r = requests.post('http://127.0.0.1:8000/api/numerost/', data = {'estudiante':'http://127.0.0.1:8000/api/estudiantes/12/', 'telefono':'99999999', 'tipo'='principal' }, auth=('user', 'pass'))
print(r)

# PUT
r = requests.put('http://127.0.0.1:8000/api/numerost/26', data = {'estudiante':'http://127.0.0.1:8000/api/estudiantes/13/', 'telefono':'99999999', 'tipo':'principal' }, auth=('user', 'pass'))
print(r)

# DELETE
r = requests.delete('http://127.0.0.1:8000/api/numerost/26/', auth=('user', 'pass'))
print(r)
```


### Problemática

Dadas dos entidades:

* Edificio:
	* nombre
	* dirección
	* ciudad
	* tipo [residencial, comercial]

* Departamento
	* nombre completo del propietario
	* costo del departamento
	* número de cuartos
	* edificio

Nota: Un departamento pertenece a un edificio

### Tecnologías y herramientas:

- Base de datos Sqlite
- Lenguaje Python
- Framework Django
- Django-Rest
- Flask


### Tarea a realizar:

- Crear un proyecto de Django.
- Crear una aplicación en el proyecto en Django.
- Generar el modelo de la aplicación usando las entidades descritas.
- Activar la interfaz de administración de la aplicación de Django.
- Agregar servicios web que permitan lista; crear; actualizar y eleminar entidades (todas deben tener acceso con autentificación)

- Crear una aplicación en Flask que permita:
	-	Listar Edificios haciendo uso de los servicios web creados en el proyecto de Django
	- Listar Departamentos haciendo uso de los servicios web creados en el proyecto	 de Django.
	- Crear Edificios haciendo uso de los servicios web creados en el proyecto de Django.
