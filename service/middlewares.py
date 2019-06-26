import logging

from aiohttp.web import HTTPInternalServerError, HTTPException, Request, middleware

logger = logging.getLogger("fizz-buzz")


@middleware
async def log_exception_middleware(request: Request, handler):
    try:
        return await handler(request)
    except Exception as exc:
        logger.exception(exc)
        if isinstance(exc, HTTPException):
            raise
        raise HTTPInternalServerError
