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
> - If you don't pass any arguments, they will be asked for you.   
   

In the `Makefile` file, we have some useful commands, which we use with the `make` command, such as:   

| **command**        | **what he does**                                  |
|--------------------|---------------------------------------------------|
| `make clean`       | clears the project folder                         |
| `make install`     | install our project as a package python           |
| `make install-dev` | similar to install, but with requirements-dev.txt |
| `make test`        | run tests                                         |
| `make run`         | run flask                                         |
| `make run-dev`     | run flask in the development environment          |
| `make init-db`     | starts and updates the database                   |
| `make format`      | formats the files (needs: isort and black)        |


## Structure provided
~~~sh
<project name>/
+-- <project name>/
|   +-- ext/ 
|   |   +-- auth/
|   |   |   +-- __init__.py
|   |   |   +-- admin.py
|   |   |   +-- models.py
|   |   +-- db/
|   |   |   +-- __init__.py
|   |   |   +-- commands.py
|   |   +-- site/
|   |   |   +-- __init__.py
|   |   |   +-- main.py
|   |   +-- __init__.py
|   |   +-- admin.py
|   |   +-- cli.py
|   |   +-- config.py
|   +-- static/
|   |   +-- ccs/
|   |   +-- img/
|   |   +-- js/
|   +-- templates/
|   +-- __init__.py
|   +-- app.py --> project entry point
+-- tests/
|   +-- conftest.py
|   +-- test_app.py --> with 3 tests
+-- LICENCE
+-- Makefile
+-- README.md
+-- requirements.txt
+-- requirements-dev.txt
+-- setup.py
~~~

---

This python script was created by Cesar and Jady Godoi during [Curso de Desenvolvimento Web](http://skip.gg/curso-flask-codeshow) taught by Bruno Rocha.
