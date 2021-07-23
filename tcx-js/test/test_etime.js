// Unit tests for class ElapsedTime
// Chris Joakim, 2019/07/26

const assert = require('assert');
const chai   = require('chai');
const chaiAlmost = require('chai-almost');
const expect = chai.expect

const ElapsedTime = require('../dist/tcx.js').ElapsedTime;

//chai.use(chaiAlmost());
chai.use(chaiAlmost(0.00000001));

// https://www.chaijs.com/api/assert/#method_istrue

describe('ElapsedTime', function() {

  describe('#constructor()', function() {

    it('It should define constant values', function() {
      expect(ElapsedTime.MILLISECONDS_PER_SECOND).to.be.almost(1000.0);
      expect(ElapsedTime.SECONDS_PER_HOUR).to.be.almost(3600.0);
      expect(ElapsedTime.SECONDS_PER_MINUTE).to.be.almost(60.0);

      ElapsedTime.MILLISECONDS_PER_SECOND = 0;

      expect(ElapsedTime.MILLISECONDS_PER_SECOND).to.be.almost(1000.0);
      expect(ElapsedTime.SECONDS_PER_HOUR).to.be.almost(3600.0);
      expect(ElapsedTime.SECONDS_PER_MINUTE).to.be.almost(60.0);
    });

    it('It should return the correct value for 0 ms', function() {
      var ms = 0;
      var et = new ElapsedTime(ms);
      chai.assert.isTrue(et.elapsedMs === ms, 'the ElapsedTime elapsedMs value is incorrect');
      chai.assert.isTrue(et.secs === 0, 'the ElapsedTime secs value is incorrect');
      chai.assert.isTrue(et.hh === 0, 'the ElapsedTime hh value is incorrect');
      chai.assert.isTrue(et.mm === 0, 'the ElapsedTime mm value is incorrect');
      chai.assert.isTrue(et.ss === 0, 'the ElapsedTime ss value is incorrect');
      chai.assert.isTrue(et.asHHMMSS() === '00:00:00', 'the ElapsedTime asHHMMSS() value is incorrect');
    });

    it('It should return the correct value for 1000 ms', function() {
      var ms = 1000;
      var et = new ElapsedTime(ms);
      chai.assert.isTrue(et.elapsedMs === ms, 'the ElapsedTime elapsedMs value is incorrect');
      chai.assert.isTrue(et.secs === 1, 'the ElapsedTime secs value is incorrect');
      chai.assert.isTrue(et.hh === 0, 'the ElapsedTime hh value is incorrect');
      chai.assert.isTrue(et.mm === 0, 'the ElapsedTime mm value is incorrect');
      chai.assert.isTrue(et.ss === 1, 'the ElapsedTime ss value is incorrect');
      chai.assert.isTrue(et.asHHMMSS() === '00:00:01', 'the ElapsedTime asHHMMSS() value is incorrect');
    });

    it('It should return the correct value for -1000 ms', function() {
      var ms = -1000;
      var et = new ElapsedTime(ms);
      chai.assert.isTrue(et.elapsedMs === 1000, 'the ElapsedTime elapsedMs value is incorrect');
      chai.assert.isTrue(et.secs === 1, 'the ElapsedTime secs value is incorrect');
      chai.assert.isTrue(et.hh === 0, 'the ElapsedTime hh value is incorrect');
      chai.assert.isTrue(et.mm === 0, 'the ElapsedTime mm value is incorrect');
      chai.assert.isTrue(et.ss === 1, 'the ElapsedTime ss value is incorrect');
      chai.assert.isTrue(et.asHHMMSS() === '00:00:01', 'the ElapsedTime asHHMMSS() value is incorrect');
    });

    it('It should return the correct value for 62000 ms', function() {
      var ms = 62000;
      var et = new ElapsedTime(ms);
      chai.assert.isTrue(et.elapsedMs === ms, 'the ElapsedTime elapsedMs value is incorrect');
      chai.assert.isTrue(et.secs === 62, 'the ElapsedTime secs value is incorrect');
      chai.assert.isTrue(et.hh === 0, 'the ElapsedTime hh value is incorrect');
      chai.assert.isTrue(et.mm === 1, 'the ElapsedTime mm value is incorrect');
      chai.assert.isTrue(et.ss === 2, 'the ElapsedTime ss value is incorrect');
      chai.assert.isTrue(et.asHHMMSS() === '00:01:02', 'the ElapsedTime asHHMMSS() value is incorrect');
    });

    it('It should return the correct value for 3663000 ms', function() {
      var ms = 3663000;
      var et = new ElapsedTime(ms);
      chai.assert.isTrue(et.elapsedMs === ms, 'the ElapsedTime elapsedMs value is incorrect');
      chai.assert.isTrue(et.secs === 3663, 'the ElapsedTime secs value is incorrect');
      chai.assert.isTrue(et.hh === 1, 'the ElapsedTime hh value is incorrect');
      chai.assert.isTrue(et.mm === 1, 'the ElapsedTime mm value is incorrect');
      chai.assert.isTrue(et.ss === 3, 'the ElapsedTime ss value is incorrect');
      chai.assert.isTrue(et.asHHMMSS() === '01:01:03', 'the ElapsedTime asHHMMSS() value is incorrect');
    });

    it('It should return the correct value for 3663200 ms', function() {
      var ms = 3663200;  // round down
      var et = new ElapsedTime(ms);
      chai.assert.isTrue(et.elapsedMs === ms, 'the ElapsedTime elapsedMs value is incorrect');
      chai.assert.isTrue(et.secs === 3663, 'the ElapsedTime secs value is incorrect');
      chai.assert.isTrue(et.hh === 1, 'the ElapsedTime hh value is incorrect');
      chai.assert.isTrue(et.mm === 1, 'the ElapsedTime mm value is incorrect');
      chai.assert.isTrue(et.ss === 3, 'the ElapsedTime ss value is incorrect');
      chai.assert.isTrue(et.asHHMMSS() === '01:01:03', 'the ElapsedTime asHHMMSS() value is incorrect');
    });

    it('It should return the correct value for 3663700.1 ms', function() {
      var ms = 3663700.1;  // round up, with fraction
      var et = new ElapsedTime(ms);
      chai.assert.isTrue(et.elapsedMs === ms, 'the ElapsedTime elapsedMs value is incorrect');
      chai.assert.isTrue(et.secs === 3664, 'the ElapsedTime secs value is incorrect');
      chai.assert.isTrue(et.hh === 1, 'the ElapsedTime hh value is incorrect');
      chai.assert.isTrue(et.mm === 1, 'the ElapsedTime mm value is incorrect');
      chai.assert.isTrue(et.ss === 4, 'the ElapsedTime ss value is incorrect');
      chai.assert.isTrue(et.asHHMMSS() === '01:01:04', 'the ElapsedTime asHHMMSS() value is incorrect');
    });

  });

});
