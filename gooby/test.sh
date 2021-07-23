#!/bin/bash

rm samples/data/2012-07-11-Dav7.json
rm samples/data/2012-07-11-Dav7.js

rake gooby:parse_tcx_file f=samples/data/2012-07-11-Dav7.tcx

rake gooby:generate_gmap_js c=config/gooby.yml

rspec
