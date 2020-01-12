import time
import requests

class OpenRouteService:

    def __init__(self):
        self.api_key = "5b3ce3597851110001cf6248782ac85e6e35409582ad067fef1ded89"
        self.base_url = "https://api.openrouteservice.org/v2/directions/cycling-regular?api_key="

    def create_query(self, from_latitude, from_longitude, to_latitude, to_longitude):
        query = self.base_url + self.api_key + \
                "&start=" + str(from_latitude) + "," + str(from_longitude) + \
                "&end=" + str(to_latitude) + "," + str(to_longitude)
        return query


    def get_probable_route_and_time(self, route):

        query = self.create_query(route.from_station_latitude,
                                  route.from_station_longitude,
                                  route.to_station_latitude,
                                  route.to_station_longitude)

        # print(query)

        # get the data from API
        r = requests.get(query)

        # print JSON response
        # print(r.json())

        json_response = r.json()

        # set data to route
        points_array = json_response['features'][0]['geometry']['coordinates']
        route.route_points = points_array
        # print(points_array)

        expected_time_seconds = json_response['features'][0]['properties']['summary']['duration']
        route.expected_time = expected_time_seconds
        # print(expected_time_seconds)

        # 40 request per minute is max
        time.sleep(2)





    # def __repr__(self):
    #     return "Route from {} to {} Coords: ( {}, {} ) -> ( {}, {} )"\
    #         .format(self.from_station_name, self.to_station_name,
    #                 self.from_station_latitude, self.from_station_longitude,
    #                 self.to_station_latitude, self.to_station_longitude)




