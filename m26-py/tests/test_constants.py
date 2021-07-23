
import pytest

import m26


def test_uom_miles():
    assert(m26.Constants.uom_miles() == 'm')

def test_uom_kilometers():
    assert(m26.Constants.uom_kilometers() == 'k')

def test_uom_yards():
    assert(m26.Constants.uom_yards()== 'y')

def test_units_of_measure():
    expected = ('m', 'k', 'y')
    assert(m26.Constants.units_of_measure()== expected)

def test_kilometers_per_mile():
    assert(m26.Constants.kilometers_per_mile() == 1.609344)

def test_miles_per_kilometer():
    assert(m26.Constants.miles_per_kilometer() == 0.621371192237334)

def test_yards_per_kilometer():
    assert(m26.Constants.yards_per_kilometer() == 1093.6132983377076)

def test_feet_per_kilometer():
    assert(m26.Constants.feet_per_kilometer() == 3280.839895013123)

def test_feet_per_meter():
    assert(m26.Constants.feet_per_meter() == 3.280839895013123)

def test_yards_per_mile():
    assert(m26.Constants.yards_per_mile() == 1760.0)

def test_seconds_per_hour():
    assert(m26.Constants.seconds_per_hour() == 3600.0)

def test_miles_per_marathon():
    v = m26.Constants.miles_per_marathon()
    assert(v == 26.2)
