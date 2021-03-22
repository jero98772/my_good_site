#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
my_good_site - 2020 - por jero98772
my_good_site - 2020 - by jero98772
"""
from setuptools import setup, find_packages
setup(
	name='my_good_site',
	version='2.7.5',
	license='GPLv3',
	author_email='jero98772@protonmail.com',
	author='jero98772',
	description='my good place with good proyects ',
	url='https://jero98772.pythonanywhere.com/',
	packages=find_packages(),
    install_requires=['Flask', 'tensorflow', 'numpy', 'opencv-python', 'removebg', ' pycrypto ', 'influxdb', 'matplotlib'],
    include_package_data=True,
	)
print(" _ __   ___ | |_ ___  ___ ")
print("| '_ \ / _ \| __/ _ \/ __|")
print("| | | | (_) | ||  __/\__ \ ")
print("|_| |_|\___/ \__\___||___/")
print("\n\n","PLEASE UPDATE PIP with (if needed):","\n\n","> pip intsall -U pip")
print("\n\n","SOME COMONS ERRORS of installing","\n\n","> tensorflow version == 1.14.0 \n> conda enviroment for tensorflow ,\n>need pip update for pycrypto")
print("tensorflow not required in general , curapeces need tensorflow")