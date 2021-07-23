## counter-hash-js

### Purpose

A Node.js library implementing a simple CounterHash class, for incrementing and
decrementing keys.

Often it is useful to traverse some data structure, accumulating conters in the process.
Class CounterHash provides functions to increment, decrement, add, subtract, and obtain
the sum, values, and sorted-keys of the hash.

### Examples

#### Setup

Add counter-hash-js to your project or package.json file:
```
npm install counter-hash-js
```

Require counter-hash-js in your code:
```
CounterHash  = require("counter-hash-js").CounterHash
```

Note: this library is now implemented in TypeScript, but these examples are in CoffeeScript.
For users of TypeScript, see the declaration file for this library at:

https://github.com/cjoakim/counter-hash-js/blob/master/lib/counter-hash-js.d.ts

#### CounterHash

Methods value(key), increment(key), decrement(key), add(key, n), subtract(key, n), value(key),
sum(), sorted_keys(), and sorted_tuples() are available.


```
h = new CounterHash()
h.increment('a')
h.increment('a')
h.increment('b')
h.decrement('q')
h.increment('z')

h.sum()       -> 3

h.value('a')  -> 2
h.value('x')  -> undefined

h.add('x', 100)
h.subtract('x', 7)

h.value('x')  -> 93

h.sorted_keys() -> [ 'a', 'b', 'q', 'x', 'z' ]

h.sorted_tuples() -> [ ['a', 2], ['b', 1],['q', -1], ['z', 1] ]

CounterHash.VERSION  -> '0.2.0'
```

### Test Results
```
Running "mocha_istanbul:coverage" (mocha_istanbul) task

  CounterHash
    read_file_sync
      ✓ should have a constructor
      ✓ should have a VERSION
      ✓ should implement methods: increment, decrement, and sum
      ✓ should implement methods: add and subtract
      ✓ should implement method: values
      ✓ should implement method: sorted_keys
      ✓ should implement method: sorted_tuples


  7 passing (10ms)

=============================================================================
Writing coverage object [/Users/cjoakim/github/counter-hash-js/coverage/coverage.json]
Writing coverage reports at [/Users/cjoakim/github/counter-hash-js/coverage]
=============================================================================

=============================== Coverage summary ===============================
Statements   : 100% ( 54/54 )
Branches     : 88.89% ( 16/18 )
Functions    : 100% ( 11/11 )
Lines        : 100% ( 54/54 )
================================================================================
```

### Release History

* 2015-05-02   v0.2.0  Implemented in TypeScript; added file 'counter-hash-js.d.ts'.
* 2015-02-20   v0.1.2  Added method 'sorted_tuples()'.
* 2015-01-13   v0.1.1  Docs updated.
* 2015-01-13   v0.1.0  Initial working version.
* 2015-01-13   v0.0.2  alpha 2
* 2015-01-13   v0.0.1  alpha 1
