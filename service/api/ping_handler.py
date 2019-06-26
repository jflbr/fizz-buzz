"""
Handles the GET /api/1/ping API endpoint.
"""

from aiohttp.web import json_response, Request

from service.config import SERVICE_VERSION


async def get_ping(request: Request):
    res = {"status": "ok", "version": SERVICE_VERSION}
    return json_response(res)
