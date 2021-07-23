
// Copyright 2015, Christopher Joakim <christopher.joakim@gmail.com>

/// <reference path="../typedefs/node.d.ts" />

import os = require('os');


export class StringBuffer {

    // class variables
    static VERSION : string = '0.3.0';

    // instance variables
    data : string[] = [];

    constructor(s : string) {

        if (this.populated(s)) {
            this.data.push(s);
        }
    }

    is_empty() : boolean {

        if (this.data.length === 0) {
            return true;
        }
        else {
            return false;
        }
    }

    isEmpty() : boolean {

        return this.is_empty();
    }

    add(s : string) : void {

        if (this.populated(s)) {
            this.data.push(s);
        }
        return;
    }

    add_line(s : string) : void {

        if (this.populated(s)) {
            this.data.push(s);
            this.data.push(os.EOL)
        }
        return;
    }

    addLine(s : string) : void {

        return this.add_line(s);
    }

    newline() : void {

        this.data.push(os.EOL)
    }

    newLine() : void {

        this.newline();
    }

    to_string(trim? : boolean) : string {

        if (trim) {
            return this.data.join('').trim()
        }
        else {
            return this.data.join('')
        }
    }

    toString(trim? : boolean) : string {

        return this.to_string(trim);
    }

    as_lines() : string[] {

        return this.to_string().split(os.EOL);
    }

    asLines() : string[] {

        return this.as_lines();
    }

    private populated(s : string) {

        if (s === undefined) {
            return false;
        }
        if (s === null) {
            return false;
        }
        return true;
    }
}
