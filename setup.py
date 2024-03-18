#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @description : description
# @file    : setup.py
# @author  : xingpeidong
# @email   : xpd1437@126.com
# @time    : 2024/3/14 15:31
"""
from setuptools import setup, find_packages
from wheel.bdist_wheel import bdist_wheel

setup(
    name='insta_python_api',
    version='1.1.0',
    packages=find_packages(),
    package_data={'insta_python_api': ['config/example_config.yaml']},
    include_package_data=True,
    install_requires=[
        'requests',
        # Add other dependencies here
        'PyYAML',
    ],
    test_suite='tests',
    tests_require=[
        'pytest',
        # Add other testing dependencies here
    ],
    author='xingpeidong',
    author_email='xpd1437@126.com',
    description='instafoging python api package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/allesx/insta_python',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        # Add other classifiers as needed
    ],
    cmdclass={'bdist_wheel': bdist_wheel},
)
