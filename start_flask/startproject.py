import os
import sys
from jinja2 import Environment, FileSystemLoader


class Project:
    def __init__(self, proj, afp, venv, sqlal):
        self.proj = proj
        self.afp = afp
        self.venv = venv
        self.sqlal = sqlal
        self.context = {"proj": proj, "afp": afp, "venv": venv, "sqlal": sqlal}

    def render_template(self, template):
        if "/" in template:
            _input = template.split("/")[-1]
        else:
            _input = template

        env = Environment(loader=FileSystemLoader("start_flask/templates"))
        _template = env.get_template(_input)

        with open(f"{self.proj}/{template}", "w") as fl:
            fl.write(_template.render(self.context))

    def dir_extrutures(self):
        print("\n1 - Creating the directories extruture ...")
        if self.afp:
            # /
            os.system(f"mkdir {self.proj}")
            # /proj
            os.system(f"mkdir {self.proj}/{self.proj}")
            # /proj/templates
            os.system(f"mkdir {self.proj}/{self.proj}/templates")
            # /proj/static (css, img, js)
            os.system(f"mkdir {self.proj}/{self.proj}/static")
            os.system(f"mkdir {self.proj}/{self.proj}/static/css")
            os.system(f"mkdir {self.proj}/{self.proj}/static/img")
            os.system(f"mkdir {self.proj}/{self.proj}/static/js")
            # /proj/ext
            os.system(f"mkdir {self.proj}/{self.proj}/ext")
            # /proj/ext/site
            os.system(f"mkdir {self.proj}/{self.proj}/ext/site")
            if self.sqlal:
                # /proj/ext/db
                os.system(f"mkdir {self.proj}/{self.proj}/ext/db")
                # /proj/ext/auth
                os.system(f"mkdir {self.proj}/{self.proj}/ext/auth")
            # /proj/tests
            os.system(f"mkdir {self.proj}/tests")
        else:
            # /
            os.system(f"mkdir {self.proj}")
            # /proj/tests
            os.system(f"mkdir {self.proj}/tests")

    def write_files(self):
        print("2 - Writing texts content in files ...")
        # /
        os.system(f"touch {self.proj}/LICENCE")
        os.system(f"touch {self.proj}/README.md")
        self.render_template("requirements.txt")
        self.render_template("requirements-dev.txt")
        self.render_template("Makefile")
        self.render_template("setup.py")

        # /proj
        os.system(f"touch {self.proj}/{self.proj}/__init__.py")
        self.render_template(f"{self.proj}/app.py")

        # /test
        self.render_template(f"/tests/conftest.py")

        # with open(f"{self.proj}/tests/conftest.py", "w") as fl:
        #     fl.write(self.conftest)
        # with open(f"{self.proj}/tests/test_app.py", "w") as fl:
        #     fl.write(self.test_app)
        # # /proj/ext
        # os.system(f"touch {self.proj}/{self.proj}/ext/__init__.py")
        # with open(f"{self.proj}/{self.proj}/ext/config.py", "w") as fl:
        #     fl.write(self.config)
        # with open(f"{self.proj}/{self.proj}/ext/cli.py", "w") as fl:
        #     fl.write(self.cli)

        # if self.sqlal:
        #     with open(f"{self.proj}/{self.proj}/ext/admin.py", "w") as fl:
        #         fl.write(self.admin)

        # # /proj/ext/site
        # with open(f"{self.proj}/{self.proj}/ext/site/main.py", "w") as fl:
        #     fl.write(self.main_site)
        # with open(f"{self.proj}/{self.proj}/ext/site/__init__.py", "w") as fl:
        #     fl.write(self.init_site)

        # if self.sqlal:
        #     # /proj/ext/db
        #     with open(f"{self.proj}/{self.proj}/ext/db/__init__.py", "w") as fl:
        #         fl.write(self.init_db)
        #     with open(f"{self.proj}/{self.proj}/ext/db/commands.py", "w") as fl:
        #         fl.write(self.commands_db)
        #     # /proj/ext/auth
        #     with open(
        #         f"{self.proj}/{self.proj}/ext/auth/__init__.py", "w"
        #     ) as fl:
        #         fl.write(self.init_auth)
        #     with open(f"{self.proj}/{self.proj}/ext/auth/models.py", "w") as fl:
        #         fl.write(self.models_auth)
        #     with open(f"{self.proj}/{self.proj}/ext/auth/admin.py", "w") as fl:
        #         fl.write(self.admin_auth)

    # def create_venv(self):
    #     print("3 - Creating virtual env (.venv) ...")
    #     os.chdir(f"{self.proj}")
    #     os.system("python3 -m venv .venv")
    #     os.system(".venv/bin/pip install -q --upgrade pip")
    #     os.system(".venv/bin/pip install -q -r requirements.txt")


# Starting project #############################################################
def start_flask():
    print("\n### Flask Project Builder ###\n")

    proj, venv, sqlal = "", None, None

    # trying to get: proj, venv and sqlal on the command line
    if sys.argv[1:]:
        proj = sys.argv[1]
        afp = True if "--afp" in sys.argv[1:] else False
        venv = True if "--venv" in sys.argv[1:] else False
        sqlal = True if "--sqlal" in sys.argv[1:] else False

    while not proj:
        print("Enter the project name.")
        proj = input().replace(" ", "_")

    # to use a virtual environment?
    if not afp:
        print("Do you want to use the Application Factory Pattern? (Y/n)")
        afp = True if input() in "YySs" else False

    # to use a virtual environment?
    if not venv:
        print("Do you want to use the .venv? (Y/n)")
        venv = True if input() in "YySs" else False

    # to use SQLAlchemy?
    if not sqlal:
        print("Do you want to use the SQLAlchemy? (Y/n)")
        sqlal = True if input() in "YySs" else False

    project = Project(proj, afp, venv, sqlal)
    project.dir_extrutures()
    project.write_files()
    # if venv:
    #     project.create_venv()

    print("\nAll done!")
