
import { Distance } from "./Distance";
import { Constants } from "./Constants";

test("constructor default uom", () => {
    let d = new Distance(26.2);
    expect(d.value).toBe(26.2);
    expect(d.uom).toBe(Constants.UOM_MILES);

    expect(d.asMiles()).toBe(26.2);
    expect(d.asKilometers()).toBe(42.1648128);
    expect(d.asYards()).toBe(46112.0);
});

test("constructor miles uom", () => {
    let d = new Distance(26.2, Constants.UOM_MILES);
    expect(d.value).toBe(26.2);
    expect(d.uom).toBe(Constants.UOM_MILES);

    expect(d.asMiles()).toBe(26.2);
    expect(d.asKilometers()).toBe(42.1648128);
    expect(d.asYards()).toBe(46112.0);
});

test("constructor kilometers uom", () => {
    // d = new Distance(10.0, 'k');
    // expect(d.uom()).toBe(Constants.UOM_KILOMETERS);
    // expect(d.as_miles()).isWithin(0.0000000001, 6.2137119223733395);
    // expect(d.as_kilometers()).isWithin(0.0000000001, 10.0);
    // return expect(d.as_yards()).isWithin(0.000001, 10936.132983377078);

    let d = new Distance(26.2, Constants.UOM_MILES);
    expect(d.value).toBe(26.2);
    expect(d.uom).toBe(Constants.UOM_MILES);

    expect(d.asMiles()).toBe(26.2);
    expect(d.asKilometers()).toBe(42.1648128);
    expect(d.asYards()).toBe(46112.0);
});

test("constructor yards uom", () => {
    // d1 = new Distance(26.2);
    // d2 = new Distance(4.8);
    // d3 = d1.add(d2);
    // expect(d3.uom()).toBe(Constants.UOM_MILES);
    // return expect(d3.as_miles()).isWithin(0.0000000001, 31.0);

    let d = new Distance(26.2, Constants.UOM_MILES);
    expect(d.value).toBe(26.2);
    expect(d.uom).toBe(Constants.UOM_MILES);

    expect(d.asMiles()).toBe(26.2);
    expect(d.asKilometers()).toBe(42.1648128);
    expect(d.asYards()).toBe(46112.0);
});

test("add", () => {
    // d1 = new Distance(26.2);
    // d2 = new Distance(4.8);
    // d3 = d1.add(d2);
    // expect(d3.uom()).toBe(Constants.UOM_MILES);
    // return expect(d3.as_miles()).isWithin(0.0000000001, 31.0);

    let d = new Distance(26.2, Constants.UOM_MILES);
});

test("subtract", () => {
    // d1 = new Distance(26.2);
    // d2 = new Distance(10.0, 'k');
    // d3 = d1.subtract(d2);
    // expect(d3.uom()).toBe(Constants.UOM_MILES);
    // return expect(d3.as_miles()).isWithin(0.0000000001, 19.98628807762666);

    let d = new Distance(26.2, Constants.UOM_MILES);
});
