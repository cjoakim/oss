require 'spec_helper'

describe "Class Gooby::Config" do
  
  describe "instance methods with a missing yml file" do

    before(:all) do
      @config = Gooby::Config.new('config/oops_not_found.yml')
    end
  
    it "should attempt to load the yml file" do
      @config.filename.should == 'config/oops_not_found.yml'
      @config.values.size.should == 0
    end
    
    it "should implement approx_max_points and return the default" do
      @config.approx_max_points.should == 200
    end
    
    it "should implement json_data_file and return the default" do
      @config.json_data_file.should == ''
    end
  end
  
  describe "instance methods with a valid yml file" do

    before(:all) do
      @config = Gooby::Config.new
    end
  
    it "should load a yml file" do
      @config.filename.should == 'config/gooby.yml'
      @config.values.size.should > 0
    end
    
    it "should implement json_data_file" do
      @config.json_data_file.should == 'samples/data/2012-07-11-Dav7.json'
    end

    it "should implement approx_max_points" do
      @config.approx_max_points.should == 500
    end
    
    it "should implement map_dom_element_id" do
      @config.map_dom_element_id.should == 'map_canvas'
    end
    
    it "should implement gmap_api_key" do
      @config.gmap_api_key.index('SyDk').should > 0
    end
    
    it "should implement gmap_type" do
      @config.gmap_type.should == 'TERRAIN'
    end
    
    it "should implement gmap_route_color" do
      @config.gmap_route_color.should == 'FF0001'
    end
    
    it "should implement gmap_route_opacity" do
      @config.gmap_route_opacity.to_s.should == '0.66'
    end
    
    it "should implement gmap_route_weight" do
      @config.gmap_route_weight.should == 2
    end
    
    it "should implement gmap_zoom_level" do
      @config.gmap_zoom_level.should == 14
    end
    
    it "should implement include_start_finish_markers?" do
      @config.include_start_finish_markers?.should == true
    end
    
    it "should implement include_mile_markers" do
      @config.include_mile_markers?.should == true
    end
    
    it "should implement start_marker_color" do
      @config.start_marker_color.should == '00FF00'
    end
    
    it "should implement finish_marker_color" do
      @config.finish_marker_color.should == 'FF0000'
    end
    
    it "should implement mile_marker_color" do
      @config.mile_marker_color.should == '0000FF'
    end
    
    it "should implement mile_marker_title_detail" do
      @config.mile_marker_title_detail.should == 'miles,elapsed,pace,mph'
    end
    
    # it "should implement xxx" do
    #   @config.xxx.should == ''
    # end
    # 
    # it "should implement xxx" do
    #   @config.xxx.should == ''
    # end
    # 
    # it "should implement xxx" do
    #   @config.xxx.should == ''
    # end
    # 
    # it "should implement xxx" do
    #   @config.xxx.should == ''
    # end
    # 
    # it "should implement xxx" do
    #   @config.xxx.should == ''
    # end
      
  end

end
