#!/usr/bin/env python2

from setuptools import setup, find_packages

version = '0.1.5'

setup(
    name='activitystreams',
    version=version,
    description="",
    long_description="""Activity Streams 1.0""",
    classifiers=[],
    keywords='activitystreams',
    author='Oscar Eriksson',
    author_email='oscar@thenetcircle.com',
    url='',
    license='LICENSE.txt',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'strict-rfc3339==0.7',  # parsing dates
    ])
