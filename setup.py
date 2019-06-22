#!/usr/bin/env python

import re
import sys
from setuptools import setup, find_packages

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = ''
with open('ichubOpenApi/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'rb') as f:
    readme = f.read().decode('utf-8')

setup(
    name='ichubOpenApi-openapi-sdk-python',
    version=version,
    description='Ichub OpenApi Python SDK',
    long_description=readme,
    packages=find_packages(),
    install_requires=['requests!=2.9.0',
                      'rsa'
                      ],
    include_package_data=True,
    url='https://www.ichubOpenApi.com',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)
