from service.models.fizzbuzz_repository import FizzBuzzRepository


def setup_fizzbuzz_repository(app, database):
    app["fizzbuzz_repository"] = FizzBuzzRepository(database)
