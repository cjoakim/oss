//=

// This class is used to create a human-readable HH:MM:SS elapsed time string
// from an elapsed time value in milliseconds.

export class ElapsedTime {

    public static get MILLISECONDS_PER_SECOND(): number  { return 1000.0; }
    public static get SECONDS_PER_HOUR():   number  { return 3600.0; }
    public static get SECONDS_PER_MINUTE(): number  { return 60.0; }

    public elapsedMs: number;
    public secs: number = 0;
    public hh: number = 0;
    public mm: number = 0;
    public ss: number = 0;

    public constructor(elapsedMs: number) {
        this.elapsedMs = Math.abs(elapsedMs);
        this.secs = Math.round(this.elapsedMs / ElapsedTime.MILLISECONDS_PER_SECOND);

        this.hh = Math.floor(this.secs / ElapsedTime.SECONDS_PER_HOUR);
        let rem = this.secs - (this.hh * ElapsedTime.SECONDS_PER_HOUR);
        this.mm = Math.floor(rem / 60.0);
        this.ss = rem - (this.mm * 60.0)

        if (this.mm > 59) {
            console.log("ElapsedTime mm normalized to 59 - " + this.mm);
            this.mm = 59;
        }
        if (this.ss > 59) {
            console.log("ElapsedTime ss normalized to 59 - " + this.ss);
            this.ss = 59;
        }
    }

    public asHHMMSS() : string {
        return this.zeroPad(this.hh) + ":" + this.zeroPad(this.mm) + ":" + this.zeroPad(this.ss);
    }

    private zeroPad(i : number) : string {
        if (i < 10) {
            return "0" + i;
        }
        else {
            return "" + i;
        }
    }

}
