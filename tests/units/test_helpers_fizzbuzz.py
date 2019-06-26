import hashlib
import pytest

from service.helpers.fizzbuzz import fizzbuzz, hash_request


class TestFizzBuzzHelpers:
    def test_hash_fizzbuzz_request(self):
        fizzbuzz_input = [3, 7, 22, "foo", "bar"]
        expected_output = hashlib.sha1(b"3722foobar").hexdigest()
        assert hash_request(*fizzbuzz_input) == expected_output

    def test_fizzbuzz(self):
        fizzbuzz_input = [3, 5, 16, "fizz", "buzz"]
        expected_output = [
            1,
            2,
            "fizz",
            4,
            "buzz",
            "fizz",
            7,
            8,
            "fizz",
            "buzz",
            11,
            "fizz",
            13,
            14,
            "fizzbuzz",
            16,
        ]
        assert fizzbuzz(*fizzbuzz_input) == expected_output
