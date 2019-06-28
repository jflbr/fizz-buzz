import hashlib
import pytest

from service.helpers.fizzbuzz import fizzbuzz, hash_request
from service.api.schemas import FIZZBUZZ_REQUEST_SCHEMA, Validator


class TestApiSchemas:
    @classmethod
    def setup_class(cls):
        cls.validator = Validator(FIZZBUZZ_REQUEST_SCHEMA)

    def test_valid_fizzbuzz_input(self):
        fizzbuzz_input = dict(
            int1=3, int2=7, limit=22, str1="foo", str2="bar"
        )
        assert self.validator.validate(fizzbuzz_input) is True

    def test_zero_int1_in_fizzbuzz_input(self):
        fizzbuzz_input = dict(
            int1=0, int2=7, limit=22, str1="foo", str2="bar"
        )
        assert self.validator.validate(fizzbuzz_input) is False
        assert "int1" in self.validator.errors

    def test_zero_int2_in_fizzbuzz_input(self):
        fizzbuzz_input = dict(
            int1=3, int2=0, limit=22, str1="foo", str2="bar"
        )
        assert self.validator.validate(fizzbuzz_input) is False
        assert "int2" in self.validator.errors

    def test_integer_str1_in_fizzbuzz_input(self):
        fizzbuzz_input = dict(int1=3, int2=7, limit=22, str1=42, str2="bar")
        assert self.validator.validate(fizzbuzz_input) is False
        assert "str1" in self.validator.errors
