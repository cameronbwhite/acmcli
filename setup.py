#!/usr/bin/env python2
#Copyright (C) 2014, Cameron Brandon White
# -*- coding: utf-8 -*-
import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="acmcli",
        version="0.1.0",
        description="command line utility for @pdxacm",
        author="Cameron Brandon White",
        author_email="cameronbwhite90@gmail.com",
        include_package_data=True,
        packages=["acmcli"],
        scripts=["bin/acmcli"],
        install_requires=[
            'acmlib',
        ],
        dependency_links=[
            'git+git://github.com/pdxacm/acmlib-py.git#egg=acmlib'
        ]
    )
