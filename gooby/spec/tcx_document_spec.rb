require 'spec_helper'

describe "Class Gooby::TcxDocument" do

  describe "instance methods" do

    it "should fail when parsing a non-existant file" do
      begin
        filename = 'samples/file_missing.tcx'
        document = Gooby::TcxDocument.new
        parser   = Nokogiri::XML::SAX::Parser.new(document)
        parser.parse(File.open(filename))
        fail('An exception should have been thrown')
      rescue Exception => e
        e.to_s.should == 'No such file or directory - samples/file_missing.tcx'
      end
    end

    it "should gracefully handle a malformed tcx file" do
      begin
        filename = 'samples/data/malformed.tcx'
        document = Gooby::TcxDocument.new
        parser   = Nokogiri::XML::SAX::Parser.new(document)
        parser.parse(File.open(filename))
        document.parsed?.should be_false
      rescue Exception => e
        fail("An exception should not have been thrown")
      end
    end

    it "should parse a properly formed tcx file" do
      begin
        filename = 'samples/data/2012-07-11-Dav7.tcx'
        document = Gooby::TcxDocument.new
        parser   = Nokogiri::XML::SAX::Parser.new(document)
        parser.parse(File.open(filename))
        document.parsed?.should be_true

        plain_json  = document.to_json(false)
        pretty_json = document.to_json(true)
        write_test_file('tcx_plain.json',  plain_json)
        write_test_file('tcx_pretty.json', pretty_json)

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
        tp['dist_meters'].should == '18.3099995'

        obj = JSON.parse(pretty_json)
        tp  = obj['trackpoints'][3]
        tp['seq'].should   == 4
        tp['time'].should  == '2012-07-11T10:49:31Z'
        tp['epoch'].should == 1342003771
        tp['elapsed'].should == '0:00:09'
        tp['lat'].should == '35.4954213'
        tp['lon'].should == '-80.8319024'
        tp['alt'].should == '249.8000000'
        tp['dist_meters'].should == '18.3099995'
        
        tp  = obj['trackpoints'][-1]
        tp['seq'].should   == 1121
        tp['time'].should  == '2012-07-11T11:55:11Z'
        tp['epoch'].should == 1342007711
        tp['elapsed'].should == '1:05:49'
        tp['lat'].should == '35.4950335'
        tp['lon'].should == '-80.8309718'
        tp['alt'].should == '240.0000000'
        tp['dist_meters'].should == '11261.2402344'
        tp['miles'].to_f.should be_within(0.00000000000001).of(6.981968945312639)
      rescue Exception => e
        fail("An exception should not have been thrown #{e.inspect}")
      end
    end

  end

end