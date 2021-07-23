require 'spec_helper'

describe "Class Gooby::GpxDocument" do

  describe "instance methods" do

    it "should fail when parsing a non-existant file" do
      begin
        filename = 'samples/file_missing.gpx'
        document = Gooby::GpxDocument.new
        parser   = Nokogiri::XML::SAX::Parser.new(document)
        parser.parse(File.open(filename))
        fail('An exception should have been thrown')
      rescue Exception => e
        e.to_s.should == 'No such file or directory - samples/file_missing.gpx'
      end
    end

    it "should gracefully handle a malformed gpx file" do
      begin
        filename = 'samples/data/malformed.gpx'
        document = Gooby::GpxDocument.new
        parser   = Nokogiri::XML::SAX::Parser.new(document)
        parser.parse(File.open(filename))
        document.parsed?.should be_false
      rescue Exception => e
        fail("An exception should not have been thrown: #{e.message}")
      end
    end

    it "should parse a properly formed gpx file" do
      begin
        filename = 'samples/data/2012-07-11-Dav7.gpx'
        document = Gooby::GpxDocument.new
        parser   = Nokogiri::XML::SAX::Parser.new(document)
        parser.parse(File.open(filename))
        document.parsed?.should be_true

        plain_json  = document.to_json(false)
        pretty_json = document.to_json(true)
        write_test_file('gpx_plain.json',  plain_json)
        write_test_file('gpx_pretty.json', pretty_json)

        plain_json.should_not be_nil
        pretty_json.should_not be_nil

        obj = JSON.parse(plain_json)
        tp  = obj['trackpoints'][3]
        tp['seq'].should   == 4
        tp['time'].should  == '2012-07-11T10:49:31Z'
        tp['epoch'].should == 1342003771
        tp['elapsed'].should == '0:00:09'
        tp['lat'].should == '35.4954213'
        tp['lon'].should == '-80.8319024'
        tp['alt'].should == '249.8000000'

        obj = JSON.parse(pretty_json)
        tp  = obj['trackpoints'][3]
        tp['seq'].should   == 4
        tp['time'].should  == '2012-07-11T10:49:31Z'
        tp['epoch'].should == 1342003771
        tp['elapsed'].should == '0:00:09'
        tp['lat'].should == '35.4954213'
        tp['lon'].should == '-80.8319024'
        tp['alt'].should == '249.8000000'
      rescue Exception => e
        fail('An exception should not have been thrown')
      end
    end

  end

end