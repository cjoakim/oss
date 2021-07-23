//=

export class GeoJsonLocation {

    public type:         string = 'Point';
    public coordinates:  number[];

    public constructor(latitude: number, longitude: number) {
        this.coordinates = [longitude, latitude];
    }

}
