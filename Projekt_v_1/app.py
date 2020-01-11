from Models.Station import Station
from Models.Route import Route
from Service.OpenRouteService import  OpenRouteService

# data  structures
stations = []
routes = []
points = []

# services
open_route_service = OpenRouteService()

# stations set up
stations_source_file = "../Data/input_stations.csv"
stations = Station.load_stations_from_file(stations_source_file)
# for s in stations:
#    print(s)

# routes set up
routes = Route.create_routes(stations)
# for r in routes:
#    print(r)


# for r in routes:
#     print(open_route_service.create_query(r.from_station_latitude,
#                                           r.from_station_longitude,
#                                           r.to_station_latitude,
#                                           r.to_station_longitude))

# for every route:
open_route_service.getProbableRouteAndTime(routes[0])


