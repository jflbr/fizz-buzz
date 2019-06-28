"""
Loads the configuration from the environment variable,
prevents the service to start if the variable cannot be found
"""
import os

# service configuration
SERVICE_VERSION = os.getenv("SERVICE_VERSION", "")
SERVICE_PORT = int(os.getenv("PORT", "8080"))

# database configuration
DB_ENGINE = os.getenv("DB_ENGINE", "postgresql")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "fizzbuzz")
DB_PASSWORD = os.getenv("DB_PASSWORD", "fizzbuzz")
DB_NAME = os.getenv("DB_NAME", "fizzbuzz")

# maximum upper bound of a fizzbuzz input
MAX_LIMIT = int(os.getenv("MAX_LIMIT", "100"))
