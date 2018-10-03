import psycopg2
import rospy
import rospkg
from commander.data_classes.Camera import Camera

SCHEMA_SQL_FILE = rospkg.RosPack().get_path('commander') + "/resources/schema.sql"


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

        # Create tables.
        self.create()

    @property
    def connection(self):
        """
        Database connection.

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
        Database cursor.

        :return: psycopg2 cursor.
        """
        if not self._cursor or self._cursor.closed:
            self._cursor = self.connection.cursor()
        return self._cursor

    def create(self):
        """
        Create database tables.
        """
        try:
            self.cursor.execute(open(SCHEMA_SQL_FILE).read())
            self.connection.commit()
        except psycopg2.Error as e:
            rospy.logerr(e)
        finally:
            self.connection.close()

    def add_camera(self, camera):
        """
        Add camera to the database.

        :param camera: Camera.
        """

        sql = """INSERT INTO cameras(name, url)
                 VALUES('%s', '%s')
                 RETURNING id;""" \
              % (camera.name, camera.url)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            camera.id = self.cursor.fetchone()[0]
        except psycopg2.Error as e:
            rospy.logerr(e)
        finally:
            self.connection.close()

    def remove_camera(self, id):
        """
        Remove camera from the database.

        :param id: Camara's ID.
        """
        sql = """DELETE FROM cameras
                 WHERE id = '%s'""" \
              % id
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except psycopg2.Error as e:
            rospy.logerr(e)
        finally:
            self.connection.close()

    def get_camera(self, id):
        """
        Get camera from the database.

        :param id: Camera's ID.
        :return: Camera.
        """

        pass

    def get_cameras(self):
        pass

    def add_filter(self):
        pass

    def remove_filter(self):
        pass
