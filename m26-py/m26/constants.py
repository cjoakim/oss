__author__ = 'cjoakim'


class Constants(object):

    @classmethod
    def uom_miles(cls):
        return 'm'

    @classmethod
    def uom_kilometers(cls):
        return 'k'

    @classmethod
    def uom_yards(cls):
        return 'y'

    @classmethod
    def units_of_measure(cls):
        return ('m', 'k', 'y')

    @classmethod
    def kilometers_per_mile(cls):
        return float(1.609344)

    @classmethod
    def miles_per_kilometer(cls):
        return float(0.621371192237334)

    @classmethod
    def yards_per_kilometer(cls):
        return float(1093.6132983377076)

    @classmethod
    def feet_per_kilometer(cls):
        return float(3280.839895013123)

    @classmethod
    def feet_per_meter(cls):
        return float(3.280839895013123)

    @classmethod
    def yards_per_mile(cls):
        return float(1760.0)

    @classmethod
    def seconds_per_hour(cls):
        return float(3600.0)

    @classmethod
    def miles_per_marathon(cls):
        return float(26.2)
