import { JsonValue } from "./tcx";
import { JsonArray } from "./tcx";
import { JsonObject } from "./tcx";

//=

export class Creator {

    public type:          string = 'Creator';
    public name:          string = '';
    public product_id:    string = '';
    public unit_id:       string = '';
    public build_major:   string = '';
    public build_minor:   string = '';
    public version_major: string = '';
    public version_minor: string = '';

    public constructor(raw_obj: JsonObject | null) {

        if (raw_obj !== null) {
            this.name    = <string> raw_obj["Name"];
            this.unit_id = <string> raw_obj["UnitId"];
            this.product_id = <string> raw_obj["ProductID"];
    
            let vers : JsonObject = <JsonObject> raw_obj["Version"];
            this.version_major = <string> vers["VersionMajor"];
            this.version_minor = <string> vers["VersionMinor"];
            this.build_major   = <string> vers["BuildMajor"];
            this.build_minor   = <string> vers["BuildMinor"];
        }
    }

}
