from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))

app_name = "hidroclorotiazida"
sqlal = True

_app = env.get_template("app.txt")


with open("templates/saida_app.py", "w") as fl:
    fl.write(_app.render(app=app_name, sqlal=sqlal))
