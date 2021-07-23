#!/bin/bash

# Bash script to execute the parsing of three tcx files.
# Chris Joakim, 2019/07/26

infile1='data/activity_twin_cities_marathon.tcx'
outfile1='data/activity_twin_cities_marathon.json'

infile2='data/alex_bike_outside_pretty.tcx'
outfile2='data/alex_bike_outside.json'

infile3='data/cj-cycling-20190721.tcx'
outfile3='data/cj-cycling-20190721.json'

rm $outfile1
rm $outfile2
rm $outfile3

echo ''
echo 'parsing first file...'
node dist/main.js $infile1 $outfile1

echo ''
echo 'parsing second file...'
node dist/main.js $infile2 $outfile2

echo ''
echo 'parsing third file...'
node dist/main.js $infile3 $outfile3

echo 'done'
