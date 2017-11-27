from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='geocrowdsource',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='geocrowdsource',
    # GETTING-STARTED: set author name (your name):
    author='Farhan Ar Rafi',
    # GETTING-STARTED: set author email (your email):
    author_email='farhanarrafi@gmail.com',
    # GETTING-STARTED: set author url (your url):
    url='farhanarrafi.com',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.11.7'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
