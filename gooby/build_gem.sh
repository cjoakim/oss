#!/bin/bash

env | grep RUBYOPT
env | grep GOOBY

touch gooby-3.0.0.gem
rm    gooby-3.0.0.gem

gem   build gooby.gemspec

cp    gooby-3.0.0.gem  /temp

cd    /temp

rm   -rf gooby-3.0.0

gem   unpack gooby-3.0.0.gem
