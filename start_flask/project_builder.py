import os

from tarfile import TarFile
from zipfile import ZipFile
from base64 import b16encode
from jinja2 import Environment, FileSystemLoader


class ProjectBuilder:
    """
    Generates the structure of a flask project. 
    
    arguments: 
    proj -> project_name (using underscores)
    afp -> Application Factory Pattern
    sqlal -> SQLAlchemy
    dyna -> Dynaconf
    dir_to_render --> if you are using on the web

    methods: 
    create_venv -> create a virtual environment
    make_tarfile -> compress the project using tar
    make_zipfile -> compress the project using zip
    """

    def __init__(self, proj, afp, sqlal, dyna, dir_to_render=None):
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
        if dir_to_render:
            os.chdir(dir_to_render)

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

    def make_tarfile(self):
        with TarFile.open(f"{self.proj}.tar.gz", "w:gz") as tar_file:
            tar_file.add(self.proj)
        os.system(f"rm -rf {self.proj}")

    def make_zipfile(self):
        file_paths = []
        for root, directories, files in os.walk(self.proj):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_paths.append(file_path)
        with ZipFile(f"{self.proj}.zip", "w") as zip_file:
            for file_ in file_paths:
                zip_file.write(file_)
        os.system(f"rm -rf {self.proj}")

