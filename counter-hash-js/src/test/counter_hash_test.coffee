
assert      = require("assert")
should      = require('should')
fs          = require('fs')
sb          = require('sb-js')
CounterHash = require('../lib/counter-hash-js.js').CounterHash

describe 'CounterHash', ->

  before (done) ->
    done()

  after (done) ->
    done()

  describe 'read_file_sync', ->

    it 'should have a constructor', (done) ->
      h = new CounterHash()
      h.values.should.be.an.instanceOf(Object)
      done()

    it 'should have a VERSION', (done) ->
      CounterHash.VERSION.should.eql('0.2.0')
      done()

    it 'should implement methods: increment, decrement, and sum', (done) ->
      h = new CounterHash()
      h.value('a').should.eql(0)
      h.sum().should.eql(0)
      h.increment('a')
      h.value('a').should.eql(1)
      h.increment('a')
      h.increment('a')
      h.increment('b')
      h.value('a').should.eql(3)
      h.value('b').should.eql(1)
      h.value('z').should.eql(0)
      h.sum().should.eql(4)

      h.decrement('a')
      h.value('a').should.eql(2)
      h.sum().should.eql(3)

      h.decrement('q')
      h.value('q').should.eql(-1)
      h.sum().should.eql(2)
      done()

    it 'should implement methods: add and subtract', (done) ->
      h = new CounterHash()
      h.value('a').should.eql(0)
      h.add('a', 42)
      h.increment('b')
      h.value('a').should.eql(42)
      h.sum().should.eql(43)

      h.add('a', null)
      h.add(null, 4)
      h.sum().should.eql(43)

      h.subtract('a', 10)
      h.value('a').should.eql(32)
      h.sum().should.eql(33)

      h.subtract('a', null)
      h.subtract(null, 4)
      h.sum().should.eql(33)

      done()

    it 'should implement method: values', (done) ->
      h = new CounterHash()
      h.increment('z')
      h.increment('a')
      h.decrement('q')
      h.increment('b')
      obj = h.values
      obj.should.be.an.instanceOf(Object)
      obj.a.should.eql(1)
      obj.b.should.eql(1)
      obj.q.should.eql(-1)
      obj.z.should.eql(1)
      done()

    it 'should implement method: sorted_keys', (done) ->
      h = new CounterHash()
      h.sorted_keys().should.eql([])
      h.increment('z')
      h.increment('a')
      h.decrement('q')
      h.increment('b')
      h.sorted_keys().should.eql([ 'a', 'b', 'q', 'z' ])
      done()

    it 'should implement method: sorted_tuples', (done) ->
      h = new CounterHash()
      h.increment('z')
      h.increment('a')
      h.decrement('q')
      h.increment('b')
      h.increment('a')
      h.sorted_tuples().should.eql([ ['a', 2], ['b', 1],['q', -1], ['z', 1] ])
      done()
