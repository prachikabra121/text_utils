
from setuptools import setup, find_packages

setup(
name="text-utils-prachi",
version="0.1.0",
author="Prachi Kabra",
author_email="kabraprachi1@gmail.com",
description="A basic text-utils pacakge",
long_description=open("README.md").read(),
long_description_content_type="text/markdown",
url="https://github.com/prachikabra121/text_utils",
packages=find_packages(),
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
python_requires=">=3.6",
)