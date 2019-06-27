# Fizz-Buzz

[![Build Status](https://travis-ci.org/jflbr/fizz-buzz.svg?branch=master)](https://travis-ci.com/jflbr/fizz-buzz)

A simple fizz-buzz REST server


## Build docker image
```bash
docker build -t fizz-buzz:latest [--build-arg INSTALL_ARGS=--dev] .
```

## Run all the tests using docker-compose
```bash
docker-compose build test
docker-compose run test
```

You can run specific test modules as follows:
```bash
docker-compose run --rm test pytest --cov=service tests/interface/test_fizzbuzz_statistics.py
```

Or even single test case:
```bash
docker-compose run --rm test pytest --cov=service tests/interface/test_fizzbuzz_statistics.py::test_empty_fizzbuzz_statistics
```

## Run the application using docker compose

```bash
docker-compose build fizz-buzz
docker-compose run fizz-buzz
```

## OpenAPI documentation

After running the application, the OpenAPI documentation will be available at http://localhost:8080/api/1/doc
