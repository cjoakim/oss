#!/bin/bash

# Bash script to merge the several src/*.ts files into file src/tcx.ts
# Chris Joakim, 2019/07/26

node dist/merge.js src/tcx.ts

echo 'done'
