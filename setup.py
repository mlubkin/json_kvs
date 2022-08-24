from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='json_kvs',
    version='0.01',
    packages=['json_kvs',],
    license='MIT',
    author="mlubkin",
    description=".json file based key/value storage",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="cache key value file json",
    url="https://github.com/mlubkin/json_kvs",   
)