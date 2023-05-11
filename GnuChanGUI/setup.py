from setuptools import setup, find_packages
setup(
    name="GnuChanGUI",
    version="0.2.1",
    author="archkubi",
    author_email="gnuchanos@gmail.com",
    description="pysimplegui base gui for beginner",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gnuchanos/GnuChanGUI",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="PySimpleGUI,GnuChanGUI,beginner gui",
    install_requires=[
        "pysimplegui",
    ],
    extras_require={},
    python_requires=">=3.11.3",
)
