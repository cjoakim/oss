require 'spec_helper'

describe "Class Gooby::DateTime" do

  describe "instance methods" do

    it "should construct an invalid instance from nil" do
      dt = Gooby::DateTime.new(nil)
      dt.class.name.should == 'Gooby::DateTime'
      dt.valid?.should be_false
      dt.time.should be_nil
      dt.to_i.should < 0
    end

    it "should construct an invalid instance from an empty string" do
      dt = Gooby::DateTime.new('')
      dt.class.name.should == 'Gooby::DateTime'
      dt.valid?.should be_false
      dt.time.should be_nil
      dt.to_i.should < 0
    end

    it "should construct an invalid instance from a malformed string" do
      dt = Gooby::DateTime.new('ham and eggs')
      dt.class.name.should == 'Gooby::DateTime'
      dt.valid?.should be_false
      dt.time.should be_nil
      dt.to_i.should < 0
    end

    it "should construct a valid instance from a properly formed string" do
      dt = Gooby::DateTime.new('2012-01-29T11:29:55Z')
      dt.class.name.should == 'Gooby::DateTime'
      dt.valid?.should be_true
      dt.time.should_not be_nil
      dt.time.class.name.should == 'Time'
      dt.time.to_s.should  == '2012-01-29 11:29:55 UTC'
      dt.yyyy_mm_dd.should == '2012-01-29'
      dt.yyyy_mm_dd_hh_mm_ss.should == '2012-01-29 11:29:55'
      dt.hh_mm_ss.should == '11:29:55'
      dt.to_s.should == '2012-01-29 11:29:55 1327836595'
    end
    
    it "should implement seconds_diff" do
      dt1 = Gooby::DateTime.new('2012-01-29T11:29:55Z')
      dt2 = Gooby::DateTime.new('2012-01-29T12:30:56Z')
      dt1.seconds_diff(dt1).should == 0
      dt1.seconds_diff(dt2).should == -3661
      dt2.seconds_diff(dt1).should == 3661
      dt2.seconds_diff(nil).should == dt2.invalid_time   
    end    

    it "should implement hhmmss_diff" do
      dt1 = Gooby::DateTime.new('2012-01-29T11:29:55Z')
      dt2 = Gooby::DateTime.new('2012-01-29T12:30:56Z')
      dt1.hhmmss_diff(dt1).should == '0:00:00'
      dt1.hhmmss_diff(dt2).should == '1:01:01'
      dt2.hhmmss_diff(dt1).should == '1:01:01'
      dt2.hhmmss_diff(nil).should == '?:??:??'
    end 
  end

end
