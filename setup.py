from setuptools import setup

setup(
    name="vm-cli",
    version="1.0",
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
        "click",
        "beautifulsoup4",
        "bs4",
        "requests",
        "tabulate",
        "colorama"
    ],
    entry_points="""
        [console_scripts]
        vm=vm:cli
    """,
)
