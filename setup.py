from setuptools import find_packages, setup


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="start_flask_afp",
    version="0.1.0",
    description="Start a Flask project in a Application Factory Pattern",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
)
