import json
from datetime import datetime

__author__ = 'attakei'


class CustomJSONSerializer(object):
    """
    Simple wrapper around json to be used in signing.dumps and
    signing.loads.
    """
    def _support_datetime_default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(repr(obj) + " is not JSON serializable")

    def dumps(self, obj):
        return json.dumps(obj, default=self._support_datetime_default, separators=(',', ':')).encode('latin-1')

    def loads(self, data):
        return json.loads(data.decode('latin-1'))
