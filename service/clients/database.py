import asyncio

import asyncpg


class DBDriver(object):
    def __init__(self, configuration):
        self.host = configuration.get("host")
        self.port = configuration.get("port")
        self.protocol = configuration.get("protocol")
        self.user = configuration.get("user")
        self.password = configuration.get("password")
        self.database = configuration.get("database")
        self._connection = None

    async def __call__(self):
        conn = await self.connection
        return conn

    @property
    async def connection(self):
        if self._connection and not self._connection.is_closed():
            return self._connection
        self._connection = await asyncpg.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        return self._connection


async def close_connection(app):
    await app["database"].connection.close()


def setup_database_connection(app, configuration):
    app["database"] = DBDriver(configuration)
