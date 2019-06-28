"""Fizzbuzz helpers module."""
import hashlib


def hash_request(
    int1: int, int2: int, limit: int, str1: str, str2: str
) -> str:
    """Create a fizzbuzz input unique identifier.

    The identifier is the sha-1 of a string formatted  version of the input
    Args:
        int1(int): First multiple number of the fizzbuzz input
        int2(int): Second multple number of the fizzbuzz input
        limit(int): Upper bound of the fizzbuz input range
        str1(str): Fizz string
        str2(str): Buzz string
    Returns:
        str: Unique identifier of the fizzbuzz input
    """
    request_string: str = f"{int1}{int2}{limit}{str1}{str2}"
    hash_object = hashlib.sha1(request_string.encode())
    return hash_object.hexdigest()


def fizzbuzz(int1: int, int2: int, limit: int, str1: str, str2: str):
    """Process a fizzbuzz input.

    Returns a list of strings with numbers from 1 to `limit`, where: all
    multiples of `int1` are replaced by `str1`, all multiples of `int2` are
    replaced by `str2`, all multiples of `int1` and `int2` are replaced by
    `str1str2`.
    Args:
        int1(int): First multiple number of the fizzbuzz input
        int2(int): Second multple number of the fizzbuzz input
        limit(int): Upper bound of the fizzbuz input range
        str1(str): Fizz string
        str2(str): Buzz string
    Returns:
        list: List representing the processed fizzbuzz input
    """
    output = []
    for number in range(1, limit + 1):
        if (number % int1) == 0 and (number % int2) == 0:
            output.append(f"{str1}{str2}")
            continue
        elif (number % int1) == 0:
            output.append(f"{str1}")
        elif (number % int2) == 0:
            output.append(f"{str2}")
        else:
            output.append(number)
    return output
