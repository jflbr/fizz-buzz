# Fizz-Buzz

[![Build Status](https://travis-ci.org/jflbr/fizz-buzz.svg?branch=master)](https://travis-ci.org/jflbr/fizz-buzz)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)


A simple [fizz-buzz](https://en.wikipedia.org/wiki/Fizz_buzz) REST server implementation.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

In order to get the development environment up and running you need to have docker and docker-compose installed. Following example is taken from the official documentation for Ubuntu.
You can find a detailed list of instructions in the [official documentation page](https://docs.docker.com/install/) depending on your OS and distribution.


### Clone the application repository

```bash
git clone https://github.com/jflbr/fizz-buzz.git
```

### Installing the dependencies

Installing your development environment is a matter of running a single command line at the root of the application folder.

```bash
docker-compose build
```

Under the hood, this will build the application's image (from the Dockerfile within the root folder)
and link it to a Postgres image; the only external dependency we have here. The docker image build installs Python dependencies specified in the `Pipfile` file. This is the place to put any dependency you might need for the application. This will also mount a volume that will enable both your host machine and containers to share the application files. So any change made in your IDE will be available in the application container.

## Running the tests

Following explains how to run the automated tests of the application.

### Run all the tests and display the code coverage

```bash
docker-compose run test
```
#### Run unit tests

```bash
# with the coverage report
docker-compose run --rm test pytest --cov=service tests/units/

# without the coverage
docker-compose run --rm test pytest tests/units/

# specific unit tests module
docker-compose run --rm test pytest tests/units/test_helpers_fizzbuzz.py

# specific unit test case
docker-compose run --rm test pytest tests/units/test_helpers_fizzbuzz.py::TestFizzBuzzHelpers::test_hash_fizzbuzz_request
```

#### Run interface tests

```bash
# with the coverage report
docker-compose run --rm test pytest --cov=service tests/interface/

# without the coverage
docker-compose run --rm test pytest tests/interface/

# specific interface tests module
docker-compose run --rm test pytest tests/interface/test_fizzbuzz.py

# specific interface test case
docker-compose run --rm test pytest tests/interface/test_fizzbuzz_statistics.py::test_empty_fizzbuzz_statistics
```

#### Check code formatting with black

```bash
docker-compose run --rm test black --check
```

#### Format code using black

```bash
docker-compose run --rm test black .
```
## Running a local instance of the application

You can run the application locally with the following command:
```bash
docker-compose up fizz-buzz
```
This command will run the service and make it available at http://localhost:8080 .

Before using the local instance of the service, you might need to apply the application migrations if this is the first time you run that command or if you made some database schema changes. 

You can run the migrations as follows

```bash
docker-compose up migrate
```
Or like this:

```bash
docker-compose run --rm test alembic upgrade head
```

## OpenAPI documentation

The application embeds an OpenAPI documentation.
After running the application, the OpenAPI documentation will be available at http://localhost:8080/api/1/doc.

The online (`staging`) version is available at https://rest-fizz-buzz.herokuapp.com/api/1/doc 


## Continuous integration and Deployment

The application CI pipeline is managed by [Travis CI](https://travis-ci.org) and the job history is available [here](https://travis-ci.org/jflbr/fizz-buzz).

The CI pipeline currently includes two stages: `script` and `deploy`.

#### Script stage

This stage checks the code formatting with black, runs all the tests and display the code coverage.

#### Deploy stage

This stage triggers a deployment of the application on [Heroku](https://heroku.com) if the current branch being qualified in the CI is the `master` branch.
The deployed application will be available at https://rest-fizz-buzz.herokuapp.com and its OpenAPI documentation at https://rest-fizz-buzz.herokuapp.com/api/1/doc
