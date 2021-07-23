#!/bin/bash

# Bash script to compile and merge the code, then execute the unit tests.
# Chris Joakim, 2019/07/26

echo 'building...'
./build.sh


echo 'testing...'
rm mocha-*-results.xml
npm test

echo 'done'
