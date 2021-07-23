
# PowerShell script to compile and merge the code, then execute the unit tests.
# Chris Joakim, 2019/07/29

echo 'building...'
./build.sh


echo 'testing...'
rm mocha-*-results.xml
npm test

echo 'done'
