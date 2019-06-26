import hashlib


def hash_request(int1: int, int2: int, limit: int, str1: str, str2: str) -> str:
    request_string: str = f"{int1}{int2}{limit}{str1}{str2}"
    hash_object = hashlib.sha1(request_string.encode())
    return hash_object.hexdigest()


def fizzbuzz(int1: int, int2: int, limit: int, str1: str, str2: str):
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
