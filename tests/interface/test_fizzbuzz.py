import aiohttp
import pytest

from service.__main__ import create_app


async def test_nominal_fizzbuzz(aiohttp_client):
    client = await aiohttp_client(create_app)
    expected_response = [
        1,
        2,
        "fizz",
        4,
        "buzz",
        "fizz",
        7,
        8,
        "fizz",
        "buzz",
        11,
        "fizz",
        13,
        14,
        "fizzbuzz",
        16,
    ]

    resp = await client.post(
        "/api/1/fizz-buzz/",
        json=dict(int1=3, int2=5, limit=16, str1="fizz", str2="buzz"),
    )

    assert resp.status == 201
    response_body = await resp.json()
    assert response_body == expected_response


async def test_missing_int1_fizzbuzz(aiohttp_client):
    client = await aiohttp_client(create_app)

    resp = await client.post(
        "/api/1/fizz-buzz/",
        json=dict(int2=5, limit=16, str1="fizz", str2="buzz"),
    )

    assert resp.status == 422
    response_body = await resp.json()
    assert "invalid_parameters" in response_body
    assert "int1" in response_body["invalid_parameters"]


async def test_zero_int1_fizzbuzz(aiohttp_client):
    client = await aiohttp_client(create_app)

    resp = await client.post(
        "/api/1/fizz-buzz/",
        json=dict(int1=0, int2=5, limit=16, str1="fizz", str2="buzz"),
    )

    assert resp.status == 422
    response_body = await resp.json()
    assert "invalid_parameters" in response_body
    assert "int1" in response_body["invalid_parameters"]
