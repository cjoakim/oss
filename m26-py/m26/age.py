__author__ = 'cjoakim'


class Age(object):
    """
    Instances of this class represent the age of a person, as a float value
    of their age in years.
    """
    def __init__(self, n=0.0):
        self.value = float(n)

    def max_pulse(self):
        if self.value < 20:
            return 200.0
        else:
            return 220.0 - self.value

    def add(self, another_instance):
        if another_instance:
            self.value = self.value + another_instance.value
        return self.value

    def subtract(self, another_instance):
        if another_instance:
            self.value = self.value - another_instance.value
        return self.value

    def training_zones(self):
        results = list()
        zones = [0.95, 0.90, 0.85, 0.80, 0.75]
        for idx, pct in enumerate(zones):
            data = dict()
            data['zone'] = idx + 1
            data['age'] = self.value
            data['max'] = self.max_pulse()
            data['pct_max'] = pct
            data['pulse'] = self.max_pulse() * pct
            results.append(data)
        return results

    def __str__(self):
        return "<Age value:{0}>".format(self.value)
