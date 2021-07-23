import * as fs from "fs";

export class Merge {

    // NOT included in tsFiles are: main.ts, merge.ts, and file_util.ts
    // tsFiles is in logical sequence of top (imports) then most granular
    // and standalone to larger and aggregated.

    private tsFiles : string[] = [
        "src/top.ts",
        "src/ts.ts",
        "src/etime.ts",
        "src/geo.ts",
        "src/trackpoint.ts",
        "src/author.ts",
        "src/creator.ts",
        "src/activity.ts",
        "src/parser.ts"
    ];
    private mergedLines : string[] = new Array<string>();
    private outfile : string = "";

    public constructor() {

    }

    public execute() : void {
        if (process.argv.length < 3) {
            console.log('Invalid program args');
            console.log('node dist/merge.js <outfile>');
            console.log('');
        }
        else {
            this.outfile = process.argv[2];
            //console.log('outfile: ' + this.outfile);

            for (var i = 0; i < this.tsFiles.length; i++) {
                var infile = this.tsFiles[i];
                console.log("merging file: " + infile);
                let filteredLines = this.readLines(infile);
                //console.log("read file: " + infile + ",  lines: " + filteredLines.length);

                for (var l = 0; l < filteredLines.length; l++) {
                    this.mergedLines.push(filteredLines[l]);
                }
            }

            fs.writeFileSync(this.outfile, this.mergedLines.join("\n"));
            console.log("file written: " + this.outfile + ", lines: " + this.mergedLines.length);
        }
    }

    private readLines(infile: string) : string[] {
        let filteredLines = new Array<string>();
        let allLines = fs.readFileSync(infile).toString().split("\n");
        let inZone = false;
        for (var i = 0; i < allLines.length; i++) {
            let line = allLines[i];
            if (inZone) {
                filteredLines.push(line);
            }
            if (line === "//=") {
                inZone = true;
            }
        }
        return filteredLines;
    }
}

new Merge().execute();
