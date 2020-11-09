import setuptools
import requests 
import os, sys, glob
import urllib.request
import platform

with open("README.md", "r") as fh:
    long_description = fh.read()

pck=setuptools.find_packages(exclude=("toto","toto.*"))


totoviewdata_files=[]
for f in glob.glob('totoview/_tools/*.*'):
    dirname = os.path.join('totoview','_tools')
    totoviewdata_files.append((dirname, [f]))


setuptools.setup(
    name="totoview",
    version="0.0.1",
    author="Remy Zyngfogel",
    author_email="R.zyngfogel@calypso.science",
    description="A GUI toolbox for processing timeseries'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/calypso-science/Totoview",
    packages=pck,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    data_files=totoviewdata_files

)

if platform.system() == 'Linux':
    os.system('sudo cp totoView.py /usr/local/bin/totoView')
    os.system('sudo chmod 777 /usr/local/bin/totoView')