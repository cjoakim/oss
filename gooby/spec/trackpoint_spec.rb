require 'spec_helper'

describe "Class Gooby::Trackpoint" do

  describe "instance methods" do

    it "should default to source_type :tcx" do
      tp = Gooby::Trackpoint.new
      tp.class.name.should == 'Gooby::Trackpoint'
      tp.source_type.should == :tcx

      tp = Gooby::Trackpoint.new(:gpx)
      tp.class.name.should == 'Gooby::Trackpoint'
      tp.source_type.should == :gpx
    end

    it "should build :tcx instances, referring to previous for missing values" do
      start_datetime = Gooby::DateTime.new('2012-07-11T10:49:22Z')
      latest_values = Hash.new('')

      # # tp1 is the "previous trackpoint" to tp2
      tp1 = Gooby::Trackpoint.new(:tcx)
      tp1.set('Time', '2012-07-11T11:53:26Z')
      tp1.set('latitudedegrees', '35.4967512')
      tp1.set('longitudedegrees', '-80.8321533')
      tp1.set('altitudemeters', '231.2000000')
      tp1.set('distancemeters', '10000') 
      tp1.finish_parsing(55, latest_values, start_datetime)

      json_hash = tp1.json_hash
      json_hash['seq'].should == 56
      json_hash['time'].should == '2012-07-11T11:53:26Z'
      json_hash['epoch'].should == 1342007606
      json_hash['elapsed'].should == '1:04:04'
      json_hash['lat'].should == '35.4967512'
      json_hash['lon'].should == '-80.8321533'
      json_hash['alt'].should == '231.2000000'
      json_hash['miles'].to_f.should be_within(0.000000001).of(6.2)

      # Update the latest_values Hash from tp1, and add DistanceMeters
      keys = tp1.values.keys
      keys.each { | key |
        if tp1.values[key]
          latest_values[key] = tp1.values[key]
        end
      }
      latest_values['distancemeters'] = '123.45'

      tp2 = Gooby::Trackpoint.new(:tcx)
      tp2.set('time', '2012-07-11T11:53:31Z')
      tp2.finish_parsing(56, latest_values, start_datetime)

      json_hash = tp2.json_hash
      json_hash['seq'].should == 57
      json_hash['time'].should == '2012-07-11T11:53:31Z'
      json_hash['epoch'].should == 1342007611
      json_hash['elapsed'].should == '1:04:09'
      json_hash['lat'].should == '35.4967512'
      json_hash['lon'].should == '-80.8321533'
      json_hash['alt'].should == '231.2000000'
      json_hash['dist_meters'].should == '123.45'
    end

    it "should implement latitude, longitude, and same_location?" do
      start_datetime = Gooby::DateTime.new('2012-07-11T10:49:22Z')
      latest_values = Hash.new('')

      tp1 = Gooby::Trackpoint.new(:tcx)
      tp1.set('latitudedegrees', '35.4967512')
      tp1.set('longitudedegrees', '-80.8321533')

      tp2 = Gooby::Trackpoint.new(:gpx)
      tp2.set('lat', '35.4967512')
      tp2.set('lon', '-80.8321533')

      tp1.same_location?(tp1).should be_true
      tp1.same_location?(tp2).should be_true
      tp2.same_location?(tp2).should be_true
      tp2.same_location?(tp1).should be_true

      tp2.set('lon', '-80.8321534')
      tp1.same_location?(tp2).should be_false
      tp2.same_location?(tp1).should be_false

      tp2.set('lat', '35.4967513')
      tp2.set('lon', '-80.8321533')
      tp1.same_location?(tp2).should be_false
      tp2.same_location?(tp1).should be_false
    end

    it "should implement degrees_diff" do
      start_datetime = Gooby::DateTime.new('2012-07-11T10:49:22Z')
      latest_values = Hash.new('')

      tp1 = Gooby::Trackpoint.new(:tcx)
      tp1.set('latitudedegrees',   '35.5000000')
      tp1.set('longitudedegrees', '-80.8000000')

      tp2 = Gooby::Trackpoint.new(:tcx)
      tp2.set('latitudedegrees',   '35.6000000')
      tp2.set('longitudedegrees', '-80.7000000')

      tp1.degrees_diff(tp2).should be_within(0.00001).of(0.20)
      tp2.degrees_diff(tp1).should be_within(0.00001).of(0.20)
    end
    
    it "should implement proximity" do
      start_datetime = Gooby::DateTime.new('2012-07-11T10:49:22Z')
      latest_values = Hash.new('')

      tp1 = Gooby::Trackpoint.new(:tcx)
      tp1.set('latitudedegrees',   '35.4955307')
      tp1.set('longitudedegrees', '-80.8321425')

      tp2 = Gooby::Trackpoint.new(:tcx)
      tp2.set('latitudedegrees',   '35.4863787')
      tp2.set('longitudedegrees', '-80.8236485')

      tp1.proximity(tp2).should be_within(0.00001).of(0.7925452460970286)
      tp2.proximity(tp1).should be_within(0.00001).of(0.7925452460970286)
    end

    it "should implement a constructor from a (JSON) Hash" do
      config = Gooby::Config.new
      hash = {
        "seq" => 663,
        "time" => "2012-07-11T11:27:13Z",
        "epoch" => 1342006033,
        "elapsed" => "0:37:51",
        "miles" => 4.04070105466311,
        "pace" => "9:22.03",
        "mph" => "6.405",
        "lat" => "35.4862804",
        "lon" => "-80.8474744",
        "alt" => "252.0000000",
        "dist_meters" => "6517.2597656"
      }
      tp = Gooby::Trackpoint.new(:tcx, hash)
      tp.sequence.should == 663
      tp.longitude.should == "-80.8474744"
      tp.get('lon').should == "-80.8474744"
      tp.time.should == '2012-07-11 11:27:13'
      tp.to_s.index('"epoch"=>1342006033,').should > 0
      tp.altitude_ft.should be_within(0.5).of(826.812)
      tp.is_mile_marker?.should be_false
      tp.include_in_map?.should be_false
      tp.start_marker_title(config).should == 'Start, 2012-07-11 11:27:13'
      tp.finish_marker_title(config).should == 'Finish, 4.0407, 0:37:51, 9:22.03, 6.405'
      tp.mile_marker_title(config).should == 'Mile 4, 4.0407, 0:37:51, 9:22.03, 6.405'
      tp.as_LatLng.should == 'new google.maps.LatLng(35.4862804, -80.8474744), // 663 '
      tp.same_location?(tp).should be_true
      tp.same_location?(nil).should be_false
      tp.degrees_diff(tp).should be_within(0.0000000001).of(0.0) 
      tp.degrees_diff(nil).should be_within(0.0000000001).of(360.0) 
      tp.proximity(tp).should be_within(0.0000000001).of(0.0) 
    end

  end

end