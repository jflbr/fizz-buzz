"""Module for api input validation."""
from cerberus import Validator as CerberusValidator
from service.config import MAX_LIMIT


FIZZBUZZ_REQUEST_SCHEMA = {
    "int1": {"type": "integer", "required": True, "is_non_zero": True},
    "int2": {"type": "integer", "required": True, "is_non_zero": True},
    "limit": {
        "type": "integer",
        "required": True,
        "min": 1,
        "max": MAX_LIMIT,
    },
    "str1": {
        "type": "string",
        "required": True,
        "minlength": 1,
        "maxlength": 16,
    },
    "str2": {
        "type": "string",
        "required": True,
        "minlength": 1,
        "maxlength": 16,
    },
}


class Validator(CerberusValidator):
    """JSON schema validation class."""
    def _validate_is_non_zero(self, is_non_zero, field, value):
        """ Make sure a  given integer is non zero.
        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """
        if is_non_zero and value == 0:
            self._error(field, "Must be non zero")
