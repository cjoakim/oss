import pytest

import glob
import os

import gdg

def test_dir_path_with_trailing_sep():
    dir_path_with_trailing_sep = 'tmp/some_path{}'.format(os.path.sep)
    __ensure_dir_present_and_empty(dir_path_with_trailing_sep)

    g = gdg.Gdg(dir_path_with_trailing_sep, reset=True)
    g.save_state()
    assert(g.directory == 'tmp/some_path')
    assert(g.get_generations() == -1)
    assert(g.get_pattern() == None)
    assert(g.next() == None)

    bool = g.set_pattern(None, 'g')
    assert(bool == False)
    assert(g.get_pattern() == None)

    bool = g.set_pattern('sample-%.txt', None)
    assert(bool == False)
    assert(g.get_pattern() == None)

def test_typical_use():
    # ensure the target directories are present and empty of regular files
    dir_path = __test_directory_path()
    __ensure_dir_present_and_empty(dir_path)

    g = gdg.Gdg(dir_path)
    assert(g.get_state() == {})

    bool = g.set_generations(-1)
    assert(bool == False)

    bool = g.set_generations('ten')
    assert(bool == False)
    assert(g.get_state() == {})

    bool = g.set_generations('9')
    assert(bool == True)
    assert(g.get_state() == {'generations': 9})

    bool = g.set_generations(10)
    assert(g.get_state() == {'generations': 10})

    bool = g.set_pattern('sample-%.txt', 'Q')
    assert(bool == False)

    bool = g.set_pattern('sample-%.txt', 'g')
    assert(bool == True)
    assert(g.get_pattern() == 'sample-%.txt')

    # assertions after .gdg state is established
    state = g.get_state()
    assert(len(state.keys()) == 4)
    assert(state['generations'] == 10)
    assert(state['pattern']     == 'sample-%.txt')
    assert(state['value_param'] == 'g')
    assert(state['regexp']      == 'sample-\\d\\d\\d\\d\\d\\d.txt')

    # assert initial set of files
    assert(g.previous() == None)
    assert(g.current() == None)
    assert(g.all_generations() == [])
    assert(g.all_files() == [])

    assert(g.next() == 'tmp/generations/sample-000001.txt')

    for i in range(1, 21):  # write files 000001 through 000020
        fname = g.next()
        __write(fname, 'this if file {}'.format(i))
    
    assert(g.previous() == 'tmp/generations/sample-000019.txt')
    assert(g.current()  == 'tmp/generations/sample-000020.txt')

    assert(len(g.all_generations()) == 10)
    assert(len(g.all_generations(limited=False)) == 20)
    assert(len(g.all_files()) == 20)

    assert(g.prune() == 10)
    assert(g.prune() == 0)

    assert(len(g.all_generations()) == 10)
    assert(len(g.all_generations(limited=False)) == 10)
    assert(len(g.all_files()) == 10)

    expected_files_list = [
        'tmp/generations/sample-000011.txt', 
        'tmp/generations/sample-000012.txt', 
        'tmp/generations/sample-000013.txt', 
        'tmp/generations/sample-000014.txt', 
        'tmp/generations/sample-000015.txt', 
        'tmp/generations/sample-000016.txt', 
        'tmp/generations/sample-000017.txt', 
        'tmp/generations/sample-000018.txt', 
        'tmp/generations/sample-000019.txt', 
        'tmp/generations/sample-000020.txt'
    ]
    assert(g.all_files() == expected_files_list)
    assert(g.all_generations() == expected_files_list)
    assert(g.all_generations(limited=False) == expected_files_list)

    assert(g.previous() == 'tmp/generations/sample-000019.txt')
    assert(g.current()  == 'tmp/generations/sample-000020.txt')
    assert(g.next()     == 'tmp/generations/sample-000021.txt')

    assert(str(g).startswith('<Gdg directory:tmp/generations state:{'))

# private methods

def __test_directory_path():
    return 'tmp/generations'

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
