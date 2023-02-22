# Proyecto de Registro de Votantes en Colombia

Este es un proyecto de sistema de información para registrar los datos de los votantes de los distintos municipios de Colombia.

## Requisitos

- Registro de votantes con sus datos básicos y asignación a un puesto de votación.
- Rol de usuario "Líder" para ingresar los datos de los votantes.
- Usuario administrador que pueda ver toda la información ingresada.
- Los líderes sólo pueden ver la información que ellos mismos han ingresado.
- Registro del usuario que ingresó los datos del votante.
- Creación de usuarios líderes con datos de identificación y una foto de perfil.
- Obtención de coordenadas de los usuarios mediante el servicio de Georreferenciación de Google.
- Base de datos relacional y/o no relacional.
- Validaciones en los campos de entrada del formulario de votantes.
- Asociación de las mesas de votación con un municipio y un departamento.

## Estructura del proyecto

A continuación se muestra una estructura sugerida para el proyecto:

PROXIMAMENTE


## Tecnologías utilizadas

- Python
- Django
- PostgreSQL (o MongoDB)

## Instalación

Para instalar el proyecto, siga los siguientes pasos:

1. Clonar este repositorio: `git clone https://github.com/tu-usuario/proyecto.git`
2. Crear un entorno virtual: `python -m venv env`
3. Activar el entorno virtual: `source env/bin/activate` (Linux/MacOS) o `env\Scripts\activate` (Windows)
4. Instalar las dependencias: `pip install -r requirements.txt`
5. Crear una base de datos y configurarla en `project/settings.py`
6. Aplicar las migraciones: `python manage.py migrate`
7. Crear un superusuario: `python manage.py createsuperuser`
8. Ejecutar el servidor: `python manage.py runserver`
9. Abrir en el navegador la dirección `http://localhost:8000`

## Uso

Una vez instalado, el proyecto se puede usar mediante el navegador web. Para ingresar al sistema se requiere un usuario y contraseña. Los líderes sólo podrán ver la información que ellos mismos han ingresado, mientras que el usuario administrador podrá ver toda la información ingresada por todos los líderes.

## Contribución

Si deseas contribuir a este proyecto, puedes realizar un fork del repositorio y crear una rama con tus cambios. Luego, puedes hacer una solicitud de extracción para que tus cambios sean revisados e incorporados al proyecto principal.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.```

