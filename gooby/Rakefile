=begin

Gooby = Google API's and Ruby
Gooby - Copyright 2012 by Chris Joakim.
Gooby is available under GNU General Public License (GPL) license.

=end

require 'rubygems'
require 'rake'

# The following prefixes /lib to the active ruby load path
$:.unshift File.join(File.dirname(__FILE__), "", "lib")
# $:.each { | path | puts path }

require 'gooby'

desc "Default Task; Display Gooby usage instructions."
task :default => [ 'gooby:help'.to_sym ]

namespace :gooby do

  desc "Display Gooby usage instructions."
  task :help do
    # GoobyProcess.new(:help)
  end

  desc "Parse a TCX file to a JSON file"
  task :parse_tcx_file do
    # rake gooby:parse_tcx_file f=samples/data/2012-07-11-Dav7.tcx
    if ENV['f']
      Gooby::XmlParser.new.parse_tcx(ENV['f'])
    else
      puts "no f=<filename> arg provided"
    end
  end
  
  desc "Generate Google Map JavaScript from a JSON file"
  task :generate_gmap_js do
    # rake gooby:generate_gmap_js c=config/gooby.yml
    Gooby::GmapGenerator.new(ENV['c'])
  end

end
