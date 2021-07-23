
import json

import m26

if __name__ == "__main__":

    d1 = m26.Distance(26.2)
    print(d1)
    print("d1, as_miles:      {0}".format(d1.as_miles()))
    print("d1, as_kilometers: {0}".format(d1.as_kilometers()))
    print("d1, as_yards:      {0}".format(d1.as_yards()))

    print('')
    d2 = m26.Distance(50.0, m26.Constants.uom_kilometers())
    print(d2)

    print('')
    d3 = m26.Distance(7040, m26.Constants.uom_yards())
    print(d3)

    print('')
    d4 = m26.Distance(10.0, m26.Constants.uom_kilometers())
    print(d4)

    print('')
    d4.add(d1)
    print(d4)

    print('')
    d4.subtract(d3)
    print(d4)

    print('')
    t1 = m26.ElapsedTime('3:47:30')
    print(t1)
    print("t1 hours: {0}".format(t1.hours()))

    print('')
    t2 = m26.ElapsedTime(3662)
    print(t2)
    print("t2 hours: {0}".format(t2.hours()))

    print('')
    s = m26.Speed(d1, t1)
    print(s)
    print("s, mph: {0}".format(s.mph()))
    print("s, kph: {0}".format(s.kph()))
    print("s, yph: {0}".format(s.yph()))
    print("s, spm: {0}".format(s.seconds_per_mile()))
    print("s, ppm: {0}".format(s.pace_per_mile()))

    hhmmss_simple = s.projected_time(d2, 'simple')
    hhmmss_riegel = s.projected_time(d2, 'riegel')
    print("projected_time, simple: {0}".format(hhmmss_simple))
    print("projected_time, riegel: {0}".format(hhmmss_riegel))

    print('')
    result = m26.RunWalkCalculator.calculate('2:30', '9:16', '0:45', '17:00', 31.0)
    print(json.dumps(result, sort_keys=True, indent=2))

    print('')
    a = m26.AgeCalculator.calculate('1960-10-01', '2015-10-18')
    print(a)

    print('')
    a2 = m26.Age(58.1)
    graded = s.age_graded(a, a2)
    print(graded)

    zones = a2.training_zones()
    print(json.dumps(zones, sort_keys=True, indent=2))
    print('')