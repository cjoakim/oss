// Unit tests for class GeoJsonLocation
// Chris Joakim, 2019/07/26

const assert = require('assert');
const chai   = require('chai');
const GeoJsonLocation = require('../dist/tcx.js').GeoJsonLocation;

// https://www.chaijs.com/api/assert/#method_istrue

describe('GeoJsonLocation', function() {

  describe('#constructor()', function() {

    it('It should return the correct value for Davidson College', function() {
      var lat = 35.499584;
      var lng = -80.842842;
      var loc = new GeoJsonLocation(lat, lng);
      var jstr = JSON.stringify(loc);
      var obj = JSON.parse(jstr)
      //console.log(jstr);
      chai.assert.isTrue(loc.coordinates[0] === lng, 'the coordinates array longitude value is incorrect');
      chai.assert.isTrue(loc.coordinates[1] === lat, 'the coordinates array latitude value is incorrect');
      chai.assert.isTrue(jstr === '{"type":"Point","coordinates":[-80.842842,35.499584]}', 'the JSON string is incorrect');
    });


  });

});
