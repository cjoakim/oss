= Gooby = Google APIs + Ruby 

Gooby is a set of Ruby code to assist you in creating Google Maps, and 
Google Earth maps, from data exported from your Garmin GPS devices and
your desktop software such as Garmin Training Center and/or MacGpsPro.
Gooby will also process gpx data from the iPhone "MotionX GPS" application.

It will parse the exported Garmin xml/tcx/txt data, or MotionX gpx data, 
into csv files in a "standard gooby format".  You then use Gooby to generate
maps from specific csv files per yaml configuration files.

The typical uses of Gooby are to create maps of your running, cycling, or
hiking events, though Gooby is suitable for mapping any outdoor activity.

All Gooby functionality is intended to be invoked from a command line.

= General

Author::   Chris Joakim <chris@joakim-systems.com>
Requires:: Ruby 1.8.4 or later
License::  Copyright 2011-2013 by Chris Joakim.
           GNU General Public License (GPL) license.
           See http://www.gnu.org/copyleft/gpl.html
        
== License

Gooby is available under GNU General Public License (GPL) license.


== Download

Gooby is packaged and installed as a ruby 'gem'.  Download file 'gooby-2.0.0.gem'
from http://rubyforge.org/projects/gooby/.


== Installation

1.  Ensure that you have the necessary prerequisites installed on your computer.  These 
    include ruby itself, the rubygems package management system, libxml-ruby, and
    fastercsv. 

    sudo gem install fastercsv        1.5.4
    sudo gem install libxml-ruby      2.0.5
    sudo gem install rspec            2.6.0
    sudo gem install cucumber         0.10.2

	gem list --local
	
	*** LOCAL GEMS ***

	abstract (1.0.0)
	actionmailer (3.0.7)
	actionpack (3.0.7)
	activemodel (3.0.7)
	activerecord (3.0.7)
	activeresource (3.0.7)
	activesupport (3.0.7)
	arel (2.0.9)
	builder (3.0.0)
	bundler (1.0.12)
	cucumber (0.10.2)
	diff-lcs (1.1.2)
	erubis (2.7.0)
	fastercsv (1.5.4)
	gherkin (2.3.7)
	i18n (0.5.0)
	joakim (1.1.0)
	json (1.5.1)
	libxml-ruby (2.0.5)
	mail (2.3.0)
	mime-types (1.16)
	minitest (2.1.0, 1.6.0)
	polyglot (0.3.1)
	rack (1.2.2)
	rack-mount (0.7.2)
	rack-test (0.5.7)
	rails (3.0.7)
	railties (3.0.7)
	rake (0.8.7)
	rdoc (3.5.3, 2.5.8)
	rspec (2.6.0)
	rspec-core (2.6.0)
	rspec-expectations (2.6.0)
	rspec-mocks (2.6.0)
	sqlite3 (1.3.3)
	sqlite3-ruby (1.3.3)
	term-ansicolor (1.0.5)
	thor (0.14.6)
	treetop (1.4.9)
	tzinfo (0.3.26)

	
    You will also need desktop software, such as Garmin Training Center and/or MacGpsPro,
    which reads data from your GPS device, and enables it to be exported to files which
    Gooby can process.  Garmin Training Center is a free download from Garmin.com.

2.  Set the required GOOBY_HOME environment variable on your computer.  This variable
    names the directory on your computer where you will store your Gooby-related files,
    and where Gooby will generate content to.  Suggested values are 'C:\gooby' on Windows, 
    and '~/gooby' on unix-based systems.

3.  From your downloads directory, run the following commands:
      gem unpack gooby-2.0.0.gem
      sudo gem install gooby-2.0.0.gem

4.  Step 3 creates directory 'gooby-2.0.0' within your downloads directory.  Navigate
    into this directory, then run the following command.
      ruby setup.rb

    This will create subdirectories within your GOOBY_HOME, and will populate the /config
    and /samples directories with several files.


== Usage

All Gooby functionality is invoked from a command line in your GOOBY_HOME directory.
The rake program is used to execute all Gooby functions.

I encourage the reader to read the cucumber test file, 'features/gooby.feature' to become
familiar with how to use Gooby.  Cucumber is a ruby testing tool that allows you to specify
tests and requirements in English, then have ruby translate and execute the English text.

1.  Run command 'rake' from your GOOBY_HOME to see the list of Gooby commands available to you.  
    The list you see will look like the following:

    rake                                    # Default Task; Display Gooby usage instructions.
    rake gooby:help                         # Display Gooby usage instructions.
    rake gooby:extract_activities_from_tcx  # Extract individual Activity xml files from a Garmin tcx file
    rake gooby:parse_activity_xml_to_csv    # Parse an extracted Activity xml file to a corresponding csv file.
    rake gooby:parse_track_log_to_csv       # Parse a GPS Track Log file a corresponding csv file.
    rake gooby:parse_gpx_to_csv             # Parse a GPX file a corresponding csv file.
    rake gooby:generate_google_map          # Generate a Google Map from a csv file.
    rake gooby:generate_google_earth_map    # Generate a Google Earth kml file from a csv file.
 
2.  Run command 'rake', or 'rake gooby:help' to display the "help content" for Gooby;
    it contains specific examples of each command, and a description of the directory structure.

3.  The typical usage sequence is as follows.

    Part 1 - outside of the realm of Gooby:
    a.  Do some outdoor event, with your Garmin GPS device recording your movements.
        Or with your MotionX application on your iPhone.  Or with another device that
        can emit data in gpx format.
    b.  Connect your Garmin device to your computer, typically via a USB port.
    c.  Use your desktop software, such as Garmin Training Center, to import the GPS
        data from your GPS device.
    d.  Use your desktop software to export its data to a file in your 'GOOBY_HOME/data' directory.
        In Garmin Training Center, this is done with the File -> Export... menu.
    
    Part 2 - within the realm of Gooby:
    e.  Depending on your GPS device and desktop software, you'll use the following commands
        to parse a data file into the "gooby standard csv format":
        - rake gooby:extract_activities_from_tcx   # Garmin 305 & Garmin Training Center
        - rake gooby:parse_activity_xml_to_csv     # Garmin 305 & Garmin Training Center
        - rake gooby:parse_track_log_to_csv        # Garmin eTrex Venture & MacGpsPro
        - rake gooby:parse_gpx_to_csv              # MotionX app on iPhone

        Note that files in "gooby standard csv format" can be used to generate either 
        Google Maps or Google Earth Maps... there is no need to recreate the csv file
        depending on what type of map you wish to create.

    f.  Manually create and edit a yaml configuration file in the /config directory for the
        specific map you want to generate.  For example: config/big_sur_marathon.yaml  
        Specify its input csv file, and any other appropriate yaml parameter values.
        This design approach was taken so that you can create a configuration file for
        each map, then essentially not have to modify that file again to regenerate the map.
        Be sure to set the value of 'gmap_key' to your own Google Maps key.

    g.  Run command 'rake gooby:generate_google_map' to generate a Google Map html file.
        View the file in your browser, and optionally deploy it to your web site.

    h.  Run command 'rake gooby:generate_google_earth_map' to generate a Google Earth kml file.
        View the file in your Google Earth software.

    i.  Example commands, see file samples.sh

        rake 

        rake gooby:extract_activities_from_tcx

        rake gooby:parse_activity_xml_to_csv  config_file=config/big_sur_marathon.yaml

        rake gooby:parse_track_log_to_csv     config_file=config/crowders_mtn_hike.yaml

        rake gooby:parse_gpx_to_csv           config_file=config/ballantyne.yaml

        rake gooby:generate_google_map        config_file=config/big_sur_marathon.yaml
        rake gooby:generate_google_map        config_file=config/crowders_mtn_hike.yaml
        rake gooby:generate_google_map        config_file=config/ballantyne.yaml

        rake gooby:generate_google_earth_map  config_file=config/big_sur_marathon.yaml
        rake gooby:generate_google_earth_map  config_file=config/crowders_mtn_hike.yaml
        rake gooby:generate_google_earth_map  config_file=config/ballantyne.yaml


== Online Resources

*   Gooby may be downloaded from http://rubyforge.org/projects/gooby/.

*   Gooby project site is http://www.joakim-systems.com/gooby

*   Sample maps are available at: http://www.joakim-systems.com/maps

*   Gooby cucumber tests are available at: http://www.joakim-systems.com/cuke


== This Release - version 2.0.0

*  The gooby 2.0.0 codebase is essentially a complete rewrite, featuring:

   - 'libxml' is now used for xml parsing instead of 'rexml'.

   - csv creation and reading with 'fastercsv'.

   - use of cucumber and rspec rather than test/unit for automated testing.

*  Simplified functionality:

   - Device focus - parses data from your Garmin 205/305 and Garmin eTrex devices
     via your desktop software such as Garmin Training Center and/or MacGpsPro.

     A late addition to this release was gpx xml file support, such as from the
     iPhone "MotionX GPS" application.

   - Data focus - the specific Garmin device data is formatted into a common csv format.
     You may optionally import the csv files created by gooby into your database of choice.
     Gooby itself, however, does not require the use of a database.

   - Google Map html generation, from common csv input.

   - Google Earth kml generation, from common csv input.

   - The 'GOOBY_HOME' environment variable is required; a user-defined value.
     Rails-like "sensible default" directory structure within your 'GOOBY_HOME' directory.

   - Configuration yaml files are now a "base plus map-specific" design.  A core yaml file
     defines most configuration parameters; while map-specific configuration yaml files
     enable you to override the base values for each particular map you create.  
     This results in less need to constantly modify the configuration values for each map
     you want to generate.

   - Focus is on the English system of units, rather than the metric system.


== Road Map / TODO List

*  No specific plans currently.  Future functionality is dependent on my future mapping
   needs, Google API evolution, and user feedback.  Interesting ideas are appreciated.


== Support

*  Please see the Tracker page at http://rubyforge.org/projects/gooby/ to submit a request
   or to report a bug.

    
== Warranty

This software is provided "as is" and without any express or implied warranties, including, 
without limitation, the implied warranties of merchantibility and  fitness for a particular purpose.


== Release Notes on RubyForge

Version 2.0.0; essentially a complete rewrite.  Added Google Earth KML support in addition to the 
original Google Map HTML/JS generation.  Added GPX parsing, such as for the MotionX iPhone app.  
Added eTrex Venture GPS log parsing.  The rewrite now uses the libxml and fastercsv gems.  
Extensive cucumber tests for core functionality, packaging, and installation.
