require 'spec_helper'

describe "Class Gooby::XmlParser" do

  describe "instance methods" do

    it "should determine a json filename from a tcx or gpx suffixed filename" do
      p = Gooby::XmlParser.new
      p.filename = 'samples/data/2012-07-11-Dav7.tcx'
      p.json_filename.should == 'samples/data/2012-07-11-Dav7.json'
    end

    it "should determine a json filename from a no-suffixed filename" do
      p = Gooby::XmlParser.new
      p.filename = 'samples/data/2012-07-11-Dav7'
      p.json_filename.should == 'samples/data/2012-07-11-Dav7.json'
    end
    
    it "should determine a json filename from a no-suffixed filename" do
      p = Gooby::XmlParser.new
      p.parse_tcx('samples/data/2012-07-11-Dav7.tcx')
      p.filename = 'samples/data/2012-07-11-Dav7.tcx'
      p.json_filename.should == 'samples/data/2012-07-11-Dav7.json'
      p.document.trackpoints.size.should == 1121
    end

  end

end