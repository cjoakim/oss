=begin

Gooby = Google APIs + Ruby.  Copyright 2011 by Chris Joakim.
Gooby is available under GNU General Public License (GPL) license.

=end

require 'fileutils'

class GoobySetup
   
  def initialize
    @test = false
    ARGV.each { | arg | @test = true if arg == 'test' }
    
    if gooby_home
      puts "Your GOOBY_HOME is: #{gooby_home}"
      FileUtils.mkdir_p(gooby_home)
      dirs = []
      dirs << 'config'
      dirs << 'csv'
      dirs << 'data'
      dirs << 'features'
      dirs << 'features/steps'
      dirs << 'features/support'
      dirs << 'out'
      dirs << 'out/images'
      dirs << 'samples'
      dirs << 'splits'
      dirs << 'tmp'   
      dirs.each { | dir | 
        filename = "#{gooby_home}/#{dir}"
        puts "creating #{filename}"
        FileUtils.mkdir_p(filename) 
      }
      FileUtils.cp   'README',             "#{gooby_home}"
      FileUtils.cp   'cucumber.yml',       "#{gooby_home}"
      FileUtils.cp   'rakefile.rb',        "#{gooby_home}"
      FileUtils.cp   'setup.rb',           "#{gooby_home}"
      FileUtils.cp   'samples.sh',         "#{gooby_home}"      
      FileUtils.cp_r 'config/.',           "#{gooby_home}/config"
      FileUtils.cp   'samples/2008_04_27_13_49_50_tcx.csv', "#{gooby_home}/csv"  
      FileUtils.cp_r 'features/.',         "#{gooby_home}/features"
      FileUtils.cp_r 'features/steps/.',   "#{gooby_home}/features/steps"
      FileUtils.cp_r 'features/support/.', "#{gooby_home}/features/support"
      FileUtils.cp_r 'out/images/.',       "#{gooby_home}/out/images"
      FileUtils.cp_r 'samples/.',          "#{gooby_home}/data"
      FileUtils.cp_r 'samples/.',          "#{gooby_home}/samples"
    else
      puts "ERROR: The required GOOBY_HOME environment variable has not yet been defined."
      puts "The GOOBY_HOME variable must be set to the directory filename where you will"
      puts "store your Gooby-related files, and where Gooby will generate content."
      puts "Suggested values are 'C:\\gooby' on Windows, and '~/gooby' on unix-based systems."
      puts "Please define the GOOBY_HOME environment varible, then rerun setup.rb."
    end
  end

  def gooby_home
    (@test) ? ENV['GOOBY_TEST'] : ENV['GOOBY_HOME']
  end
    
end

# For developer testing of setup.rb: ruby setup.rb test

GoobySetup.new
