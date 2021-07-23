
import pytest

import m26


def assert_almost_equal(x, y, threshold=0.0001):
    assert(abs(x - y) < threshold)

def test_constructor_with_number():
    t = m26.ElapsedTime(3665)
    assert_almost_equal(t.hh, 1.0000)
    assert_almost_equal(t.mm, 1.0000)
    assert_almost_equal(t.ss, 5.0000)
    assert_almost_equal(t.secs, 3665.0000)
    assert_almost_equal(t.hours(), 1.0180555555555555)
    assert(t.as_hhmmss() == '01:01:05')

def test_constructor_with_hhmmss_string():
    t = m26.ElapsedTime('3:47:30')
    assert_almost_equal(t.hh, 3.0000)
    assert_almost_equal(t.mm, 47.0000)
    assert_almost_equal(t.ss, 30.0000)
    assert_almost_equal(t.secs, 13650.0000)
    assert_almost_equal(t.hours(), 3.7916666666666665)
    assert(t.as_hhmmss() == '03:47:30')

def test_constructor_with_mmss_string():
    t = m26.ElapsedTime('30:0')
    assert_almost_equal(t.hh,  0.0000)
    assert_almost_equal(t.mm, 30.0000)
    assert_almost_equal(t.ss,  0.0000)
    assert_almost_equal(t.secs, 1800.0000)
    assert_almost_equal(t.hours(), 0.500)
    assert(t.as_hhmmss() == '00:30:00')

def test_constructor_with_ss_string():
    t = m26.ElapsedTime('10')
    assert_almost_equal(t.hh, 0.0000)
    assert_almost_equal(t.mm, 0.0000)
    assert_almost_equal(t.ss, 10.0000)
    assert_almost_equal(t.secs, 10.0000)
    assert_almost_equal(t.hours(), 0.002777777777777778)
    assert(t.as_hhmmss() == '00:00:10')

def test_constructor_with_empty_string():
    t = m26.ElapsedTime('')
    assert_almost_equal(t.hh, 0.0000)
    assert_almost_equal(t.mm, 0.0000)
    assert_almost_equal(t.ss, 00.0000)
    assert_almost_equal(t.secs, 00.0000)
    assert_almost_equal(t.hours(), 0.0)
    assert(t.as_hhmmss() == '00:00:00')

def test_constructor_with_malformed_string():
    t = m26.ElapsedTime('3:xx:q')
    assert_almost_equal(t.hh, 3.0000)
    assert_almost_equal(t.mm, 0.0000)
    assert_almost_equal(t.ss, 0.0000)
    assert_almost_equal(t.secs, 10800.0000)
    assert_almost_equal(t.hours(), 3.000)
    assert(t.as_hhmmss() == '03:00:00')
