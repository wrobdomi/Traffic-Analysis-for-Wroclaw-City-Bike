class Route:

    # latitude - szerokosc
    # longitude - dlugosc
    def __init__(self,
                 from_station_name, to_station_name,
                 from_station_latitude, from_station_longitude,
                 to_station_latitude, to_station_longitude
                 ):
        self.from_station_name = from_station_name
        self.to_station_name = to_station_name
        self.from_station_latitude = from_station_latitude
        self.from_station_longitude = from_station_longitude
        self.to_station_latitude = to_station_latitude
        self.to_station_longitude = to_station_longitude
        self.expected_time = 0
        self.route_points = []

    def __repr__(self):
        return "Route from {} to {} Coords: ( {}, {} ) -> ( {}, {} )"\
            .format(self.from_station_name, self.to_station_name,
                    self.from_station_latitude, self.from_station_longitude,
                    self.to_station_latitude, self.to_station_longitude)

    @classmethod
    def create_routes(cls, stations):
        print("Hello")
        routes_arr = []
        for i, s1 in enumerate(stations):
            print("1")
            for j, s2 in enumerate(stations):
                if i == j:
                    continue
                routes_arr.append(cls(
                    s1.station_name, s2.station_name,
                    s1.latitude, s1.longitude,
                    s2.latitude, s2.longitude))
        return routes_arr
