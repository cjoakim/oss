
// Copyright 2015, Christopher Joakim <christopher.joakim@gmail.com>

/// <reference path="../typedefs/node.d.ts" />

import os = require('os');


export class CounterHash {

    // class variables
    static VERSION : string = '0.2.0';

    // instance variables
    values : Object = {};

    constructor() {

    }

    value(key : string) : number {

        var n = this.values[key];
        if (this.populated(n)) {
            return n;
        }
        else {
          return 0;
        }
    }

    sum() : number {

      var sum = 0;
      var keys = Object.getOwnPropertyNames(this.values);
      for (var i = 0; i < keys.length; i++) {
        var key = keys[i];
        var val = this.value(key);
        sum = sum + val;
      }
      return sum;
    }

    increment(key : string) : void {

      if (this.populated(key)) {
        var val = this.value(key);
        this.values[key] = val + 1;
      }
    }

    decrement(key : string) : void {

      if (this.populated(key)) {
        var val = this.value(key);
        this.values[key] = val - 1;
      }
    }

    add(key : string, n : number) : void {

      if (this.populated(key)) {
        if (this.populated(n)) {
          var val = this.value(key);
          this.values[key] = val + n;
        }
      }
    }

    subtract(key : string, n : number) : void {

      if (this.populated(key)) {
        if (this.populated(n)) {
          var val = this.value(key);
          this.values[key] = val - n;
        }
      }
    }

    sorted_keys() : string[] {

      var keys = Object.getOwnPropertyNames(this.values);
      return keys.sort();
    }

    sorted_tuples() : Object[] {

      var array = [];
      var keys = Object.getOwnPropertyNames(this.values);
      for (var i = 0; i < keys.length; i++) {
        var key = keys[i];
        var val = this.value(key);
        array.push([key, val]);
      }
      return array.sort();
    }

    private populated(s : any) {

        if (s === undefined) {
            return false;
        }
        if (s === null) {
            return false;
        }
        return true;
    }
}
