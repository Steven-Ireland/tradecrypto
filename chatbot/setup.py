from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


setup(
    name='tradeCypto',
    version='1.0.0',
    description='A chatbot to trade crypto currencies.'
    long_description='poop',
    url='https://github.com/Steven-Ireland/tradecrypto',
    author='Irelands Drunken Developer',
    license='MIT',
    classifiers=[],
    keywords='twitch chat bot chatbot crypto cryptocurrency',
    packages=find_packages(exclude=['docs'])
)
