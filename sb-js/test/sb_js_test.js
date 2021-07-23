
/*
Copyright 2015, Christopher Joakim <christopher.joakim@gmail.com>
 */

(function() {
  var StringBuffer, assert, os, should;

  assert = require("assert");

  should = require('should');

  os = require('os');

  StringBuffer = require('../lib/sb-js.js').StringBuffer;

  describe('StringBuffer', function() {
    describe('VERSION number is exposed by the API', function() {
      return it('defines VERSION', function() {
        return StringBuffer.VERSION.should.eql('0.3.0');
      });
    });
    describe('original snake_case API', function() {
      it("should construct an empty instance with no constructor argument", function() {
        var sb;
        sb = new StringBuffer();
        (sb.to_string()).should.eql('');
        (sb.is_empty()).should.eql(true);
        sb.add('x');
        (sb.to_string()).should.eql('x');
        return (sb.is_empty()).should.eql(false);
      });
      it("should construct a populated instance with a constructor String argument", function() {
        var sb;
        sb = new StringBuffer('git');
        (sb.is_empty()).should.eql(false);
        (sb.to_string()).should.eql('git');
        sb.add(' push');
        return (sb.to_string()).should.eql('git push');
      });
      it("should implement method 'as_lines'", function() {
        var sb;
        sb = new StringBuffer("first" + os.EOL + "second");
        sb.newline();
        sb.add_line(null);
        sb.add_line(void 0);
        sb.add_line("third");
        return (sb.as_lines()).should.eql(['first', 'second', 'third', '']);
      });
      return it("should optionally trim the result of to_string", function() {
        var sb1, sb2;
        sb1 = new StringBuffer('  git  ');
        (sb1.to_string()).should.eql('  git  ');
        sb2 = new StringBuffer('  git  ');
        return (sb1.to_string(true)).should.eql('git');
      });
    });
    return describe('new camelCase API', function() {
      it("should construct an empty instance with no constructor argument", function() {
        var sb;
        sb = new StringBuffer();
        (sb.toString()).should.eql('');
        (sb.isEmpty()).should.eql(true);
        sb.add('x');
        (sb.toString()).should.eql('x');
        return (sb.isEmpty()).should.eql(false);
      });
      it("should construct a populated instance with a constructor String argument", function() {
        var sb;
        sb = new StringBuffer('git');
        (sb.isEmpty()).should.eql(false);
        (sb.toString()).should.eql('git');
        sb.add(' push');
        return (sb.toString()).should.eql('git push');
      });
      it("should implement method 'asLines'", function() {
        var sb;
        sb = new StringBuffer("first" + os.EOL + "second");
        sb.newLine();
        sb.addLine(null);
        sb.addLine(void 0);
        sb.addLine("third");
        return (sb.asLines()).should.eql(['first', 'second', 'third', '']);
      });
      return it("should optionally trim the result of toString", function() {
        var sb1, sb2;
        sb1 = new StringBuffer('  git  ');
        (sb1.toString()).should.eql('  git  ');
        sb2 = new StringBuffer('  git  ');
        return (sb1.toString(true)).should.eql('git');
      });
    });
  });

}).call(this);
