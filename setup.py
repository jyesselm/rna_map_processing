#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()


with open("README.md", "r", encoding="UTF-8") as f:
    readme = f.read()

with open("requirements.txt", "r", encoding="UTF-8") as f:
    requirements = f.read().splitlines()

setup(
    name="rna_map_processing",
    version="0.1.0",
    description="set of functions to process MaP data ",
    long_description=readme,
    long_description_content_type="test/markdown",
    author="Joe Yesselman",
    author_email="jyesselm@unl.edu",
    url="https://github.com/jyesselm/rna_map_processing",
    packages=[
        "rna_map_processing",
    ],
    package_dir={"rna_map_processing": "rna_map_processing"},
    py_modules=[
        "rna_map_processing/analysis",
        "rna_map_processing/paths",
        "rna_map_processing/processing",
        "rna_map_processing/search",
        "rna_map_processing/titration",
    ],
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords="rna_map_processing",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    entry_points={"console_scripts": []},
)
