"""Module for fizzbuzz repository's configuration."""

from aiohttp.web import Application
from service.clients.database import DBDriver
from service.models.fizzbuzz_repository import FizzBuzzRepository


def setup_fizzbuzz_repository(app: Application, database: DBDriver) -> None:
    """Inject fizz buzz repository into the application's instance.

    Args:
        app (aiohttp.web.Application): Application's instance
        database (aiohttp.web.Request): The current request instance
    """
    app["fizzbuzz_repository"] = FizzBuzzRepository(database)
