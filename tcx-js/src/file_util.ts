// A wrapper around common filesystem operations because I forget how to code them.
// Chris Joakim, 2019/07/25

import * as fs from "fs";

export class FileUtil {

    public exists(infile: string) : boolean {
        return fs.existsSync(infile);
    }

    public getFilenames(path: string) : string[] {
        return fs.readdirSync(path);
    }

    public readText(infile: string) : string {
        return fs.readFileSync(infile).toString();
    }

    public readLines(infile: string) : string[] {
        return fs.readFileSync(infile).toString().split("\n");
    }

    public readParseJsonFile(infile: string) : object {
        var jstr = fs.readFileSync(infile).toString();
        return JSON.parse(jstr);
    }

    public writeFile(outfile: string, text: string) : void {
        fs.writeFileSync(outfile, text);
        console.log("file written: " + outfile);
    }

    public writeJsonObject(outfile: string, obj: object) : void {
        this.writeFile(outfile, JSON.stringify(obj, null, 2));
    }
}
