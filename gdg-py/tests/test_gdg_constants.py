import pytest

import gdg


def test_format_generation():
    assert(gdg.GdgConstants.format_generation() == 'g')

def test_format_epoch():
    assert(gdg.GdgConstants.format_epoch() == 'e')

def test_format_timestamp_utc():
    assert(gdg.GdgConstants.format_timestamp_utc() == 'ts_utc')

def test_format_timestamp_local():
    assert(gdg.GdgConstants.format_timestamp_local() == 'ts_local')

def test_valid_formats():
    assert(gdg.GdgConstants.valid_formats() == __expected_format_keys())

def test_generation_format():
    assert(gdg.GdgConstants.generation_format() == '{0:06d}')

def test_timestamp_format():
    assert(gdg.GdgConstants.timestamp_format() == '%Y%m%d-%H%M%S')

def test_parameter_char():
    assert(gdg.GdgConstants.parameter_char() == '%')

def test_re_generation_number():
    assert(gdg.GdgConstants.re_generation_number() == '\\d\\d\\d\\d\\d\\d')

def test_re_token_map():
    map = gdg.GdgConstants.re_token_map()
    expected_keys = sorted(__expected_format_keys())
    assert(sorted(map.keys()) == expected_keys)

# private methods

def __expected_format_keys():
    return 'g,e,ts_utc,ts_local'.split(',')
