import operator


class Matcher(object):
    """docstring for Helper."""

    def __init__(self):
        self.condition_mapper = {
            "=": operator.eq,
            "eq": operator.eq,
            "!=": operator.ne,
            "neq": operator.ne,
            ">": operator.gt,
            "gt": operator.gt,
            "<": operator.lt,
            "lt": operator.lt,
            ">=": operator.gt,
            "gte": operator.gt,
            "<=": operator.lt,
            "lte": operator.lt,
            "in": self._is_in,
            "notin": self._is_not_in,
            "null": lambda x: x is None,
            "notnull": lambda x: x is not None,
            "startswith": lambda v, s: v.startswith(s),
            "endswith": lambda v, s: v.endswith(s),
            "contains": self._is_contain,
        }

    @staticmethod
    def _is_in(key, arr):
        """Checks the given `key` exists in the given `list`

        :@param key, arr
        :@type key: mixed
        :type arr: list

        :@return bool
        """

        return isinstance(arr, list) and bool(
            len(([k for k in key if k in arr] if isinstance(key, list) else key in arr))
        )

    @staticmethod
    def _is_not_in(key, arr):
        """Checks the given `key` is not exists in the given `arr`

        :@param x, y
        :@type x, y: mixed

        :@return bool
        """
        return isinstance(arr, list) and (key not in arr)

    @staticmethod
    def _is_contain(data, val):
        """Checks the given `val` exists in the given `string`

        :@param str, val
        :@type: string/list
        :@type val: string

        :@return bool
        """
        return val in data

    def _to_lower(self, x, y):
        """Convert val to lower case

        :@param x, y
        :@type x, y: mixed

        :@return x, y
        """
        return [
            [v.lower() if isinstance(v, str) else v for v in val]
            if isinstance(val, list)
            else val.lower()
            if isinstance(val, str)
            else val
            for val in [x, y]
        ]

    def _match(self, x, op, y, case_insensitive):
        """Compare the given `x` and `y` based on `op`

        :@param x, y, op, case_insensitive
        :@type x, y: mixed
        :@type op: string
        :@type case_insensitive: bool

        :@return bool
        :@throws ValueError
        """
        if op not in self.condition_mapper:
            raise ValueError("Invalid where condition given")

        if case_insensitive:
            x, y = self._to_lower(x, y)

        return self.condition_mapper.get(op)(x, y)
