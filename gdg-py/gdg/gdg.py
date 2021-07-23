__author__ = 'cjoakim'

import glob
import json
import os
import re
import sys
import time
import traceback

from datetime import datetime, date, timezone

from .gdg_constants import GdgConstants


class Gdg(object):
    def __init__(self, directory, reset=False):
        self.directory = directory.strip()
        if self.directory.endswith(os.path.sep):
            self.directory = self.directory[:-1]
        self.metafile = '{}{}.gdg'.format(self.directory, os.path.sep)
        if reset == True:
            self.state = {}
        else:
            self.state = self.__read_state()
        self.__write_state()

    def get_state(self):
        return self.__read_state()

    def save_state(self):
        return self.__write_state()

    def set_generations(self, n):
        try:
            if int(n) > 0:
                self.state['generations'] = int(n)
                self.__write_state()
                return True
            else:
                return False
        except:
            return False

    def get_generations(self):
        if 'generations' in self.state:
            return self.state['generations']
        else:
            return -1

    def set_pattern(self, pattern, value_param):
        if (pattern == None) or (len(pattern.strip()) < 1):
            return False
        if (value_param == None) or (len(value_param.strip()) < 1):
            return False
        if (value_param.lower().strip() in GdgConstants.valid_formats()):
            pass
        else:
            return False

        self.state['pattern'] = pattern.strip()
        self.state['value_param'] = value_param.lower().strip()
        self.state['regexp'] = self.__format_regexp()
        self.__write_state()
        return True

    def get_pattern(self):
        if 'pattern' in self.state:
            return self.state['pattern']
        else:
            return None

    def next(self):
        try:
            template = self.state['pattern'].replace(GdgConstants.parameter_char(), '{}')
            values = list()
            p = self.state['value_param']

            if p == GdgConstants.format_generation():
                f, n = self.current(), 0
                if f != None:
                    n = self.__parse_generation_number(f)
                values.append(GdgConstants.generation_format().format(n + 1))

            elif p == GdgConstants.format_epoch():
                values.append(int(time.time()))

            elif p == GdgConstants.format_timestamp_utc():
                values.append(datetime.utcnow().strftime(GdgConstants.timestamp_format()))

            elif p == GdgConstants.format_timestamp_local():
                values.append(datetime.now().strftime(GdgConstants.timestamp_format()))

            basename = template.format(*values)
            return '{}{}{}'.format(self.directory, os.path.sep, basename)
        except:
            return None

    def current(self):
        all = self.all_generations()
        if len(all) > 0:
            return all[-1]
        else:
            return None

    def previous(self):
        all = self.all_generations()
        if len(all) > 1:
            return all[-2]
        else:
            return None

    def all_generations(self, limited=True):
        files_list, matched_list = self.__list_directory(), list()
        compiled_re = re.compile('{}{}{}'.format(
            self.directory, os.path.sep, self.state['regexp']))
        for f in files_list:
            m = compiled_re.match(f)
            if m != None:
                matched_list.append(f)

        if limited == True:
            sorted_list = sorted(matched_list)
            index = len(sorted_list) - self.get_generations()
            return sorted(sorted_list[index:])
        else:
            return sorted(matched_list)

    def all_files(self):
        return self.__list_directory()

    def prune(self, do_deletes=False):
        # return the number of files removed from the filesystem
        retain_hash = self.__generations_hash()
        pruned_count = 0
        for f in self.all_files():
            if f not in retain_hash:
                os.remove(f)
                pruned_count = pruned_count + 1
        return pruned_count

    # dunder methods

    def __str__(self):
        return "<Gdg directory:{} state:{}>".format(
            self.directory, json.dumps(self.state))
        
    # private methods follow 

    def __parse_generation_number(self, f):
        match = re.search(GdgConstants.re_generation_number(), f)
        if match != None:
            span = match.span()
            return int(f[span[0]:span[1]])

    def __format_regexp(self):
        format_template = self.state['pattern'].replace('%', '{}')
        format_values = list()
        map_key = self.state['value_param']
        re_value = GdgConstants.re_token_map()[map_key]
        format_values.append(re_value)
        return format_template.format(*format_values)

    def __list_directory(self):
        # this method intentionally omits hidden files in the directory, such as .gdg
        return sorted(glob.glob('{}/*'.format(self.directory)))

    def __generations_hash(self):
        hash = dict()
        for f in self.all_generations():
            hash[f] = True
        return hash

    def __read_state(self):
        try:
            with open(self.metafile, 'rt') as f:
                return json.loads(f.read())
        except:
            return {}

    def __write_state(self):
        with open(self.metafile, 'w') as f:
            jstr = json.dumps(self.state)
            f.write(jstr)
