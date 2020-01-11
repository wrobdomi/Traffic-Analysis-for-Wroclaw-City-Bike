from Models.Station import Station
from Models.Route import Route

stations = []
routes = []
points = []

# stations set up
stations_source_file = "../Data/input_stations.csv"
stations = Station.load_stations_from_file(stations_source_file)
for s in stations:
    print(s)

# routes set up
routes = Route.create_routes(stations)
for r in routes:
    print(r)






