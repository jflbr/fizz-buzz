"""Database abstraction module."""
import asyncpg
from aiohttp.web import Application


class DBDriver:
    """Database abstraction driver"""

    def __init__(self, configuration: dict):
        """Initialize database abstraction driver.

        Args:
            configuration (dict): Database info and credentials
        """
        self.host = configuration.get("host")
        self.port = configuration.get("port")
        self.protocol = configuration.get("protocol")
        self.user = configuration.get("user")
        self.password = configuration.get("password")
        self.database = configuration.get("database")
        self._connection = None

    @property
    async def connection(self) -> asyncpg.connection:
        """Provide a database connection if it exists or create a new one otherwise.

        Returns:
            asyncpg.connection: Instance of a database connection
        """
        if self._connection and not self._connection.is_closed():
            return self._connection
        self._connection = await asyncpg.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        return self._connection


def setup_database_connection(app: Application, configuration: dict) -> None:
    """Inject database connection into the application's instance.
    Args:
        app: aiohttp.web.Application
        configuration(dict): Database info and credentials

    """
    app["database"] = DBDriver(configuration)
