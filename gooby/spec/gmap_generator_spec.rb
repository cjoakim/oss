require 'spec_helper'

describe "Class Gooby::GmapGenerator" do

  describe "instance methods" do

    it "should generate a the JavaScript for a Google map" do
      generator = Gooby::GmapGenerator.new('config/gooby.yml')
      generator.source_type.should == :tcx
      generator.tkpts.size.should == 1121
      generator.js_lines.size.should be_within(1).of(722)
      
      array_contains(generator.js_lines, '<script type="text/javascript" src="http://maps.googleapis.com/maps/api/js?key=A').should be_true
      array_contains(generator.js_lines, 'mapTypeId: google.maps.MapTypeId.TERRAIN,').should be_true
      array_contains(generator.js_lines, 'zoom: 14,').should be_true
      array_contains(generator.js_lines, 'new google.maps.LatLng(35.4955307, -80.8321425), // 1 ').should be_true
      array_contains(generator.js_lines, 'new google.maps.LatLng(35.4863787, -80.8236485), // 166 1.0').should be_true
      array_contains(generator.js_lines, 'strokeColor:   "#FF0001",').should be_true
      array_contains(generator.js_lines, 'var marker_latlng_start = new google.maps.LatLng(35.4955307, -80.8321425);').should be_true
      array_contains(generator.js_lines, 'position: marker_latlng_start,').should be_true
      array_contains(generator.js_lines, 'var marker_latlng_finish = new google.maps.LatLng(35.4950335, -80.8309718);').should be_true
      array_contains(generator.js_lines, 'position: marker_latlng_finish,').should be_true
      array_contains(generator.js_lines, 'title: "Start, 2012-07-11 10:49:22"').should be_true
      array_contains(generator.js_lines, 'title: "Finish, 6.9820, 1:05:49, 9:25.60, 6.365"').should be_true
      array_contains(generator.js_lines, 'var marker_latlng_mile_4 = new google.maps.LatLng(35.4861818, -80.8470072);').should be_true
      array_contains(generator.js_lines, 'title: "Mile 4, 4.0131, 0:37:37, 9:22.41, 6.401"').should be_true
      array_contains(generator.js_lines, '<script type="text/javascript">').should be_true
      array_contains(generator.js_lines, '</script>').should be_true
    end

  end

end
 