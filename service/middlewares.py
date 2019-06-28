"""Module for HTTP exceptions logging middleware."""

import logging

from aiohttp.web import (
    HTTPInternalServerError,
    HTTPException,
    Request,
    middleware,
)

LOGGER = logging.getLogger("fizz-buzz")


@middleware
async def log_exception_middleware(request: Request, handler):
    """Catch unhandled HTTP exceptions and log them.

    Args:
        loop (aiohttp.web.Request): The current request instance
    """
    try:
        return await handler(request)
    except Exception as exc:
        LOGGER.exception(exc)
        if isinstance(exc, HTTPException):
            raise
        raise HTTPInternalServerError
