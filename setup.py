from setuptools import setup


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="start_flask",
    version="0.1.0",
    description="Start a Flask project in a Application Factory Pattern",
    author="Cesar Godoi",
    author_email="cesar.godoi@gmail.com",
    packages=["start_flask"],
    package_dir={"start_flask": "start_flask"},
    entry_points={"console_scripts": ["start_flask=start_flask.cli:main"]},
    include_package_data=True,
    install_requires=["jinja2", "Click"],
)
