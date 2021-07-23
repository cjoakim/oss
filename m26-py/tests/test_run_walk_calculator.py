
import json
import pytest

import m26


def assert_almost_equal(x, y, threshold=0.0001):
    assert(abs(x - y) < threshold)

def log_result(result_dict):
    print(json.dumps(result_dict, sort_keys=True, indent=2))

def test_calculate_all_walking():
    run_hhmmss = '00:00'
    run_ppm = '9:00'
    walk_hhmmss = '10:00'
    walk_ppm = '18:00'
    miles = '3.333'

    result = m26.RunWalkCalculator.calculate(run_hhmmss, run_ppm, walk_hhmmss, walk_ppm, miles)
    log_result(result)

    assert_almost_equal(result['avg_mph'], 3.33333333)
    assert_almost_equal(result['miles'], 3.333)
    assert_almost_equal(result['proj_miles'], 3.333)

    assert(result['avg_ppm'] == '18:00.0')
    assert(result['proj_time'] == '00:59:59')
    assert(result['run_hhmmss'] == '00:00')
    assert(result['run_ppm'] == '9:00')
    assert(result['walk_hhmmss'] == '10:00')
    assert(result['walk_ppm'] == '18:00')

def test_calculate_all_running():
    run_hhmmss = '10:00'
    run_ppm = '9:00'
    walk_hhmmss = '00:00'
    walk_ppm = '18:00'
    miles = '3.333'

    result = m26.RunWalkCalculator.calculate(run_hhmmss, run_ppm, walk_hhmmss, walk_ppm, miles)
    log_result(result)

    assert_almost_equal(result['avg_mph'], 6.66666666)
    assert_almost_equal(result['miles'], 3.333)
    assert_almost_equal(result['proj_miles'], 3.333)

    assert(result['avg_ppm'] == '9:00.0')
    assert(result['proj_time'] == '00:29:59')
    assert(result['run_hhmmss'] == '10:00')
    assert(result['run_ppm'] == '9:00')
    assert(result['walk_hhmmss'] == '00:00')
    assert(result['walk_ppm'] == '18:00')

def test_calculate_1_to_1_run_walk():
    run_hhmmss = '10:00'
    run_ppm = '8:00'
    walk_hhmmss = '10:00'
    walk_ppm = '16:00'
    miles = '4.0'

    result = m26.RunWalkCalculator.calculate(run_hhmmss, run_ppm, walk_hhmmss, walk_ppm, miles)
    log_result(result)

    assert_almost_equal(result['avg_mph'], 5.0000000)
    assert_almost_equal(result['miles'], 4.000)
    assert_almost_equal(result['proj_miles'], 4.000)

    assert(result['avg_ppm'] == '12:00.0')
    assert(result['proj_time'] == '00:48:00')
    assert(result['run_hhmmss'] == '10:00')
    assert(result['run_ppm'] == '8:00')
    assert(result['walk_hhmmss'] == '10:00')
    assert(result['walk_ppm'] == '16:00')

def test_calculate_9_to_1_marathon():
    run_hhmmss = '9:00'
    run_ppm = '9:00'
    walk_hhmmss = '1:00'
    walk_ppm = '18:00'
    miles = '26.2'

    result = m26.RunWalkCalculator.calculate(run_hhmmss, run_ppm, walk_hhmmss, walk_ppm, miles)
    log_result(result)

    assert_almost_equal(result['avg_mph'], 6.0606060606060606)
    assert_almost_equal(result['miles'], 26.200)
    assert_almost_equal(result['proj_miles'], 26.200)

    assert(result['avg_ppm'] == '9:54.0')
    assert(result['proj_time'] == '04:19:22')
    assert(result['run_hhmmss'] == '9:00')
    assert(result['run_ppm'] == '9:00')
    assert(result['walk_hhmmss'] == '1:00')
    assert(result['walk_ppm'] == '18:00')
