import os
import re

from setuptools import setup


def _read_version():
    root = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(root, "GnuChanGUI", "version.py")
    with open(path, encoding="utf-8") as f:
        m = re.search(r'^__version__\s*=\s*["\']([^"\']+)["\']', f.read(), re.MULTILINE)
    return m.group(1) if m else "0.0.0"


setup(
    name="GnuChanGUI",
    version=_read_version(),
    description="GnuChanGUI — tkinter tabanli GUI (LGPL-3.0+)",
    author="archkubi",
    author_email="gnuchanos@email.com",
    packages=["GnuChanGUI"],
    install_requires=[
        "pygame-ce",
        "Pillow",
        "pynput",
    ],
)
