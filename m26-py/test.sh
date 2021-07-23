#!/bin/bash

echo 'checking the source code with flake8 ...'
#flake8 m26 --ignore F401

echo 'executing unit tests with code coverage ...'
# pytest -v --cov=m26/ --cov-report html tests/

python -m pytest --cov=m26/ --cov-report html tests/

# For sdist deployment to PyPi, or local PyPi server:
# python setup.py sdist
# python setup.py sdist upload
# python setup.py sdist upload -r local
# python setup.py sdist upload -r pypilegacy
# ls -al /Users/cjoakim/pypi-packages
# rm /Users/cjoakim/pypi-packages/m26*
