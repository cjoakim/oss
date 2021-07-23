import { JsonValue } from "./tcx";
import { JsonArray } from "./tcx";
import { JsonObject } from "./tcx";

//=

export class Author {

    public type:          string = 'Author';
    public name:          string = '';
    public part_number:   string = '';
    public lang:          string = '';
    public build_major:   string = '';
    public build_minor:   string = '';
    public version_major: string = '';
    public version_minor: string = '';

    public constructor(raw_obj: JsonObject | null) {

        if (raw_obj !== null) {
            this.name = <string> raw_obj["Name"];
            this.lang = <string> raw_obj["LangID"];
            this.part_number = <string> raw_obj["PartNumber"];
    
            let build : JsonObject = <JsonObject> raw_obj["Build"];
            let vers  : JsonObject = <JsonObject> build["Version"];
            this.version_major = <string> vers["VersionMajor"];
            this.version_minor = <string> vers["VersionMinor"];
            this.build_major   = <string> vers["BuildMajor"];
            this.build_minor   = <string> vers["BuildMinor"];
        }
    }
}
