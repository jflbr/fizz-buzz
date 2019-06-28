import datetime

from service.helpers.fizzbuzz import hash_request


class FizzBuzzRepository(object):
    def __init__(self, **store):
        self.store = store if store else dict()
        self.most_frequent = None

    def _update_most_frequent(self, candidate):
        if self.most_frequent is None or (
            candidate["hits"] > self.most_frequent["hits"]
        ):
            self.most_frequent = candidate

    async def create(
        self, int1: int, int2: int, limit: int, str1: str, str2: str
    ):
        fizzbuzz_hash = hash_request(int1, int2, limit, str1, str2)
        if fizzbuzz_hash in self.store:
            self.store[fizzbuzz_hash]["hits"] += 1
            self._update_most_frequent(self.store[fizzbuzz_hash])
            return

        created_at = datetime.datetime.utcnow()
        updated_at = datetime.datetime.utcnow()
        self.store[fizzbuzz_hash] = dict(
            id=fizzbuzz_hash,
            int1=int1,
            int2=int2,
            upper_bound=limit,
            str1=str1,
            str2=str2,
            hits=1,
            created_at=created_at,
            updated_at=updated_at,
        )
        self._update_most_frequent(self.store[fizzbuzz_hash])
        return

    async def get_most_frequent(self):
        return self.most_frequent

    async def clear(self):
        self.store.clear()
        self.most_frequent = None
