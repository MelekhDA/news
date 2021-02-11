"""
Utilities for news app
"""


def str2bool(string: str) -> bool:
    """
    Converts a string value to boolean type

    :param string: value to convert to boolean

    :return: boolean
    """

    return string.lower() in ['true', 't', '1', '1.0']
