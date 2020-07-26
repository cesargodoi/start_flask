# Start Flask
Start a new Flask project on the application factory model.      

## How to use

1. Update the pip in your virtual environment:
> ~~~sh
> $ pip install --upgrade pip
> ~~~
2. Install start_flask package:
> ~~~sh
> $ pip install -i https://test.pypi.org/simple/ start-flask
> ~~~
3. Create your new projects:
> ~~~sh
> $ start_flask project_name [options]
> or
> $ start_flask [options] project_name
> ~~~

> IMPORTANT
> - Do not use spaces in your project name.  Prefer underscores instead spaces.
> - The `--afp` option indicates that you want to create a new Flask project on Application Factory Pattern.
> - The `--venv` option indicates that you want to create a virtual environment.  It will be created inside the project's root folder as `.venv`.
> - The `--sqlal` option indicates that you want to install SQLAlchemy in your project.
> - The `--all` option indicates that you want to install all options (afp + venv + sqlal).
> - If you chose the Application Factory Pattern (`--afp`), don't forget to update the FLASK_APP environment variable:
>> ~~~sh
>> $ export FLASK_APP=project_name/app.py
>> ~~~
> - If you want to run flask in development mode, update the FLASK_ENV environment variable:
>> ~~~sh
>> $ export FLASK_ENV=development
>> ~~~
<br>

In the `Makefile` file, we have some useful commands, which we use with the `make` command, such as:   

| **command**        | **what he does**                                    |
|--------------------|-----------------------------------------------------|
| `make clean`       | clears the project folder                           |
| `make install`     | install our project as a package python             |
| `make install-dev` | similar to install, but with requirements-dev.txt   |
| `make test`        | run tests                                           |
| `make init-db`     | starts and updates the db (if you choose `--sqlal`) |
| `make format`      | formats the files (needs: isort and black)          |
<br>

## Structures provided
### Basic or Basic with SQLAlchemy
~~~bash
project_name
├── app.py
├── __init__.py
├── LICENCE
├── Makefile
├── README.md
├── requirements-dev.txt
├── requirements.txt
├── setup.py
└── tests
    ├── conftest.py
    └── test_app.py
~~~
### Application Factory Pattern
~~~bash
project_name
├── project_name
│   ├── app.py
│   ├── ext
│   │   ├── cli.py
│   │   ├── config.py
│   │   ├── __init__.py
│   │   └── site
│   │       ├── __init__.py
│   │       └── main.py
│   ├── __init__.py
│   ├── static
│   │   ├── css
│   │   ├── img
│   │   └── js
│   └── templates
├── LICENCE
├── Makefile
├── README.md
├── requirements-dev.txt
├── requirements.txt
├── setup.py
└── tests
    ├── conftest.py
    └── test_app.py
~~~
### Application Factory Pattern and SQLAlchemy
~~~bash
project_name
├── LICENCE
├── Makefile
├── project_name
│   ├── app.py
│   ├── ext
│   │   ├── admin.py
│   │   ├── auth
│   │   │   ├── admin.py
│   │   │   ├── __init__.py
│   │   │   └── models.py
│   │   ├── cli.py
│   │   ├── config.py
│   │   ├── db
│   │   │   ├── commands.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   └── site
│   │       ├── __init__.py
│   │       └── main.py
│   ├── __init__.py
│   ├── static
│   │   ├── css
│   │   ├── img
│   │   └── js
│   └── templates
├── README.md
├── requirements-dev.txt
├── requirements.txt
├── setup.py
└── tests
    ├── conftest.py
    └── test_app.py
~~~
---

This python script was created by Cesar and Jady Godoi during [Curso de Desenvolvimento Web](http://skip.gg/curso-flask-codeshow) taught by Bruno Rocha.
