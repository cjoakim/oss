require 'simplecov'
SimpleCov.start do
  add_filter "/spec/"
end

require 'rspec'
require 'gooby'

RSpec.configure do | config |
  config.color_enabled = true
  config.formatter     = 'documentation'
end

def array_contains(array, txt)
  result = false
  array.each { | line |
    result = true if line.index(txt) 
  }
  result  
end

def write_test_file(out_name, content, verbose=false) 
  FileUtils.mkdir_p('tmp/test/')
  out = File.new "tmp/test/#{out_name}", "w+"
  out.write content
  out.flush
  out.close
  puts "file written: #{out_name}" if verbose
end
