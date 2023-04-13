import mysql.connector
from mysql.connector import Error


class DbMySql:
    def __int__(self):
        self.host = "localhost"
        self.database = "developer"
        self.user = "dev"
        self.password = "dev"

    def db_connect(self):
        connection = None
        cursor = None

        try:
            connection = mysql.connector.connect(host="localhost",
                                                 database="developer",
                                                 user="root",
                                                 password="root")
            if connection.is_connected():
                db_info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_info)
                cursor = connection.cursor()
        except Exception as e:
            print("**", e)
            print("Error while connecting to MySQL", e)
        finally:
            return connection, cursor
