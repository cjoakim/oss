
# PowerShell to Build/transpile the *.ts code into .js
# Chris Joakim, 2019/07/29

echo 'removing output files...'
rm dist/*.*

echo 'compiling the merge program...'
tsc --build tsconfig-merge.json

echo 'executing the merge program...'
node dist/merge.js src/tcx.ts

echo 'compiling after merge...'
tsc

echo 'done'
