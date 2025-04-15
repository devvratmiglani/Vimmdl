import setuptools
from setuptools import setup

setup(
    name="vm-cli",
    version="2.2",
    description="CLI tool to search and download roms from vimm's lair",
    url="https://github.com/devvratmiglani",
    author="Devvrat Miglani",
    author_email="devvratmiglani@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["vm"],
    install_requires=[
        "click>=8.0.4",
        "beautifulsoup4>=4.12.2",
        "bs4>=0.0.1",
        "requests>=2.31.0",
        "tabulate>=0.8.10",
        "colorama>=0.4.6",
        "certifi>=2023.7.22",
        # "truststore",
        "setuptools>=64.0.0,<=69.0.2"
    ],
    entry_points="""
        [console_scripts]
        vm=vm:cli
    """,
)
