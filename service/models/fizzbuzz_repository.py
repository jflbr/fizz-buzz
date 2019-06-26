import logging

import asyncpg

from service.helpers.fizzbuzz import hash_request


LOGGER = logging.getLogger("fizz-buzz.models.fizzbuzz-repository")


class FizzBuzzRepository(object):
    def __init__(self, database):
        self.database = database

    async def get_most_frequent(self):
        query = """
            SELECT * FROM fizzbuzz
            WHERE hits = (SELECT MAX(hits) FROM fizzbuzz)
        """
        connection = await self.database.connection
        fizzbuzz = await connection.fetchrow(query)
        return dict(fizzbuzz) if fizzbuzz else fizzbuzz

    async def upsert(
        self, fizzbuzz_hash: str, int1: int, int2: int, limit: int, str1: str, str2: str
    ):
        query = """
            INSERT INTO fizzbuzz (
                id,
                int1,
                int2,
                upper_bound,
                str1,
                str2
            ) VALUES (
                $1, $2, $3, $4, $5, $6
            )
            ON CONFLICT (id)
            DO UPDATE SET
                hits = (fizzbuzz.hits + 1)
        """
        connection = await self.database.connection
        fizzbuzz = await connection.fetch(
            query, *[fizzbuzz_hash, int1, int2, limit, str1, str2]
        )

        return fizzbuzz

    async def create(self, int1: int, int2: int, limit: int, str1: str, str2: str):
        fizzbuzz_hash: str = hash_request(int1, int2, limit, str1, str2)
        fizzbuzz = await self.upsert(fizzbuzz_hash, int1, int2, limit, str1, str2)
        return fizzbuzz
