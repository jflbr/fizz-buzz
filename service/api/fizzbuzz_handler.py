"""Handles the POST /api/1/fizz-buzz/ API endpoint."""
import logging

from aiohttp.web import json_response, Response, Request

from service.api.schemas import FIZZBUZZ_REQUEST_SCHEMA, Validator
from service.models.fizzbuzz_repository import FizzBuzzRepository
from service.helpers.fizzbuzz import fizzbuzz


LOGGER = logging.getLogger("fizz-buzz.fizz-buzz")


async def create(request: Request) -> Response:
    """Fizzbuzz processing handler.

    Process a fizzbuzz input within an HTTP request object.

    Args:
        request(aiohttp.web.Request): request object

    Returns:
        aiohttp.web.json_response: the processed fizzbuzz
    """
    LOGGER.info("Process fizz-buzz")

    request_body: dict = request.body_exists and await request.json() or {}
    validator = Validator(FIZZBUZZ_REQUEST_SCHEMA)
    if not validator.validate(request_body):
        return json_response(
            dict(invalid_parameters=validator.errors),
            status=422,
            reason="invalid_parameters",
        )

    # TODO: encapsulate the fizzbuzz processing and persistence (fixme)
    # into a "business" class
    processed_fizzbuzz = fizzbuzz(
        request_body["int1"],
        request_body["int2"],
        request_body["limit"],
        request_body["str1"],
        request_body["str2"],
    )

    fizzbuzz_repository: FizzBuzzRepository = request.app[
        "fizzbuzz_repository"
    ]
    _ = await fizzbuzz_repository.create(
        request_body["int1"],
        request_body["int2"],
        request_body["limit"],
        request_body["str1"],
        request_body["str2"],
    )

    return json_response(processed_fizzbuzz, status=201)
