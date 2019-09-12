#!/usr/bin/env python3

from setuptools import setup, find_packages

from modelica_language import __version__ as package_version

setup(
    name="ModelicaLanguage",
    version=package_version,
    description="Modelica parser and class representation for Python3.x",
    author="ijknabla",
    author_email="ijknabla@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    url="https://github.com/ijknabla/ModelicaLanguageForPython",
    packages=find_packages(),
    install_requires=[
        "Arpeggio",
        "Numpy",
    ],
    python_requires='>=3.6',
)
