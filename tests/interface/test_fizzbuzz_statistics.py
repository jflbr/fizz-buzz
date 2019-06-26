from service.__main__ import create_app
from tests.interface.fakes.fizzbuzz_repository import FizzBuzzRepository


async def test_empty_fizzbuzz_statistics(aiohttp_client):
    client = await aiohttp_client(create_app)
    client.app["fizzbuzz_repository"] = FizzBuzzRepository()
    expected_response = dict(most_frequent=None)

    resp = await client.get("/api/1/fizz-buzz/statistics/")

    assert resp.status == 200
    response_body = await resp.json()
    assert response_body == expected_response


async def test_single_hit_fizzbuzz_statistics(aiohttp_client):
    client = await aiohttp_client(create_app)
    fizzbuzz_repository: FizzBuzzRepository = FizzBuzzRepository()
    await fizzbuzz_repository.create(int1=3, int2=5, limit=16, str1="fizz", str2="buzz")
    client.app["fizzbuzz_repository"] = fizzbuzz_repository
    expected_response = dict(
        most_frequent=dict(int1=3, int2=5, limit=16, str1="fizz", str2="buzz", hits=1)
    )

    resp = await client.get("/api/1/fizz-buzz/statistics/")

    assert resp.status == 200
    response_body = await resp.json()
    assert response_body["most_frequent"] == expected_response["most_frequent"]


async def test_multiple_fizzbuzz_statistics(aiohttp_client):
    client = await aiohttp_client(create_app)
    fizzbuzz_repository: FizzBuzzRepository = FizzBuzzRepository()
    expected_max_hits = 10
    expected_response = dict(
        most_frequent=dict(
            int1=3, int2=5, limit=16, str1="fizz", str2="buzz", hits=expected_max_hits
        )
    )
    other_hits = expected_max_hits - 2
    for _ in range(expected_max_hits):
        await fizzbuzz_repository.create(
            int1=3, int2=5, limit=16, str1="fizz", str2="buzz"
        )

    for index in range(other_hits):
        await fizzbuzz_repository.create(
            int1=2, int2=5, limit=16, str1="foo", str2="bar"
        )
        await fizzbuzz_repository.create(
            int1=(index + 1), int2=5, limit=16, str1="foo", str2="bar"
        )

    client.app["fizzbuzz_repository"] = fizzbuzz_repository

    resp = await client.get("/api/1/fizz-buzz/statistics/")

    assert resp.status == 200
    response_body = await resp.json()
    assert response_body["most_frequent"] == expected_response["most_frequent"]
