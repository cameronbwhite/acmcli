#!/usr/bin/env python2
#Copyright (C) 2014, Cameron Brandon White
# -*- coding: utf-8 -*-
import setuptools

from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement
# object
install_reqs = parse_requirements("requirements.txt")

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

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
        install_requires=reqs
    )
