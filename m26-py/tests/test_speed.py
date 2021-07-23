
import pytest

import m26


def assert_almost_equal(x, y, threshold=0.0001):
    assert(abs(x - y) < threshold)

def test_a_walk_with_round_numbers():
    d = m26.Distance(2.0)
    t = m26.ElapsedTime('30:00')
    s = m26.Speed(d, t)
    assert_almost_equal(s.mph(), 4.0000)
    assert_almost_equal(s.kph(), 6.437376)
    assert_almost_equal(s.yph(), 7040.0000)
    assert_almost_equal(s.seconds_per_mile(), 900.0)
    assert(s.pace_per_mile() == '15:00.0')
    assert(str(s) == '<Speed dist:<Distance value:2.0 uom:m> etime:<ElapsedTime hh:0 mm:30.0 ss:0.0 secs:1800.0>>')

def test_a_marathon_with_fractional_numbers():
    d = m26.Distance(26.2)
    t = m26.ElapsedTime('3:47:30')
    s = m26.Speed(d, t)
    ppm = s.pace_per_mile()

    assert_almost_equal(s.mph(), 6.90989010989011)
    assert_almost_equal(s.kph(), 11.120390189010989)
    assert_almost_equal(s.yph(), 12161.4065934066)
    assert_almost_equal(s.seconds_per_mile(), 520.992366412214)
    assert(ppm == '8:40.99')

def test_project_time_with_linear_formula():
    d = m26.Distance(10.0)
    t = m26.ElapsedTime('1:30:0')
    s = m26.Speed(d, t)
    spm = s.seconds_per_mile()
    ppm = s.pace_per_mile()
    assert_almost_equal(spm, 540.0)
    assert(ppm == '9:00.0')

    d2 = m26.Distance(20.0)
    hhmmss = s.projected_time(d2)
    assert(hhmmss == '03:00:00')

def test_project_time_with_exponential_formula():
    d = m26.Distance(10.0)
    t = m26.ElapsedTime('1:30:0')
    s = m26.Speed(d, t)
    spm = s.seconds_per_mile()
    ppm = s.pace_per_mile()
    assert_almost_equal(spm, 540.0)
    assert(ppm == '9:00.0')

    d2 = m26.Distance(20.0)
    hhmmss = s.projected_time(d2, 'riegel')
    assert(hhmmss == '03:07:38')

def test_age_graded_time():
    d = m26.Distance(26.2)
    t = m26.ElapsedTime('3:47:30')
    s1 = m26.Speed(d, t)
    a1 = m26.Age(42.5)
    a2 = m26.Age(43.5)
    a3 = m26.Age(57.1)
    s2 = s1.age_graded(a1, a2)
    s3 = s1.age_graded(a1, a3)

    assert_almost_equal(s1.mph(), 6.90989010989011)
    assert_almost_equal(s2.mph(), 6.870961151524531)
    assert_almost_equal(s3.mph(), 6.341527317752669)
