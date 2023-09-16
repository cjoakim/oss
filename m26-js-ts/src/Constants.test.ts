import { Constants } from "./Constants";

test("constant values", () => {

    expect(Constants.VERSION).toBe('1.0.0');
    expect(Constants.UOM_MILES).toBe('m');
    expect(Constants.UOM_KILOMETERS).toBe('k');
    expect(Constants.UOM_YARDS).toBe('y');
    expect(Constants.UNITS_OF_MEASURE).toEqual(['m','k','y']);

    expect(Constants.KILOMETERS_PER_MILE).toBe(1.609344);
    expect(Constants.MILES_PER_KILOMETER).toBe(0.621371192237334);
    expect(Constants.YARDS_PER_KILOMETER).toBe(1093.6132983377076);
    expect(Constants.FEET_PER_KILOMETER).toBe(3280.839895013123);
    expect(Constants.FEET_PER_METER).toBe(3.280839895013123);
    expect(Constants.YARDS_PER_MILE).toBe(1760.0);
    expect(Constants.SECONDS_PER_HOUR).toBe(3600.0);
});
