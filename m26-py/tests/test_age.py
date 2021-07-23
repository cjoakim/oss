
import json
import pytest

import m26


def write_tmp_file(basename, contents):
    with open('tmp/' + basename, 'w', encoding='utf-8') as out:
        out.write(contents)
        print('tmp/ file written: ' + basename)

def test_constructor():
    assert(m26.Age().value == 0)
    assert(m26.Age().value == 0)
    assert(m26.Age(58.1).value == 58.1)
    assert(m26.Age('58.2').value == 58.2)

def test_max_pulse():
    assert(m26.Age(16).max_pulse() == 200.0)
    assert(m26.Age(20).max_pulse() == 200.0)
    assert(m26.Age(21).max_pulse() == 199.0)
    assert(m26.Age(58.1).max_pulse() == 161.9)

def test_add():
    a16 = m26.Age(16.0)
    a58 = m26.Age(58.0)
    assert(a58.add(a16) == 74.0)
    assert(a58.value == 74.0)

def test_subtract():
    a16 = m26.Age(16.0)
    a58 = m26.Age(58.0)
    assert(a58.subtract(a16) == 42.0)
    assert(a58.value == 42.0)

def test_training_zones():
    a58 = m26.Age(58.0)
    zones = a58.training_zones()
    write_tmp_file('training_zones.json', json.dumps(zones, indent=True))
    assert(len(zones) == 5)
    z0 = zones[0]
    z4 = zones[4]

    assert(z0['pct_max'] == 0.95)
    assert(z0['pulse']   == 153.9)

    assert(z4['pct_max'] == 0.75)
    assert(z4['pulse']   == 121.5)

def test_str():
    a = m26.Age(58.0)
    assert(str(a) == '<Age value:58.0>')
