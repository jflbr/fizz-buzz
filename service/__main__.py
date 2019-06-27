import logging
from logging import config
from pathlib import Path, PurePath


from aiohttp import web
from aiohttp_swagger import setup_swagger
import asyncio
import uvloop
from yaml import safe_load

from service.config import (
    SERVICE_PORT,
    DB_ENGINE,
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_USER,
    DB_PORT,
)
from service.api import fizzbuzz_handler
from service.api import fizzbuzz_statistics_handler
from service.api import ping_handler
from service.middlewares import log_exception_middleware
from service.clients.database import setup_database_connection
from service.models.repository_configuration import setup_fizzbuzz_repository


logging.config.dictConfig(safe_load(open("logging.yaml", "r")))
logger = logging.getLogger("fizz-buzz")


def main():
    logger.info("Service Startss")
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    app = create_app(loop=None)

    web.run_app(app, port=SERVICE_PORT)


def create_app(loop):
    app = web.Application(loop=loop, middlewares=[log_exception_middleware])
    setup_database_connection(
        app,
        {
            "protocol": DB_ENGINE,
            "host": DB_HOST,
            "database": DB_NAME,
            "password": DB_PASSWORD,
            "user": DB_USER,
            "port": DB_PORT,
        },
    )
    setup_fizzbuzz_repository(app, app["database"])

    here = Path(__file__).parent.absolute()
    swagger_doc_path = str(PurePath(here, "../doc/api.yaml"))
    setup_swagger(app, swagger_url="/api/1/doc", swagger_from_file=swagger_doc_path)

    app.router.add_routes(
        [
            web.route(method="get", path="/api/1/ping", handler=ping_handler.get_ping),
            web.route(
                method="post",
                path=r"/api/1/fizz-buzz/",
                handler=fizzbuzz_handler.create,
            ),
            web.route(
                method="get",
                path=r"/api/1/fizz-buzz/statistics/",
                handler=fizzbuzz_statistics_handler.statistics,
            ),
        ]
    )
    return app


if __name__ == "__main__":
    main()
