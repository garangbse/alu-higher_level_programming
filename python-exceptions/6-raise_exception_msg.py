#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    Raises a name exception with a message.

    Args:
        message (str): The message to be included with the name exception.

    Raises:
        NameError: Always raises this exception with the given message.
    """
    raise NameError(message)
