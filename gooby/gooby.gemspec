=begin

Gooby = Google APIs + Ruby.  Copyright 2011 by Chris Joakim.
Gooby is available under GNU General Public License (GPL) license.

=end

require 'rubygems' 
require 'rake'

SPEC = Gem::Specification.new do | s |
  s.name                  = "gooby" 
  s.version               = "3.0.0" 
  s.author                = "Chris Joakim" 
  s.email                 = "chris@joakimsoftware.com" 
  s.homepage              = "http://rubyforge.org/projects/gooby/" 
  s.platform              = Gem::Platform::RUBY 
  s.rubyforge_project     = 'gooby'
  s.description           = "Generate Google & Google Earth maps from your GPS data." 
  s.summary               = "Google APIs + Ruby = Gooby." 
  s.require_paths         = ["lib"] 
  s.has_rdoc              = true 
  s.extra_rdoc_files      = ["README.md"]
  s.required_ruby_version = '>= 1.9.3'
  
  patterns = []
  patterns << 'config/*'
  patterns << 'lib/**/*.rb'
  patterns << 'samples/*'
  patterns << 'spec/*'
  patterns << 'Rakefile'
  patterns << 'setup.rb'
  s.files = FileList[patterns]
end 
