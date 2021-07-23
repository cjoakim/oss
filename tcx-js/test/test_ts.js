// Unit tests for class Timestamp
// Chris Joakim, 2019/07/26

const assert = require('assert');
const chai   = require('chai');
const Timestamp = require('../dist/tcx.js').Timestamp;

// https://www.chaijs.com/api/assert/#method_istrue

describe('Timestamp', function() {

  describe('#constructor()', function() {

    it('It should return the correct value for 1970-01-01T00:00:00.000Z', function() {
      var ts = new Timestamp('1970-01-01T00:00:00.000Z');
      //console.log(ts.toString());
      chai.assert.isTrue(ts.epochMilliseconds === 0, 'the epochMilliseconds value is incorrect');
    });

    it('It should return the correct value for 1970-01-01T00:00:01.000Z', function() {
      var ts = new Timestamp('1970-01-01T00:00:01.000Z');
      //console.log(ts.toString());
      chai.assert.isTrue(ts.epochMilliseconds === 1000, 'the epochMilliseconds value is incorrect');
    });

    it('It should return the correct value for 1970-01-01T00:00:01.234Z', function() {
      var ts = new Timestamp('1970-01-01T00:00:01.234Z');
      //console.log(ts.toString());
      chai.assert.isTrue(ts.epochMilliseconds === 1234, 'the epochMilliseconds value is incorrect');
    });

    it('It should return the correct value for 2014-10-05T17:10:36.000Z', function() {
      var ts = new Timestamp('2014-10-05T17:10:36.000Z');
      //console.log(ts.toString());
      chai.assert.isTrue(ts.epochMilliseconds === 1412529036000, 'the epochMilliseconds value is incorrect');
    });

  });

});
