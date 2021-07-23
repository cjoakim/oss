###
Copyright 2015, Christopher Joakim <christopher.joakim@gmail.com>
###

# grunt ; mocha test/sb_js_test.js

assert = require("assert")
should = require('should')
os     = require('os')

StringBuffer = require('../lib/sb-js.js').StringBuffer


describe 'StringBuffer', ->

  describe 'VERSION number is exposed by the API', ->

    it 'defines VERSION', ->
      (StringBuffer.VERSION).should.eql('0.3.0')

  describe 'original snake_case API', ->

    it "should construct an empty instance with no constructor argument", ->
      sb = new StringBuffer()
      (sb.to_string()).should.eql('')
      (sb.is_empty()).should.eql(true)
      sb.add('x')
      (sb.to_string()).should.eql('x')
      (sb.is_empty()).should.eql(false)

    it "should construct a populated instance with a constructor String argument", ->
      sb = new StringBuffer('git')
      (sb.is_empty()).should.eql(false)
      (sb.to_string()).should.eql('git')
      sb.add(' push')
      (sb.to_string()).should.eql('git push')

    it "should implement method 'as_lines'", ->
      sb = new StringBuffer("first" + os.EOL + "second")
      sb.newline()
      sb.add_line(null)
      sb.add_line(undefined)
      sb.add_line("third")
      (sb.as_lines()).should.eql(['first', 'second', 'third', ''])

    it "should optionally trim the result of to_string", ->
      sb1 = new StringBuffer('  git  ')
      (sb1.to_string()).should.eql('  git  ')
      sb2 = new StringBuffer('  git  ')
      (sb1.to_string(true)).should.eql('git')

  describe 'new camelCase API', ->

    it "should construct an empty instance with no constructor argument", ->
      sb = new StringBuffer()
      (sb.toString()).should.eql('')
      (sb.isEmpty()).should.eql(true)
      sb.add('x')
      (sb.toString()).should.eql('x')
      (sb.isEmpty()).should.eql(false)

    it "should construct a populated instance with a constructor String argument", ->
      sb = new StringBuffer('git')
      (sb.isEmpty()).should.eql(false)
      (sb.toString()).should.eql('git')
      sb.add(' push')
      (sb.toString()).should.eql('git push')

    it "should implement method 'asLines'", ->
      sb = new StringBuffer("first" + os.EOL + "second")
      sb.newLine()
      sb.addLine(null)
      sb.addLine(undefined)
      sb.addLine("third")
      (sb.asLines()).should.eql(['first', 'second', 'third', ''])

    it "should optionally trim the result of toString", ->
      sb1 = new StringBuffer('  git  ')
      (sb1.toString()).should.eql('  git  ')
      sb2 = new StringBuffer('  git  ')
      (sb1.toString(true)).should.eql('git')
