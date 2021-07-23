//=

// Instances of this class represent a Timestamp from a string value
// like "2014-10-05T17:10:36.000Z" from a Garmin device.

export class Timestamp {

    public time_str: string;
    public date: Date = new Date();
    public epochMilliseconds : number = 0;

    public constructor(time_str: string) {
        //  time_str is a value like "2014-10-05T17:10:36.000Z" from the Garmin device
        this.time_str = time_str;

        try {
            this.date = new Date(time_str);
            this.epochMilliseconds = this.date.getTime();
        }
        catch(e) {
            console.log(e);
        }
    }

    public isValid() {
        return this.epochMilliseconds > 0;
    }

    public toString() : string {
        return "Timestamp: " + this.isValid() + ", " + this.time_str + ", " + this.date + ", " + this.epochMilliseconds;
    }

}
