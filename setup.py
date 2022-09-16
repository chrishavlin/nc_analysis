#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('readme.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as reqs_file:
    requirements = [req for req in reqs_file.readlines()]

with open('requirements_dev.txt') as reqs_file:
    test_requirements = [req for req in reqs_file.readlines()]

setup(
    author="C. Havlin",
    author_email='chris.havlin@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="a starter repository for netcdf analysis",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='nc_analysis',
    name='nc_analysis',
    packages=find_packages(include=['nc_analysis', 'nc_analysis.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/chrishavlin/nc_analysis',
    version='0.1.0',
    zip_safe=False,
)
