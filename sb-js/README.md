## sb-js

### Purpose

A Node.js library implementing a simple StringBuffer, much like the Java class.

Efficiently uses an Array internally, rather than continually appending Strings.


### Examples

#### Setup

Add sb-js to your project or package.json file:
```
npm install sb-js
```

Require sb-js in your code:
```
StringBuffer = require("sb-js").StringBuffer
```

Note: this library is now implemented in TypeScript, but these examples are in CoffeeScript.
For users of TypeScript, see the declaration file for this library at:

https://github.com/cjoakim/sb-js/blob/master/lib/sb-js.d.ts

#### StringBuffer

Construct a StringBuffer, optionally provide an initial String value.

Original "snake_case" methods add(), add_line(), newline(), to_string(), as_lines(), and is_empty() are available.
Corresponding new "camelCase" methods addLine(), newLine(), toString(), asLines(), and isEmpty() are also available.
```
sb = new StringBuffer()
sb.is_empty()  -> true
sb.isEmpty()  -> true
sb.to_string() -> ""
sb.toString() -> ""

sb.add("one")
sb.is_empty()  -> false

sb.add(",two")
sb.to_string() -> "one,two"

sb.newline()
sb.add_line("three")
sb.add_line(null)      // null values ignored
sb.addLine(undefined)  // undefined values ignored

sb.to_string() -> "one,two
three
"
sb.as_lines()  -> "["one,two","three",""]"
sb.asLines()  -> "["one,two","three",""]"

sb2 = new StringBuffer("  hello world  ")
sb2.is_empty()  ->  false
sb2.as_lines()  -> "["  hello world  "]"
sb2.to_string() -> "  hello world  "
sb2.to_string(true) -> "hello world"

StringBuffer.VERSION  -> 0.3.0
```

### Test Results
```
Running "mocha_istanbul:coverage" (mocha_istanbul) task


  StringBuffer
    VERSION number is exposed by the API
      ✓ defines VERSION
    original snake_case API
      ✓ should construct an empty instance with no constructor argument
      ✓ should construct a populated instance with a constructor String argument
      ✓ should implement method 'as_lines'
      ✓ should optionally trim the result of to_string
    new camelCase API
      ✓ should construct an empty instance with no constructor argument
      ✓ should construct a populated instance with a constructor String argument
      ✓ should implement method 'asLines'
      ✓ should optionally trim the result of toString


  9 passing (10ms)

=============================================================================
Writing coverage object [/Users/cjoakim/github/sb-js/coverage/coverage.json]
Writing coverage reports at [/Users/cjoakim/github/sb-js/coverage]
=============================================================================

=============================== Coverage summary ===============================
Statements   : 100% ( 46/46 )
Branches     : 92.86% ( 13/14 )
Functions    : 100% ( 14/14 )
Lines        : 100% ( 46/46 )
================================================================================
```

### Release History

* 2015-05-02   v0.3.0  Renamed the source to sb-js so as to generate file 'lib/sb-js.d.ts'.
* 2015-04-22   v0.2.0  Implementation language is now TypeScript.  API expanded to both snake_case and camelCase.
* 2015-01-24   v0.1.1  Changed line endings from "\n" to os.EOL.  Replaced jasmine with mocha and istanbul.
* 2014-11-06   v0.1.0  Initial working version; implemented in CoffeeScript.
* 2014-11-06   v0.0.1  alpha 1
