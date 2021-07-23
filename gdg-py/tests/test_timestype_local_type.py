import pytest

import glob
import os
import time

import gdg


def test_typical_use():
    # ensure the target directories are present and empty of regular files
    dir_path = __test_directory_path()
    __ensure_dir_present_and_empty(dir_path)

    g = gdg.Gdg(dir_path)
    assert(g.get_state() == {})

    bool = g.set_generations(3)
    assert(g.get_state() == {'generations': 3})

    bool = g.set_pattern('sample-%.txt', 'ts_local')
    assert(bool == True)
    assert(g.get_pattern() == 'sample-%.txt')

    # assertions after .gdg state is established
    state = g.get_state()
    assert(len(state.keys()) == 4)
    assert(state['generations'] == 3)
    assert(state['pattern']     == 'sample-%.txt')
    assert(state['value_param'] == 'ts_local')
    assert(state['regexp']      == 'sample-\\d\\d\\d\\d\\d\\d\\d\\d-\\d\\d\\d\\d\\d\\d.txt')

    # assert initial set of files
    assert(g.previous() == None)
    assert(g.current() == None)
    assert(g.all_generations() == [])
    assert(g.all_files() == [])

    for fname in __test_fixture_files():
        __write(fname, 'this if file {}'.format(fname))

    fname = g.next()
    __write(fname, 'this if file {}'.format(fname))

    assert(len(g.all_generations()) == 3)
    assert(len(g.all_generations(limited=False)) == 6)
    assert(len(g.all_files()) == 6)

    assert(g.prune() == 3)
    assert(g.prune() == 0)

    assert(len(g.all_generations()) == 3)
    assert(len(g.all_generations(limited=False)) == 3)
    assert(len(g.all_files()) == 3)

    assert(g.previous() == __test_fixture_files()[-1])
    assert(g.current()  == fname)

    assert(str(g).startswith('<Gdg directory:tmp/ts_local state:{'))

# private methods

def __test_directory_path():
    return 'tmp/ts_local'

def __test_fixture_files():
    return [
        'tmp/ts_local/sample-20210207-172005.txt',
        'tmp/ts_local/sample-20210207-172006.txt',
        'tmp/ts_local/sample-20210207-172007.txt',
        'tmp/ts_local/sample-20210207-172008.txt',
        'tmp/ts_local/sample-20210207-172009.txt'
    ]

def __ensure_dir_present_and_empty(dir_path):
    if os.path.isdir(dir_path):
        for f in glob.glob('{}/.gdg'.format(dir_path)):
            os.remove(f)
        for f in glob.glob('{}/*'.format(dir_path)):
            os.remove(f)
    else:
        os.mkdir(dir_path) 

def __write(outfile, s):
    with open(outfile, 'w') as f:
        f.write(s)
