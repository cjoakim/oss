
import pytest

import m26


def test_seconds_per_year():
    assert(m26.AgeCalculator.seconds_per_year() == 31557600.0)

def test_milliseconds_per_year():
    assert(m26.AgeCalculator.milliseconds_per_year() == 31557600000.0)

def test_calculate():
    a1 = m26.AgeCalculator.calculate('1960-10-01', '2015-10-01')
    actual = 54.997946611909654
    assert(a1.value > (actual - 0.000001))
    assert(a1.value < (actual + 0.000001))

def test_calculate_no_birthdate():
    a1 = m26.AgeCalculator.calculate(None, '2015-10-01')
    assert(a1 == None)
