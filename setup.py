# -*- coding: utf-8 -*-
'''
File Name: steup.py
Author: JackeyGao
mail: junqi.gao@shuyun.com
Created Time: 2015年07月13日 星期一 13时02分21秒
'''

from setuptools import setup, find_packages
from teambition import __version__ as version, __doc__ as description

setup(
    name='teambition',
    version=version,
    install_requires=[
        'requests',
    ],
    zip_safe=False,
    py_modules = ['teambition'],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    description=description,
    author='JackeyGao',
    author_email='gaojunqi@outlook.com',
    url='https://github.com/jackeygao/teambition-client',
)

