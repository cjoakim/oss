(function() {
  var CounterHash, fs, h, sb, sprintf;

  fs = require('fs');

  sprintf = require("sprintf-js").sprintf;

  sb = require("sb-js");

  CounterHash = require("counter-hash-js").CounterHash;

  h = new CounterHash();

  h.increment('a');

  h.increment('b');

  h.increment('c');

  h.increment('a');

  h.decrement('d');

  h.add('b', 7);

  h.subtract('b', 7);

  console.log(JSON.stringify(h.values, null, 2));

}).call(this);
