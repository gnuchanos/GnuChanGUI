import os
import re

from setuptools import setup, find_packages



setup(
    name="GnuChanGUI",
    version=0.31,
    description="GnuChanGUI — tkinter tabanli GUI (LGPL-3.0+)",
    author="archkubi",
    author_email="gnuchanos@email.com",
    packages=find_packages(include=["GnuChanGUI", "GnuChanGUI.*"]),
    install_requires=[
        "pygame-ce",
        "Pillow",
    ],
)
