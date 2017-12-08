# -*- Coding:utf-8 -*-
import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="union-find",
    version='0.0.1',
    license="MIT-LICENSE",
    url='http://github.com/minghu6/union-find',
    platforms=["any"],
    description="union-find data structure.",
    long_description=README,
    py_modules=['union_find'],
    package_data={'': ['MIT-LICENSE']},
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
