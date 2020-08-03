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
> - The `--venv` option indicates that you want to create a virtual environment.  _It will be created inside the project's root folder as `.venv`_.
> - The `--sqlal` option indicates that you want to install [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) in your project.
> - The `--dyna` option indicates that you want to install [Dynaconf](https://dynaconf.readthedocs.io/en/docs_223/) in your project.
> - The `--all` option indicates that you want to install all options (afp + venv + sqlal).
> - If you chose the Application Factory Pattern (`--afp`), don't forget to update the FLASK_APP environment variable:
>> ~~~sh
>> $ export FLASK_APP=project_name/app.py
>> ~~~
> - If you want to run flask in development mode, update the FLASK_ENV environment variable:
>> ~~~sh
>> $ export FLASK_ENV=development
>> ~~~
> - if you are using the Application Factory Pattern and want to use the `flask-toolbar`, run the command:
>> ~~~sh
>> $ pip install flask-toolbar
>> ~~~
>> and uncomment the line:   
>> `# toolbar.init_app(app)` at `app.py` file or   
>> `# "project_name.ext.toolbar:init_app"` in `settings.toml` _(when you are using Dynaconf)_   
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

---

This python script was created by Cesar and Jady Godoi during [Curso de Desenvolvimento Web](http://skip.gg/curso-flask-codeshow) taught by Bruno Rocha.
