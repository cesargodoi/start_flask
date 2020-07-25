from setuptools import setup


setup(
    name="start_flask",
    version="0.1.2",
    author="Cesar Godoi",
    author_email="cesar.godoi@gmail.com",
    packages=["start_flask"],
    package_dir={"start_flask": "start_flask"},
    include_package_data=True,
    description="Start a Flask project in a Application Factory Pattern",
    url="https://github.com/cesargodoi/start_flask",
    project_urls={"source code": "https://github.com/cesargodoi/start_flask",},
    license="GNU GPLv3",
    entry_points={"console_scripts": ["start_flask=start_flask.cli:main"]},
    install_requires=["jinja2", "Click"],
)
