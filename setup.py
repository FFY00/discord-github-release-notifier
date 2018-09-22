#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version__ = '1.0.1'

setup(
    name='discord_github_release_notifier',
    python_requires=">=3",
    version=__version__,
    packages=find_packages(),
    author="Filipe LAÍNS",
    author_email="filipe.lains@gmail.com",
    description="Github Notifier",
    long_description=open('README.rst').read(),
    install_requires=["feedparser", "requests", "tomd"],
    include_package_data=True,
    url='http://github.com/FFY00/diiscord-github-release-notifier/',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Communications",
        "Topic :: Internet",
        "Topic :: Software Development :: Pre-processors",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
    ],
    entry_points={
        'console_scripts': [
            'discord-github-release-notifier = github_release_notifier.cli:main',
        ],
    },
    license="MIT",
)
