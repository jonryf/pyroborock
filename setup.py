from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pyroborock',
    version='1.1.5',
    packages=['pyroborock'],
    install_requires=['tinytuya==v1.2.3', 'python-miio==0.5.11', 'pycryptodome==3.14.1'],
    description='Communicate with roborock over tuya protocol',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/89jd/pyroborock',
    author='jd89',
    author_email='jd89.dev@gmail.com',
)
