import os
from base64 import b16encode
from jinja2 import Environment, FileSystemLoader


class ProjectBuilder:
    def __init__(self, proj, afp, sqlal, dyna):
        self.proj = proj
        self.afp = afp
        self.sqlal = sqlal
        self.dyna = dyna
        secret = b16encode(os.urandom(16)).decode("utf-8")
        self.context = {
            "proj": proj,
            "afp": afp,
            "sqlal": sqlal,
            "dyna": dyna,
            "secret": str(secret) if dyna else "",
        }
        self.templates = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "templates"
        )

    def render_template(self, path):
        if "/" in path:
            _template = "/".join(path.split("/")[1:])
        else:
            _template = path

        env = Environment(loader=FileSystemLoader(self.templates))
        template = env.get_template(_template)

        with open(f"{self.proj}/{path}", "w") as fl:
            fl.write(template.render(self.context))

    def directories(self):
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
            # /proj/tests
            os.system(f"mkdir {self.proj}/tests")
            if self.sqlal:
                # /proj/ext/db
                os.system(f"mkdir {self.proj}/{self.proj}/ext/db")
                # /proj/ext/auth
                os.system(f"mkdir {self.proj}/{self.proj}/ext/auth")
                # /proj/migrations
                os.system(f"mkdir {self.proj}/migrations")
        else:
            # /
            os.system(f"mkdir {self.proj}")
            # /proj/tests
            os.system(f"mkdir {self.proj}/tests")
            # /proj/templates
            os.system(f"mkdir {self.proj}/templates")

    def files(self):
        # /
        os.system(f"touch {self.proj}/LICENCE")
        os.system(f"touch {self.proj}/README.md")
        self.render_template("requirements.txt")
        self.render_template("requirements-dev.txt")
        self.render_template("Makefile")
        self.render_template("setup.py")
        if self.dyna:
            self.render_template(".env")
            self.render_template(".secrets.toml")
            self.render_template("settings.toml")

        # /proj (app)
        if self.afp:
            os.system(f"touch {self.proj}/{self.proj}/__init__.py")
            self.render_template(f"{self.proj}/app.py")
        else:
            os.system(f"touch {self.proj}/__init__.py")
            self.render_template("app.py")

        # /test
        self.render_template("tests/conftest.py")
        self.render_template("tests/test_app.py")

        # index in /proj/templates or /templates
        if self.afp:
            self.render_template(f"{self.proj}/templates/index.html")
        else:
            self.render_template(f"templates/index.html")

        # /proj/ext
        if self.afp:
            os.system(f"touch {self.proj}/{self.proj}/ext/__init__.py")
            self.render_template(f"{self.proj}/ext/config.py")
            self.render_template(f"{self.proj}/ext/cli.py")
            self.render_template(f"{self.proj}/ext/hooks.py")
            if self.sqlal:
                self.render_template(f"{self.proj}/ext/admin.py")
                self.render_template(f"{self.proj}/ext/migrate.py")
                self.render_template(f"{self.proj}/ext/toolbar.py")

            # /proj/ext/site
            self.render_template(f"{self.proj}/ext/site/main.py")
            self.render_template(f"{self.proj}/ext/site/__init__.py")

            if self.sqlal:
                # /proj/ext/db
                self.render_template(f"{self.proj}/ext/db/__init__.py")
                self.render_template(f"{self.proj}/ext/db/commands.py")

                # /proj/ext/auth
                self.render_template(f"{self.proj}/ext/auth/__init__.py")
                self.render_template(f"{self.proj}/ext/auth/models.py")
                self.render_template(f"{self.proj}/ext/auth/admin.py")

    def create_venv(self):
        os.chdir(f"{self.proj}")
        os.system("python3 -m venv .venv")
        os.system(".venv/bin/pip install -q --upgrade pip")
        os.system(".venv/bin/pip install -q -r requirements.txt")
