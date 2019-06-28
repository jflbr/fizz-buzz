"""Handles the GET /api/1/ping API endpoint."""

from aiohttp.web import json_response, Request

from service.config import SERVICE_VERSION


async def get_ping(request: Request):
    """Health handler.

    Return the service status and version.

    Args:
        request(aiohttp.web.Request): request object

    Returns:
        aiohttp.web.json_response: Service's status and version
    """
    _ = request
    res = {"status": "ok", "version": SERVICE_VERSION}
    return json_response(res)
