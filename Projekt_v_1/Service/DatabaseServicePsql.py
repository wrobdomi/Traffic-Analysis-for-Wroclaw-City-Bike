import psycopg2

class DatabaseServicePsql:

    # table wypozyczenia
    table_name = "wypozyczenia"
    field_name_id = "id"
    field_name_data_wynajmu = "data_wynajmu"
    field_name_data_zwrotu = "data_zwrotu"
    field_name_stacja_wynajmu = "stacja_wynajmu"
    field_name_stacja_zwrotu = "stacja_zwrotu"

    def __init__(self):
        self.user = "postgres"
        self.password = "admin"
        self.database = "projekt"
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

    def get_number_of_proper_records(self, route):
        query = """SELECT count(*) FROM
            (SELECT EXTRACT(minutes FROM (data_zwrotu - data_wynajmu))::integer AS m FROM wypozyczenia
            WHERE stacja_wynajmu = 'Traugutta - Pułaskiego' AND stacja_zwrotu = 'Rynek') AS arr
            WHERE abs(m-15) < 3;
        """
        with self.connect_to_db() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                print(cursor.fetchone())