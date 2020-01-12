import psycopg2
from psycopg2.extras import execute_values

class DatabaseServicePsql:

    # table wypozyczenia
    table_name = "wypozyczenia"
    field_name_id = "id"
    field_name_data_wynajmu = "data_wynajmu"
    field_name_data_zwrotu = "data_zwrotu"
    field_name_stacja_wynajmu = "stacja_wynajmu"
    field_name_stacja_zwrotu = "stacja_zwrotu"

    geo_table_name = "punkty"
    geo_field_id = "id"
    geo_field_geom = "geom"
    geo_field_label = "label"

    def __init__(self):
        self.user = "postgres"
        self.password = "admin"
        self.database = "projekt"
        self.host = "localhost"
        self.port = "5432"
        self.required_coefficient = 0.5

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

        number_of_proper_records = 0
        expected_time_minutes = DatabaseServicePsql.get_expected_time_in_minutes(route.expected_time)
        # print("Expected in minutes: ")
        # print(expected_time_minutes)
        difference_margin = self.get_difference_margin(expected_time_minutes)
        # print("Difference margin is: ")
        # print(difference_margin)

        query = """SELECT count(*) FROM
            (SELECT EXTRACT(minutes FROM (data_zwrotu - data_wynajmu))::integer AS m FROM wypozyczenia
            WHERE stacja_wynajmu = %s AND stacja_zwrotu = %s) AS arr
            WHERE abs(m - %s) < %s;
        """
        with self.connect_to_db() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (
                    route.from_station_name,
                    route.to_station_name,
                    expected_time_minutes,
                    difference_margin))
                # print(cursor.mogrify(query, (
                #     route.from_station_name,
                #     route.to_station_name,
                #     expected_time_minutes,
                #     difference_margin)))
                # print(cursor.fetchone()[0])
                number_of_proper_records = cursor.fetchone()[0]
        return number_of_proper_records

    @classmethod
    def get_expected_time_in_minutes(cls, expected_time):
        expected_time_minutes = int(expected_time / 60)
        return expected_time_minutes

    def get_difference_margin(self, expected_time_minutes):
        return expected_time_minutes - self.required_coefficient * expected_time_minutes

    def save_points_in_database(self, points_dict):
        rows_list = self.convert_points_dict_to_tuples_list(points_dict)
        sql = "INSERT INTO punkty (geom, label) VALUES %s"
        with self.connect_to_db() as connection:
            with connection.cursor() as cursor:
                execute_values(cursor, sql, rows_list,
                            template="(ST_GeomFromText(%s , 4326), %s)")

    def convert_points_dict_to_tuples_list(self, point_dict):
        rows = []
        for point in point_dict:
            point_tuple = (
                "POINT(" + str(point.latitude) + " " + str(point.longitude) + ")",
                point_dict[point])
            rows.append(point_tuple)
        return rows;
