from Models.Station import Station
from Models.Route import Route
from Models.Point import Point
from Service.OpenRouteService import  OpenRouteService
from Service.DatabaseServicePsql import DatabaseServicePsql

# data  structures
stations = []
routes = []
points = dict()

# services
open_route_service = OpenRouteService()
database_service = DatabaseServicePsql()

# stations set up
stations_source_file = "../Data/input_stations_extended.csv"
stations = Station.load_stations_from_file(stations_source_file)
# for s in stations:
#    print(s)

# routes set up
routes = Route.create_routes(stations)
# for r in routes:
#    print(r)

counter = 1

for r in routes:
    open_route_service.get_probable_route_and_time(r)

    proper_records_number = database_service.get_number_of_proper_records(r)

    route_points_list = r.get_route_points_list()

    # print(route_points_list)

    for single_point in route_points_list:
        if single_point in points:
            points[single_point] += proper_records_number
        else:
            points[single_point] = proper_records_number
            Point.number_of_all_registered_points += 1

    counter = counter + 1
    print(counter)
    print(len(points))
    print(".")
    # print(", ")

# tuples = database_service.convert_points_dict_to_tuples_list(points)
# print(tuples)
database_service.save_points_in_database(points)