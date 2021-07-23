import * as fs from "fs";

import { Parser }     from "./tcx";
import { Activity }   from "./tcx";
import { Author }     from "./tcx";
import { Creator }    from "./tcx";
import { Trackpoint } from "./tcx";

export class Main {

    public constructor() {

    }

    public execute() : void {

        if (process.argv.length < 4) {
            console.log('Invalid program args');
            console.log('node main.js <infile> <outfile>');
            console.log('');
        }
        else {
            var infile = process.argv[2];
            var outfile = process.argv[3];
            console.log('infile:  ' + infile);
            console.log('outfile: ' + outfile);

            var parser :   Parser   = new Parser(infile);
            var activity : Activity = parser.activity;
            var creator :  Creator  = activity.creator;
            var author :   Author   = activity.author;
            var trackpoints : Trackpoint[] = activity.trackpoints;

            var jstr : string = JSON.stringify(parser.activity, (key, value) => {
                if (value !== null) {
                    return value;
                }
            }, 2);
            fs.writeFileSync(outfile, jstr);
            console.log("file written: " + outfile);
        }
    }
}

new Main().execute();
