
import pytest

import ggps


def expected_tcm_first_trackpoint():
    return {
        "altitudefeet": "850.3937408367167",
        "altitudemeters": "259.20001220703125",
        "distancekilometers": "0.0",
        "distancemeters": "0.0",
        "distancemiles": "0.0",
        "elapsedtime": "00:00:00",
        "heartratebpm": "85",
        "latitudedegrees": "44.97431952506304",
        "longitudedegrees": "-93.26310088858008",
        "cadence": "89",
        "cadencex2": "178",
        "seq": "1",
        "speed": "0.0",
        "time": "2014-10-05T13:07:53.000Z",
        "type": "Trackpoint"
    }

def expected_tcm_middle_trackpoint():
    return {
        "altitudefeet": "805.7742982398804",
        "altitudemeters": "245.60000610351562",
        "distancekilometers": "32.187189453125",
        "distancemeters": "32187.189453125",
        "distancemiles": "20.00019228525722",
        "elapsedtime": "03:13:19",
        "heartratebpm": "140",
        "latitudedegrees": "44.959017438814044",
        "longitudedegrees": "-93.21290854364634",
        "cadence": "84",
        "cadencex2": "168",
        "seq": "1747",
        "speed": "2.8269999027252193",
        "time": "2014-10-05T16:21:12.000Z",
        "type": "Trackpoint"
    }

def expected_tcm_last_trackpoint():
    return {
        "altitudefeet": "864.8294163501167",
        "altitudemeters": "263.6000061035156",
        "distancekilometers": "42.63544921875",
        "distancemeters": "42635.44921875",
        "distancemiles": "26.492439912628992",
        "elapsedtime": "04:14:24",
        "heartratebpm": "161",
        "latitudedegrees": "44.95180849917233",
        "longitudedegrees": "-93.10493202880025",
        "cadence": "77",
        "cadencex2": "154",
        "seq": "2256",
        "speed": "3.5460000038146977",
        "time": "2014-10-05T17:22:17.000Z",
        "type": "Trackpoint"
    }

def test_twin_cities_marathon_tcx_file():
    filename = 'data/twin_cities_marathon.tcx'
    handler = ggps.TcxHandler()
    handler.parse(filename)

    tkpts = handler.trackpoints
    expected_tcm_attr_count = 15

    assert(handler.curr_depth() == 0)
    assert(handler.curr_path() == '')

    # check the number of trackpoints
    actual = len(tkpts)
    expected = 2256
    assert(actual == expected)
    actual = handler.trackpoint_count()
    assert(actual == expected)

    # check the first trackpoint
    expected_tkpt = expected_tcm_first_trackpoint()
    expected_keys = sorted(expected_tkpt.keys())
    actual_tkpt   = handler.trackpoints[0]
    actual_keys   = sorted(actual_tkpt.values.keys())
    assert(expected_keys == actual_keys)

    assert(len(actual_tkpt.values) == expected_tcm_attr_count)
    for key in expected_tkpt.keys():
        expected, actual = expected_tkpt[key], actual_tkpt.values[key]
        assert(expected == actual)

    # check a trackpoint at ~mile 20
    expected_tcm_tkpt = expected_tcm_middle_trackpoint()
    actual_tkpt = handler.trackpoints[1746]
    assert(len(actual_tkpt.values) == expected_tcm_attr_count)
    for key in expected_tcm_tkpt.keys():
        expected, actual = expected_tcm_tkpt[key], actual_tkpt.values[key]
        assert(expected == actual)

    # check the last trackpoint
    expected_tcm_tkpt = expected_tcm_last_trackpoint()
    actual_tkpt = handler.trackpoints[-1]
    assert(len(actual_tkpt.values) == expected_tcm_attr_count)
    for key in expected_tcm_tkpt.keys():
        expected, actual = expected_tcm_tkpt[key], actual_tkpt.values[key]
        assert(expected == actual)

    # check seconds_to_midnight
    secs = int(handler.first_time_secs_to_midnight)
    assert(secs > 0)
    assert(secs < 86400)

def test_dc_trails_20200217_tcx_file():
    filename = 'data/activity_4564516081.tcx'
    handler = ggps.TcxHandler()
    handler.parse(filename)
    tkpts = handler.trackpoints

    # check the number of trackpoints
    actual = len(tkpts)
    expected = 2209
    assert(actual == expected)

