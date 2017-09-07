#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

name = "build-requester-vcs"

setup(
    name=name,
    version="0.1.0",
    license="MIT",
    description="Build Requester Component.",
    long_description="Build Requester Component.",
    author="Renat Zhilkibaev",
    author_email="rzhilkibaev@gmail.com",
    url="https://github.com/shmenkins/" + name,
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "boto3", "shmenkins.utils"
    ],
)
