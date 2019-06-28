"""Handles the GET /api/1/fizz-buzz/statistics/ API endpoint."""
import logging

from aiohttp.web import json_response, Response, Request

from service.models.fizzbuzz_repository import FizzBuzzRepository


LOGGER = logging.getLogger("fizz-buzz.statistics")


async def statistics(request: Request) -> Response:
    """Fizzbuzz statistics handler.

    Return the most requested fizzbuzz input.

    Args:
        request(aiohttp.web.Request): request object

    Returns:
        aiohttp.web.json_response: the most frequent fizzbuzz input
    """
    LOGGER.info("Fetch fizz-buzz statistics")
    fizzbuzz_repository: FizzBuzzRepository = request.app[
        "fizzbuzz_repository"
    ]
    most_frequent = await fizzbuzz_repository.get_most_frequent()
    LOGGER.debug("MOST FREQ REQ: %s", most_frequent)

    if most_frequent:
        most_frequent["limit"] = most_frequent.pop("upper_bound")
        most_frequent.pop("id")
        most_frequent.pop("created_at")
        most_frequent.pop("updated_at")

    return json_response(dict(most_frequent=most_frequent))
