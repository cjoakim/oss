__author__ = 'cjoakim'


class GdgConstants(object):

    @classmethod
    def format_generation(cls):
        return 'g'

    @classmethod
    def format_epoch(cls):
        return 'e'

    @classmethod
    def format_timestamp_utc(cls):
        return 'ts_utc'

    @classmethod
    def format_timestamp_local(cls):
        return 'ts_local'

    @classmethod
    def valid_formats(cls):
        return [
            GdgConstants.format_generation(),
            GdgConstants.format_epoch(),
            GdgConstants.format_timestamp_utc(),
            GdgConstants.format_timestamp_local()
        ]

    @classmethod
    def generation_format(cls):
        return '{0:06d}'

    @classmethod
    def timestamp_format(cls):
        return '%Y%m%d-%H%M%S'

    @classmethod
    def parameter_char(cls):
        return '%'

    @classmethod
    def re_generation_number(cls):
        return '\\d\\d\\d\\d\\d\\d'

    @classmethod
    def re_token_map(cls):
        d = dict()
        d[GdgConstants.format_generation()]      = '\\d\\d\\d\\d\\d\\d'  # 6 digits
        d[GdgConstants.format_epoch()]           = '\\d\\d\\d\\d\\d\\d\\d\\d\\d\\d'  # 10 digits
        d[GdgConstants.format_timestamp_utc()]   = '\\d\\d\\d\\d\\d\\d\\d\\d-\\d\\d\\d\\d\\d\\d'  # 20210205-075623
        d[GdgConstants.format_timestamp_local()] = '\\d\\d\\d\\d\\d\\d\\d\\d-\\d\\d\\d\\d\\d\\d'  # 20210205-075623
        return d 
