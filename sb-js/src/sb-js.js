// Copyright 2015, Christopher Joakim <christopher.joakim@gmail.com>
/// <reference path="../typedefs/node.d.ts" />
var os = require('os');
var StringBuffer = (function () {
    function StringBuffer(s) {
        this.data = [];
        if (this.populated(s)) {
            this.data.push(s);
        }
    }
    StringBuffer.prototype.is_empty = function () {
        if (this.data.length === 0) {
            return true;
        }
        else {
            return false;
        }
    };
    StringBuffer.prototype.isEmpty = function () {
        return this.is_empty();
    };
    StringBuffer.prototype.add = function (s) {
        if (this.populated(s)) {
            this.data.push(s);
        }
        return;
    };
    StringBuffer.prototype.add_line = function (s) {
        if (this.populated(s)) {
            this.data.push(s);
            this.data.push(os.EOL);
        }
        return;
    };
    StringBuffer.prototype.addLine = function (s) {
        return this.add_line(s);
    };
    StringBuffer.prototype.newline = function () {
        this.data.push(os.EOL);
    };
    StringBuffer.prototype.newLine = function () {
        this.newline();
    };
    StringBuffer.prototype.to_string = function (trim) {
        if (trim) {
            return this.data.join('').trim();
        }
        else {
            return this.data.join('');
        }
    };
    StringBuffer.prototype.toString = function (trim) {
        return this.to_string(trim);
    };
    StringBuffer.prototype.as_lines = function () {
        return this.to_string().split(os.EOL);
    };
    StringBuffer.prototype.asLines = function () {
        return this.as_lines();
    };
    StringBuffer.prototype.populated = function (s) {
        if (s === undefined) {
            return false;
        }
        if (s === null) {
            return false;
        }
        return true;
    };
    StringBuffer.VERSION = '0.3.0';
    return StringBuffer;
})();
exports.StringBuffer = StringBuffer;
