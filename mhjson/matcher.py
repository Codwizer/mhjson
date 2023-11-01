class Matcher(object):
    """docstring for Helper."""

    def __init__(self):
        self.condition_mapper = {
            "=": "_is_equal",
            "eq": "_is_equal",
            "!=": "_is_not_equal",
            "neq": "_is_not_equal",
            ">": "_is_greater",
            "gt": "_is_greater",
            "<": "_is_smaller",
            "lt": "_is_smaller",
            ">=": "_is_greater_equal",
            "gte": "_is_greater_equal",
            "<=": "_is_smaller_equal",
            "lte": "_is_smaller_equal",
            "in": "_is_in",
            "notin": "_is_not_in",
            "null": "_is_null",
            "notnull": "_is_not_null",
            "startswith": "_is_starts_with",
            "endswith": "_is_ends_with",
            "contains": "_is_contain",
        }

    def _is_equal(self, x, y):
        """Checks the given values are equal

        :@param x, y
        :@type x, y: mixed

        :@return bool
        """
        return x == y

    def _is_not_equal(self, x, y):
        """Checks the given values are not equal

        :@param x, y
        :@type x, y: mixed

        :@return bool
        """
        return x != y

    def _is_greater(self, x, y):
        """Checks the given value `x` is greater than the given value `y`

        :@param x, y
        :@type x, y: mixed

        :@return bool
        """
        return x > y

    def _is_smaller(self, x, y):
        """Checks the given value `x` is less than the given value `y`

        :@param x, y
        :@type x, y: mixed

        :@return bool
        """
        return x < y

    def _is_greater_equal(self, x, y):
        """Checks the given value `x` is greater than or equal the given value `y`

        :@param x, y
        :@type x, y: mixed

        :@return bool
        """
        return x >= y

    def _is_smaller_equal(self, x, y):
        """Checks the given value `x` is less than or equal the given value `y`

        :@param x, y
        :@type x, y: mixed

        :@return bool
        """
        return x <= y

    def _is_in(self, key, arr):
        """Checks the given `key` is exists in the given `list`

        :@param key, arr
        :@type key: mixed
        :type arr: list

        :@return bool
        """

        return isinstance(arr, list) and bool(
            len(([k for k in key if k in arr] if isinstance(key, list) else key in arr))
        )

    def _is_not_in(self, key, arr):
        """Checks the given `key` is not exists in the given `arr`

        :@param x, y
        :@type x, y: mixed

        :@return bool
        """
        return isinstance(arr, list) and (key not in arr)

    def _is_null(self, x, y=None):
        """Checks the given value `x` is None

        :@param x, y
        :@type x, y: mixed

        :@return bool
        """
        return x is None

    def _is_not_null(self, x, y=None):
        """Checks the given value `x` is not None

        :@param x, y
        :@type x, y: mixed

        :@return bool
        """
        return x is not None

    def _is_starts_with(self, data, val):
        """Checks the given string `data` starts with the given string `val`

        :@param data
        :@param val
        :@type data: string
        :@type val: string

        :@return bool
        """
        return data.startswith(val)

    def _is_ends_with(self, data, val):
        """Checks the given string `data` ends with the given string `val`

        :@param data
        :@param val
        :@type data: string
        :@type val: string

        :@return bool
        """
        return data.endswith(val)

    def _is_contain(self, str, val):
        """Checks the given `val` is exists in the given `string`

        :@param str, val
        :@type: string/list
        :@type val: string

        :@return bool
        """
        return val in str

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

        func = getattr(self, self.condition_mapper.get(op))
        return func(x, y)
