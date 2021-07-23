__author__ = 'cjoakim'

import math

from .elapsed_time import ElapsedTime


class Speed(object):

    def __init__(self, d, et):
        self.dist = d    # an instance of Distance
        self.etime = et  # an instance of ElapsedTime

    def mph(self):
        return self.dist.as_miles() / self.etime.hours()

    def kph(self):
        return self.dist.as_kilometers() / self.etime.hours()

    def yph(self):
        return self.dist.as_yards() / self.etime.hours()

    def pace_per_mile(self):
        spm = self.seconds_per_mile()
        mm = math.floor(spm / 60.0)
        ss = spm - (mm * 60.0)

        if ss < 10:
            ss = "0{0}".format(ss)
        else:
            ss = "{0}".format(ss)

        if len(ss) > 5:
            ss = ss[0:5]

        return "{0}:{1}".format(mm, ss)

    def seconds_per_mile(self):
        return float(self.etime.secs / self.dist.as_miles())

    def projected_time(self, another_distance, algorithm='simple'):
        if algorithm is 'riegel':
            t1 = float(self.etime.secs)
            d1 = self.dist.as_miles()
            d2 = another_distance.as_miles()
            t2 = t1 * math.pow(float(d2 / d1), float(1.06))
            et = ElapsedTime(t2)
            return et.as_hhmmss()
        else:
            secs = float(self.seconds_per_mile() * another_distance.as_miles())
            et = ElapsedTime(secs)
            return et.as_hhmmss()

    def age_graded(self, event_age, graded_age):
        ag_factor = event_age.max_pulse() / graded_age.max_pulse()
        graded_secs = float((self.etime.secs)) * float(ag_factor)
        graded_et = ElapsedTime(graded_secs)
        return Speed(self.dist, graded_et)

    def __str__(self):
        template = "<Speed dist:{0} etime:{1}>"
        return template.format(self.dist, self.etime)
