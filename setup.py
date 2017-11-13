#!/usr/bin/env python2

from setuptools import setup, find_packages

version = '0.1.7'

setup(
    name='activitystreams',
    version=version,
    description="ActivityStreams 1.0 JSON implementation",
    long_description="""Activity Streams 1.0""",
    classifiers=[],
    keywords='activitystreams',
    author='Oscar Eriksson',
    author_email='oscar.eriks@gmail.com',
    url='https://github.com/sovaa/activitystreams',
    license='LICENSE.txt',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'strict-rfc3339==0.7',  # parsing dates
    ],
    test_requires=[
        'nose==-1.3.7'
    ])
