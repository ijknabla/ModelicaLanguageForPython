
from setuptools import setup, find_packages

setup(
    name="ModelicaLanguage",
    version="0.0.0a1",
    pack="Modelica language for Python3.x",
    packages=find_packages(),
    install_requires=[
        "Arpeggio",
        "Numpy",
    ],
)
