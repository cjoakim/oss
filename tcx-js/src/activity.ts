import { Author } from "./author";
import { Creator } from "./creator";
import { Trackpoint } from "./trackpoint";
import { ElapsedTime } from "./etime";
import { Timestamp }   from "./ts";

//=

// Instances of this class represent the aggregated data from one TCX file,
// and its Activity XML tag.

export class Activity {

    public tcx_filename : string = "";
    public activityId: string = "";
    public sport: string = "";
    public author: Author;
    public creator: Creator;
    public trackpoints: Trackpoint[] = new Array<Trackpoint>();
    public firstTrackpoint : Trackpoint | null = new Trackpoint({}, 0);
    public startingEpoch : number = 0;
    public parsedDate : string = new Date().toISOString();

    public constructor() {
        this.sport   = "";
        this.author  = new Author(null);
        this.creator = new Creator(null);
    }

    public addTrackpoint(tkpt: Trackpoint) {
        this.trackpoints.push(tkpt);
        if (this.trackpoints.length === 1) {
            this.firstTrackpoint = tkpt;
            this.startingEpoch = tkpt.epoch_ms;
        }
    }

}
