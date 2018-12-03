from setuptools import setup
    
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="blackPanther-pydialog",

    version="0.9.8",

    description="PyDialog [PyQt5] is a new dialog instead kdialog or zenity",
    long_description = """
    My problem was that the kdialog code is still not ported previously to Qt5 
    and it depends on various Qt4/KDE4 components. 
    The kdialog has big dependency sizes so we made an alternate dialogs like 
    kdialog switches, options (Zenity is too ugly and Gtk based). 
    We would still like full compatibility with kdialog but a few options are 
    still not finished and although this release provides many important 
    functions.

    Patches, extensions, ideas are welcome!

    Maintainer Miklos Horvath 
    Project idea, design, contributor and first code by me (Charles K. B.)    
    """,
    
    url="https://github.com/blackPantherOS/pydialog",

    author="Charles Barcza, Miklos Horvath",
    maintainer="Miklos Horvath <hmiki@blackpantheros.eu>",
    
    license="GPLv3+",

    classifiers=[
        "Development Status :: 5 - Production/Stable",

        "Intended Audience :: Developers",

        "Topic :: Desktop Environment",
        "Topic :: Desktop Environment :: K Desktop Environment (KDE)",
        "Environment :: X11 Applications :: Qt",
        
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: BSD :: FreeBSD",
        "Operating System :: POSIX :: BSD :: OpenBSD",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],

    packages=["blackPanther_pydialog"],
    
    scripts=["bin/pydialog"],
    
    install_requires = ["argparse", "configparser"]
)