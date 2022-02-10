# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from setuptools import setup, find_packages

__version__ = '1.1.4'

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    reqs = f.read()

setup(
    name='pytextclassifier',
    version=__version__,
    description='Text Classifier, Text Classification',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='XuMing',
    author_email='xuming624@qq.com',
    url='https://github.com/shibing624/pytextclassifier',
    license='Apache 2.0',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='pytextclassifier,textclassifier,classifier,textclassification',
    install_requires=reqs.strip().split('\n'),
    packages=find_packages(exclude=['tests']),
    package_dir={'pytextclassifier': 'pytextclassifier'},
    package_data={
        'pytextclassifier': ['*.*', '../LICENSE', '../README.*', '../*.txt', 'data/*',
                             'tools/*', '../examples/thucnews_train_10w.txt'],
    },
    test_suite='tests',
)
