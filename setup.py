# -*- coding: utf-8 -*-
# This is free and unencumbered software released into the public domain.

from setuptools import find_packages
from setuptools import setup

requires = [
    'nbsphinx',
    'sphinx',
    'sphinxcontrib-confluencebuilder',
    ]

setup(
    name='sphinx-confluence-nbsphinx-test',
    version='0.0.0-dev0',
    #author='???',
    #author_email='???',
    description="""Sphinx extension to support nbsphinx with the Sphinx """
                """Confluence extension.""",
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
