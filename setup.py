from setuptools import setup

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="start_flask",
    version="0.1.9",
    author="Cesar Godoi",
    author_email="cesar.godoi@gmail.com",
    packages=["start_flask"],
    package_dir={"start_flask": "start_flask"},
    include_package_data=True,
    description="Start a Flask project in a Application Factory Pattern",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cesargodoi/start_flask",
    project_urls={"source code": "https://github.com/cesargodoi/start_flask",},
    license="GNU GPLv3",
    entry_points={"console_scripts": ["start_flask=start_flask.cli:main"]},
    install_requires=["jinja2", "Click"],
)
