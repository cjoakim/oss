#!/bin/bash

# For sdist deployment to PyPi, or local PyPi server:
# python setup.py sdist
# python setup.py sdist upload
# python setup.py sdist upload -r local
# python setup.py sdist upload -r pypilegacy
# ls -al /Users/cjoakim/pypi-packages
# rm /Users/cjoakim/pypi-packages/gdg*


# $ python setup.py sdist upload
# running sdist
# running egg_info
# writing gdg.egg-info/PKG-INFO
# writing dependency_links to gdg.egg-info/dependency_links.txt
# writing requirements to gdg.egg-info/requires.txt
# writing top-level names to gdg.egg-info/top_level.txt
# reading manifest file 'gdg.egg-info/SOURCES.txt'
# reading manifest template 'MANIFEST.in'
# warning: no previously-included files found matching '*.json'
# warning: no previously-included files found matching '*.sh'
# warning: no previously-included files found matching '*.txt'
# warning: no previously-included files found matching '*.xml'
# no previously-included directories found matching 'bin'
# no previously-included directories found matching 'htmlcov'
# warning: no previously-included files found matching 'examples.py'
# warning: no previously-included files found matching 'pyenv.sh'
# writing manifest file 'gdg.egg-info/SOURCES.txt'
# running check
# creating gdg-0.1.0
# creating gdg-0.1.0/gdg
# creating gdg-0.1.0/gdg.egg-info
# creating gdg-0.1.0/tests
# copying files to gdg-0.1.0...
# copying LICENSE -> gdg-0.1.0
# copying MANIFEST.in -> gdg-0.1.0
# copying README.rst -> gdg-0.1.0
# copying setup.cfg -> gdg-0.1.0
# copying setup.py -> gdg-0.1.0
# copying gdg/__init__.py -> gdg-0.1.0/gdg
# copying gdg/gdg.py -> gdg-0.1.0/gdg
# copying gdg/gdg_constants.py -> gdg-0.1.0/gdg
# copying gdg.egg-info/PKG-INFO -> gdg-0.1.0/gdg.egg-info
# copying gdg.egg-info/SOURCES.txt -> gdg-0.1.0/gdg.egg-info
# copying gdg.egg-info/dependency_links.txt -> gdg-0.1.0/gdg.egg-info
# copying gdg.egg-info/requires.txt -> gdg-0.1.0/gdg.egg-info
# copying gdg.egg-info/top_level.txt -> gdg-0.1.0/gdg.egg-info
# copying tests/__init__.py -> gdg-0.1.0/tests
# copying tests/test_epoch_type.py -> gdg-0.1.0/tests
# copying tests/test_gdg_constants.py -> gdg-0.1.0/tests
# copying tests/test_generation_type.py -> gdg-0.1.0/tests
# copying tests/test_timestype_local_type.py -> gdg-0.1.0/tests
# copying tests/test_timestype_utc_type.py -> gdg-0.1.0/tests
# Writing gdg-0.1.0/setup.cfg
# Creating tar archive
# removing 'gdg-0.1.0' (and everything under it)
# running upload
# Submitting dist/gdg-0.1.0.tar.gz to https://upload.pypi.org/legacy/
# Server response (200): OK