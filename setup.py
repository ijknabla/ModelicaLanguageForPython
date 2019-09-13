#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="ModelicaLanguage",
    version="0.0.0a5",
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
