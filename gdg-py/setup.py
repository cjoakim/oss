
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gdg',

    # Versions should comply with PEP440.
    version='0.1.0',

    description='gdg - generation data groups with python',
    long_description=long_description,

    url='https://github.com/cjoakim/gdg-py',

    # Author details
    author='Christopher Joakim',
    author_email='christopher.joakim@gmail.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    keywords='generation data groups (gdg) with python',

    # You can just specify the packages manually here if your project is simple.
    # Or you can use find_packages().
    packages=find_packages(exclude=['bin', 'contrib', 'htmlcov', 'data', 'docs', 'tests*']),

    # Run-time dependencies; these will be installed by pip when the project is installed.
    # See https://packaging.python.org/en/latest/requirements.html
    install_requires=['arrow'],

    # Dev and Test dependencies, install like this: $ pip install -e .[dev,test]
    extras_require={
        'dev':  ['check-manifest'],
        'test': ['pytest', 'pytest-cov'],
    },
)
