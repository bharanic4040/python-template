from setuptools import setup

setup(
    name='python-template',
    version='3.0.0',
    packages=['python-template'],
    entry_points = {
        "console_scripts": ['python-template = python-template.main-runner.py:main']
        },
    url='https://github.com/bharanic4040/python-template/',
    license='Open Source',
    author='bharani chennu',
    author_email='bharanic404@gmail.com',
    description='',
    setup_requires=['wheel']
)
