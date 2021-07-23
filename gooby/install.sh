#!/bin/bash

# First we install the gem, which was previously created by 'build_gem.sh'.

GOOBY_HOME=~/gooby
export GOOBY_HOME

cd    /temp

gem   uninstall gooby
gem   list --local | grep gooby > gem_list_after_uninstall.txt

gem   install gooby-3.0.0.gem 
gem   list --local | grep gooby > gem_list_after_install.txt

cd    gooby-3.0.0
ruby  setup.rb

set | sort > gooby_install_env.txt

# Now we execute gooby from within the GOOBY_HOME diretory.

cd   $GOOBY_HOME

rake > tmp/help.txt

# rake gooby:extract_activities_from_tcx

rake gooby:parse_activity_xml_to_csv  config_file=config/big_sur_marathon.yaml

rake gooby:parse_track_log_to_csv     config_file=config/crowders_mtn_hike.yaml

rake gooby:parse_gpx_to_csv           config_file=config/ballantyne.yaml

rake gooby:generate_google_map        config_file=config/big_sur_marathon.yaml
rake gooby:generate_google_map        config_file=config/crowders_mtn_hike.yaml
rake gooby:generate_google_map        config_file=config/ballantyne.yaml

rake gooby:generate_google_earth_map  config_file=config/big_sur_marathon.yaml
rake gooby:generate_google_earth_map  config_file=config/crowders_mtn_hike.yaml
rake gooby:generate_google_earth_map  config_file=config/ballantyne.yaml
