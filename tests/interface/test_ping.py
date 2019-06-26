from service.__main__ import create_app


async def test_ping(aiohttp_client):
    client = await aiohttp_client(create_app)
    resp = await client.get("/api/1/ping")
    assert resp.status == 200
    response_payload = await resp.json()
    assert "status" in response_payload
    assert "version" in response_payload
