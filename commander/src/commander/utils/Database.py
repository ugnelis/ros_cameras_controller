import psycopg2


class Database:
    """
    Database utils for working with database.

    :ivar name: Database name.
    :ivar username: Database username.
    :ivar password: Database password.
    :ivar host: Database host.
    :ivar port: Database port.
    :ivar _cursor: Database cursor.
    :ivar _connection: Database connection.
    """

    def __init__(self, dbname, username, password=None, host=None, port=None):
        """
        :param dbname: Database name.
        :param username: Database username.
        :param password: Database password.
        :param host: Database host.
        :param port: Database port.
        """
        self.dbname = dbname
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self._cursor = None
        self._connection = None

    @property
    def connection(self):
        """
        :return: psycopg2 connection.
        """
        if not self._connection or self._connection.closed:
            self._connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.username,
                password=self.password,
                host=self.host,
                port=self.port
            )
        return self._connection

    @property
    def cursor(self):
        """
        :return: psycopg2 cursor.
        """
        if not self._cursor or self._cursor.closed:
            self._cursor = self.connection.cursor()
        return self._cursor
