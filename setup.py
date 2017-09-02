#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup


setup(
    name="Webhook",
    version="0.1.0",
    license="MIT",
    description="Webhook Component.",
    long_description="Webhook Component.",
    author="Renat Zhilkibaev",
    author_email="rzhilkibaev@gmail.com",
    url="https://github.com/rzhilkibaev/shmenkins",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "boto3", "shmenkins"
    ],
)
