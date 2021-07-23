
/*
This purpose of this file is to test the generated sb.js file, outside of jasmine,
before deployment to npm.  It (accurately) generates Examples section of the README.md
file based on actual working code and output.
Copyright 2015, Christopher Joakim <christopher.joakim@gmail.com>
 */

(function() {
  var StringBuffer, sb, sb2;

  StringBuffer = require("./lib/sb-js.js").StringBuffer;

  console.log('');

  console.log('### Examples');

  console.log('');

  console.log('#### Setup');

  console.log('');

  console.log('Add sb-js to your project or package.json file:');

  console.log('```');

  console.log('npm install sb-js');

  console.log('```');

  console.log('');

  console.log('Require sb-js in your code:');

  console.log('```');

  console.log('StringBuffer = require("sb-js").StringBuffer');

  console.log('```');

  console.log('');

  console.log('Note: this library is now implemented in TypeScript, but these examples are in CoffeeScript.');

  console.log('');

  console.log('#### StringBuffer');

  console.log('');

  console.log('Construct a StringBuffer, optionally provide an initial String value.');

  console.log('');

  console.log('Original "snake_case" methods add(), add_line(), newline(), to_string(), as_lines(), and is_empty() are available.');

  console.log('Corresponding new "camelCase" methods addLine(), newLine(), toString(), asLines(), and isEmpty() are also available.');

  console.log('```');

  sb = new StringBuffer();

  console.log('sb = new StringBuffer()');

  console.log('sb.is_empty()  -> ' + sb.is_empty());

  console.log('sb.isEmpty()  -> ' + sb.isEmpty());

  console.log('sb.to_string() -> "' + sb.to_string() + '"');

  console.log('sb.toString() -> "' + sb.toString() + '"');

  console.log('');

  sb.add("one");

  console.log('sb.add("one")');

  console.log('sb.is_empty()  -> ' + sb.is_empty());

  console.log('');

  sb.add(",two");

  console.log('sb.add(",two")');

  console.log('sb.to_string() -> "' + sb.to_string() + '"');

  console.log('');

  sb.newline();

  console.log('sb.newline()');

  sb.add_line("three");

  console.log('sb.add_line("three")');

  console.log('sb.add_line(null)      // null values ignored');

  console.log('sb.addLine(undefined)  // undefined values ignored');

  console.log('');

  console.log('sb.to_string() -> "' + sb.to_string() + '"');

  console.log('sb.as_lines()  -> "' + JSON.stringify(sb.as_lines()) + '"');

  console.log('sb.asLines()  -> "' + JSON.stringify(sb.asLines()) + '"');

  console.log('');

  sb2 = new StringBuffer("  hello world  ");

  console.log('sb2 = new StringBuffer("  hello world  ")');

  console.log('sb2.is_empty()  ->  ' + sb2.is_empty());

  console.log('sb2.as_lines()  -> "' + JSON.stringify(sb2.as_lines()) + '"');

  console.log('sb2.to_string() -> "' + sb2.to_string() + '"');

  console.log('sb2.to_string(true) -> "' + sb2.to_string(true) + '"');

  console.log('');

  console.log('StringBuffer.VERSION  -> ' + StringBuffer.VERSION);

  console.log('```');

  console.log('');

}).call(this);
