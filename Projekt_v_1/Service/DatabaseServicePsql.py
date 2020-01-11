import psycopg2

class DatabaseServicePsql:

    def __init__(self):
        self.user = "postgres"
        self.password = "admin"
        self.database = "learning"
        self.host = "localhost"
        self.port = "5432"

    def connect_to_db(self):
        connection = psycopg2.connect(
            user=self.user,
            password=self.password,
            database=self.database,
            host=self.host,
            port=self.port)
        return connection

    # connection.commit()
    # connection.close()
