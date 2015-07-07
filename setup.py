#!/usr/bin/env python
import os
from setuptools import setup, find_packages


README = os.path.join(os.path.dirname(__file__), 'README.md')

# when running tests using tox, README.md is not found
try:
    with open(README) as file:
        long_description = file.read()
except Exception:
    long_description = ''


setup(
    name='python-resize-image',
    version='1.1.3',
    description='A Small python package to easily resize images',
    long_description=long_description,
    url='https://github.com/VingtCinq/python-resize-image',
    author='Charles TISSIER',
    author_email='charles@vingtcinq.io',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='image resize resizing python',
    packages=find_packages(),
    install_requires=['pillow'],
    test_suite='tests',
)
