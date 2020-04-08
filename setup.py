# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my_lambdata_johan_mazorra", # the name that you will install via pip
    version="1.0.0",
    author="Johan Mazorra",
    author_email="johan-mazorra@lambdastudents.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/jsmazorra/my-lambdata",
    #keywords="",
    packages=find_packages() # ["my_lambdata_johan_mazorra"]
)