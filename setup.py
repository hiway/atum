#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import (
    absolute_import,
    print_function
)

import io
from os.path import (
    dirname,
    join,
)

from setuptools import find_packages, setup


def read(*names, **kwargs):
    return io.open(
            join(dirname(__file__), *names),
            encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
        name='atum',
        version='0.2.0',
        license='MIT',
        description='Erlang-like atoms in Python 3',
        long_description=read('README.rst'),
        author='Harshad Sharma',
        author_email='harshad@sharma.io',
        url='https://github.com/hiway/atum',
        py_modules=['atum'],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Topic :: Software Development',
            'Topic :: Utilities',
        ],
        install_requires=[
        ],
        extras_require={
            'dev': [
                'twine',
                'pypandoc',
                'pytest',
                'pytest-cov',
            ],
        },
)
