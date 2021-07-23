import { JsonValue } from "./tcx";
import { JsonArray } from "./tcx";
import { JsonObject } from "./tcx";
import { GeoJsonLocation } from "./geo";
import { ElapsedTime } from "./etime";
import { Timestamp } from "./ts";

//=

// Instances of this class represent one of the many Trackpoints in a Garmin TCX Activity.

export class Trackpoint {

    public static get DEFAULT_EPOCH_TIMESTAMP_STRING(): string  { return "1970-01-01T00:00:00.000Z"; }
    public static get MILES_PER_KILOMETER(): number  { return 0.621371192237334; }
    public static get YARDS_PER_MILE():   number  { return 1760.0; }
    public static get FEET_PER_METER(): number  { return 3.280839895013123; }

    public doctype:         string = 'trackpoint';
    public time:            string | null = null;
    public seq:             number | null = null;
    public latitude:        number | null = 0; 
    public longitude:       number | null = 0;
    public altitude_meters: number | null = null;
    public altitude_feet:   number | null = null;
    public distance_meters: number | null = 0;
    public distance_miles:  number | null = null;
    public distance_km:     number | null = null;
    public distance_yds:    number | null = null;
    public heart_rate_bpm:  number | null = null;
    public speed:           number | null = null;
    public cadence:         number | null = null;  // either running or cycling
    public watts:           number | null = null; 
    public location:        GeoJsonLocation | null = null;
    public elapsed_sec:     number | null = null;
    public elapsed_hhmmss:  string | null = null;
    public epoch_ms: number = -1;

    public constructor(raw_obj : JsonObject, sequence : number) {
        this.seq = sequence;
        this.epoch_ms = -1;
        let keys : string[] = Object.keys(raw_obj);

        if (keys.includes("Time")) {
            this.time = <string> raw_obj["Time"];
        }
        else {
            this.time = Trackpoint.DEFAULT_EPOCH_TIMESTAMP_STRING;
        }

        try {
            let ts = new Timestamp(this.time);
            this.epoch_ms = ts.epochMilliseconds;
        }
        catch(e) {
            console.log(e);
        }

        if (keys.includes("Position")) {
            try {
                let position : JsonObject = <JsonObject> raw_obj["Position"];
                this.latitude  = Number(position["LatitudeDegrees"]);
                this.longitude = Number(position["LongitudeDegrees"]);
            }
            catch(e) {
                console.log(e);
            }
        }
        if (keys.includes("AltitudeMeters")) {
            this.altitude_meters = Number(raw_obj["AltitudeMeters"]);
        }
        if (keys.includes("DistanceMeters")) {
            this.distance_meters = Number(raw_obj["DistanceMeters"]);
        }
        if (keys.includes("HeartRateBpm")) {
            try {
                let hr : JsonObject = <JsonObject> raw_obj["HeartRateBpm"];
                this.heart_rate_bpm = Number(hr["Value"]);
            }
            catch(e) {
                console.log(e);
            }
        }
        if (keys.includes("Cadence")) {
            this.cadence = Number(raw_obj["Cadence"]);
        }
        if (keys.includes("Extensions")) {
            try {
                let ext : JsonObject = <JsonObject> raw_obj["Extensions"];
                let ext_keys : string[] = Object.keys(ext);
                if (ext_keys.includes("TPX")) {
                    let tpx = <JsonObject> ext["TPX"];
                    let tpx_keys : string[] = Object.keys(tpx);
                    if (tpx_keys.includes("Speed")) {
                        this.speed = Number(tpx["Speed"]);
                    }
                    if (tpx_keys.includes("RunCadence")) {
                        this.cadence = Number(tpx["RunCadence"]);
                    }
                    if (tpx_keys.includes("Watts")) {
                        this.watts = Number(tpx["Watts"]);
                    }
                }
            }
            catch(e) {
                console.log(e);
            }
        }
    }

    public addAltitudeFeet() : void {
        if (this.altitude_meters) {
            try {
                this.altitude_meters = Number(this.altitude_meters);
                this.altitude_feet = this.altitude_meters * Trackpoint.FEET_PER_METER;
            }
            catch(e) {
                console.log(e);
            }
        }
    }

    public addDistances() : void {
        if (this.distance_meters !== null) {
            try {
                this.distance_km    = this.distance_meters / 1000.0;
                this.distance_miles = this.distance_km * Trackpoint.MILES_PER_KILOMETER;
                this.distance_yds   = this.distance_miles * Trackpoint.YARDS_PER_MILE;
            }
            catch(e) {
                console.log(e);
            }
        }
    }

    public calculateElapsed(startingEpoch: number) : void {
        let elapsedMs = this.epoch_ms - startingEpoch;
        let et : ElapsedTime = new ElapsedTime(elapsedMs);
        this.elapsed_sec = et.secs;
        this.elapsed_hhmmss = et.asHHMMSS();
    }

    public addGeoJson() : void {
        try {
            let lat = <number> this.latitude;
            let lng = <number> this.longitude;
            this.location = new GeoJsonLocation(lat, lng);
        }
        catch(e) {
            console.log(e);
        }
    }

    public cleanup() : void {

    }
}
