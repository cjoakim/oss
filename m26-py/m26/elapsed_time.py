__author__ = 'cjoakim'

import math

from numbers import Number

from .constants import Constants


class ElapsedTime(object):

    def __init__(self, val):
        self.secs = 0
        self.hh = 0
        self.mm = 0
        self.ss = 0

        if not val:
            val = 0
        if isinstance(val, Number):
            self.initialize_from_number(val)
        elif isinstance(val, str):
            self.initialize_from_string(val)

    def initialize_from_number(self, val):
        sph = Constants.seconds_per_hour()
        self.secs = float(val)
        self.hh = math.floor(self.secs / sph)
        rem = self.secs - (self.hh * sph)
        self.mm = math.floor(rem / 60.0)
        self.ss = rem - (self.mm * 60.0)

    def initialize_from_string(self, val):
        stripped = str(val).strip()
        if len(stripped) > 0:
            tokens = stripped.split(':')
            if len(tokens) == 1:
                self.ss = self.to_float(tokens[0])
            elif len(tokens) == 2:
                self.mm = self.to_float(tokens[0])
                self.ss = self.to_float(tokens[1])
            elif len(tokens) == 3:
                self.hh = self.to_float(tokens[0])
                self.mm = self.to_float(tokens[1])
                self.ss = self.to_float(tokens[2])
            else:
                pass

        self.secs = (self.hh * 3600.0) + (self.mm * 60.0) + self.ss

    def to_float(self, s):
        try:
            return float(s)
        except ValueError:
            return float(0.0)

    def hours(self):
        return float(self.secs / Constants.seconds_per_hour())

    def as_hhmmss(self):
        hhs = self.zero_fill(self.hh)
        mms = self.zero_fill(self.mm)
        sss = self.zero_fill(self.ss)
        return "{0}:{1}:{2}".format(hhs, mms, sss)

    def zero_fill(self, n):
        if n < 10:
            return "0{0}".format(int(n))
        else:
            return "{0}".format(int(n))

    def __str__(self):
        template = "<ElapsedTime hh:{0} mm:{1} ss:{2} secs:{3}>"
        return template.format(self.hh, self.mm, self.ss, self.secs)
