import os


def get_env_variable(variable_name, default_value=''):
    return os.environ.get(variable_name, default_value)


def parse_comma_list(comma_sep_str):
    """
        Parse a comma-separated string and return a list of stripped strings.

        Args:
            comma_sep_str (str): The comma-separated string to parse.

        Returns:
            list: A list of stripped strings.

        Note:
            If the input string is empty or not a string, an empty list is returned.
            The strings in the resulting list are stripped of leading and trailing whitespace.

        Examples:
            >>> parse_comma_list('hello, world')
            ['hello', 'world']

            >>> parse_comma_list('   apple,   banana,   cherry   ')
            ['apple', 'banana', 'cherry']
    """  # noqa
    if not comma_sep_str or not isinstance(comma_sep_str, str):
        return []
    return [string.strip() for string in comma_sep_str.split(',') if string]
