# package code is present in __init__.py and setup.py is used for its identification

Build the package install below commands
pip install wheel
python steup.py bdist_wheel
python setup.py sdist bdist_wheel

with above commands package will be created and to run it use the below commands

pip install package_name
import package_name                    #to run them in powershell

setUp.py

from setuptools import setupsetup(name="packagecode"
                                  version="0.3"
                                  description="this is a code"
                                  long_description="this is very long code"
                                  author="Hello"
                                  packages=["Hellopackages"]
                                  install_requires=[]
                                  )
__init__.py
def func(number):
    return number