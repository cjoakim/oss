
import pytest

import m26


def assert_almost_equal(x, y, threshold=0.0001):
    assert(abs(x - y) < threshold)

def test_constructor_miles():
    d = m26.Distance()
    assert(d.value == 0)
    assert(d.uom  == 'm')

    d = m26.Distance(26.2)
    assert(d.value == 26.2)
    assert(d.uom  == 'm')

    assert(d.is_miles())
    assert(d.is_kilometers() == False)
    assert(d.is_yards() == False)

    assert_almost_equal(d.as_miles(),      26.2)
    assert_almost_equal(d.as_kilometers(), 42.1648128)
    assert_almost_equal(d.as_yards(),      46112.0)

def test_constructor_kilometers():
    d = m26.Distance(50.0, 'k')
    assert(d.value == 50.0)
    assert(d.uom  == 'k')

    d = m26.Distance(10, ' K ')
    assert(d.value == 10.0)
    assert(d.uom  == 'k')

    assert(d.is_miles() == False)
    assert(d.is_kilometers())
    assert(d.is_yards() == False)

    assert_almost_equal(d.as_miles(),      6.2137119223733395)
    assert_almost_equal(d.as_kilometers(), 10.000000)
    assert_almost_equal(d.as_yards(),      10936.132983377078)

def test_constructor_yards():
    d = m26.Distance(3600.0, 'y')
    assert(d.value == 3600.0)
    assert(d.uom == 'y')

    d = m26.Distance(1800.0, ' Y ')
    assert(d.value == 1800.0)
    assert(d.uom == 'y')

    assert(d.is_miles() == False)
    assert(d.is_kilometers() == False)
    assert(d.is_yards())

    assert_almost_equal(d.as_miles(),      1.0227272727272727)
    assert_almost_equal(d.as_kilometers(), 1.64592)
    assert_almost_equal(d.as_yards(),      1800.000000)

def test_add_to_miles():
    d1 = m26.Distance(26.2, 'm')
    d2 = m26.Distance(4.8, 'm')
    d3 = m26.Distance(5.0, 'k')
    d4 = m26.Distance(1800, 'y')

    d1.add(d2)
    assert_almost_equal(d1.value, 31.0)
    assert(d1.uom == 'm')

    d1.add(d3)
    assert_almost_equal(d1.value, 34.10685596118667)

    d1.add(d4)
    assert_almost_equal(d1.value, 35.12958323391394)
    assert(d1.uom == 'm')

def test_add_to_kilometers():
    d1 = m26.Distance(10.0, 'k')
    d2 = m26.Distance(3.1, 'm')

    d1.add(d2)
    assert(d1.uom == 'k')
    assert_almost_equal(d1.value, 14.9889664)

def test_add_to_yards():
    d1 = m26.Distance(1800, 'y')
    d2 = m26.Distance(1.0, 'm')

    d1.add(d2)
    assert(d1.uom == 'y')
    assert_almost_equal(d1.value, 3560.0)

def test_subtract_from_miles():
    d1 = m26.Distance(26.2, 'm')
    d2 = m26.Distance(4.8, 'm')
    d3 = m26.Distance(5.0, 'k')
    d4 = m26.Distance(1800, 'y')

    d1.subtract(d2)
    assert_almost_equal(d1.value, 21.4)
    assert(d1.uom == 'm')

    d1.subtract(d3)
    assert_almost_equal(d1.value, 18.293144038813328)

    d1.subtract(d4)
    assert_almost_equal(d1.value, 17.270416766086054)
    assert(d1.uom == 'm')

def test_subtract_from_kilometers():
    d1 = m26.Distance(10.0, 'k')
    d2 = m26.Distance(3.1, 'm')

    d1.subtract(d2)
    assert(d1.uom == 'k')
    assert_almost_equal(d1.value, 5.011033599999999)

def test_subtract_from_yards():
    d1 = m26.Distance(3600, 'y')
    d2 = m26.Distance(1.0, 'm')

    d1.subtract(d2)
    assert(d1.uom == 'y')
    assert_almost_equal(d1.value, 1840.0)
