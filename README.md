# Start Flask
Start a new Flask project on the application factory model.      

## How to use
1. Clone this repository: 
> ~~~sh
> $ git clone git@github.com:cesargodoi/start_flask.git
> ~~~
2. Install virtual environment and update pip:
> ~~~sh
> $ cd start_flask
> $ python3 -m venv .venv
> $ source .venv/bin/activate
> $ pip install --upgrade pip
> ~~~
3. Install start_flask package:
> ~~~sh
> $ make install
> ~~~
4. Create your new projects:
> ~~~sh
> $ ./startproject <project_name> --[arg]
> ~~~

> IMPORTANT
> - Do not use spaces in your project name.  Prefer underscores instead spaces.
> - The `--sfp` argument indicates that you want to create a new Flask project on Application Factory Pattern.
> - The `--venv` argument indicates that you want to create a virtual environment.  It will be created inside the project's root folder as `.venv`.
> - The `--sqlal` argument indicates that you want to install SQLAlchemy in your project.
   

In the `Makefile` file, we have some useful commands, which we use with the `make` command, such as:   

| **command**        | **what he does**                                    |
|--------------------|-----------------------------------------------------|
| `make clean`       | clears the project folder                           |
| `make install`     | install our project as a package python             |
| `make install-dev` | similar to install, but with requirements-dev.txt   |
| `make test`        | run tests                                           |
| `make run`         | run flask                                           |
| `make run-dev`     | run flask in the development environment            |
| `make init-db`     | starts and updates the dd (if you choose `--sqlal`) |
| `make format`      | formats the files (needs: isort and black)          |


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
