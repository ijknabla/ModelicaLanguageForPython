
from setuptools import setup, find_packages

setup(
    name="ModelicaLanguage",
    pack="Modelica language for Python3.x",
    packages=find_packages(),
    install_requires=["Arpeggio"],
)
