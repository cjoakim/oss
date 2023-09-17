
import { Age } from "./Age";
import { Distance } from "./Distance";
import { Constants } from "./Constants";
import { ElapsedTime } from "./ElapsedTime";
import { Speed } from "./Speed";

test("calculates a 2-mile walk, with round numbers", () => {
    let d1  = new Distance(2.0);
    let et1 = new ElapsedTime('30:00');
    let s1  = new Speed(d1, et1);
    expect(s1.secondsPerMile()).toBe(900);
    expect(s1.pacePerMile()).toBe('15:00');
});

test("calculates a marathon", () => {
    let d1  = new Distance(26.2);
    let et1 = new ElapsedTime('3:47:30');
    let s1  = new Speed(d1, et1);
    expect(s1.secondsPerMile()).toBe(520.9923664122138);
    expect(s1.pacePerMile()).toBe('8:40.99');
});

// it('calculates a marathon, with fractional pace_per_mile', function() {
//     var d, s, t;
//     d = new Distance(26.2);
//     t = new ElapsedTime('03:47:30');
//     s = new Speed(d, t);
//     expect(s.mph()).isWithin(0.000001, 6.90989010989011);
//     expect(s.kph()).isWithin(0.000001, 11.120390189010989);
//     expect(s.yph()).isWithin(0.000001, 12161.4065934066);
//     expect(s.seconds_per_mile()).isWithin(0.000001, 520.992366412214);
//     return expect(s.pace_per_mile()).toBe('8:40.99');
//   });


