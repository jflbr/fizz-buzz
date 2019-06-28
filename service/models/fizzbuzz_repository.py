"""Module defining the persistence layer for fizzbuzz management."""
import logging

from service.helpers.fizzbuzz import hash_request


LOGGER = logging.getLogger("fizz-buzz.models.fizzbuzz-repository")


class FizzBuzzRepository:
    """Persistence layer for fizzbuzz management."""

    def __init__(self, database: dict) -> None:
        """Initialization"""
        self.database: dict = database

    async def get_most_frequent(self) -> dict:
        """Get the most requested fizzbuzz input.

        Returns:
            dict: Dict representing the most requested fizzbuzz input.
        """
        query = """
            SELECT * FROM fizzbuzz
            WHERE hits = (SELECT MAX(hits) FROM fizzbuzz)
        """
        connection = await self.database.connection
        fizzbuzz = await connection.fetchrow(query)
        return dict(fizzbuzz) if fizzbuzz else fizzbuzz

    async def upsert(
        self,
        fizzbuzz_hash: str,
        int1: int,
        int2: int,
        limit: int,
        str1: str,
        str2: str,
    ):
        """Create or update a fizzbuzz input if it does not exist.

        The update consists of incrementing the hits column by 1
        Args:
            fizzbuzz_hash(str): Unique identifier of a fizzbuzz input
            limit(int): Upper bound of the fizzbuz input range
            int1(int): First multiple number of the fizzbuzz input
            int2(int): Second multple number of the fizzbuzz input
            str1(str): Fizz string
            str2(str): Buzz string
        Returns:
            dict: Dict representing the created or updated fizzbuzz input.
        """
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

    async def create(
        self, int1: int, int2: int, limit: int, str1: str, str2: str
    ) -> dict:
        """Get the most requested fizzbuzz inputs.

        Args:
            fizzbuzz_hash(str): Unique identifier of a fizzbuzz input
            limit(int): Upper bound of the fizzbuz input range
            int1(int): First multiple number of the fizzbuzz input
            int2(int): Second multple number of the fizzbuzz input
            str1(str): Fizz string
            str2(str): Buzz string

        Returns:
            dict: Dict representing the most requested fizzbuzz inputs.
        """
        fizzbuzz_hash: str = hash_request(int1, int2, limit, str1, str2)
        fizzbuzz = await self.upsert(
            fizzbuzz_hash, int1, int2, limit, str1, str2
        )
        return fizzbuzz
