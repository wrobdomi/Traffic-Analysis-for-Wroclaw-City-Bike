import csv

class Station:

    # latitude - szerokosc
    # longitude - dlugosc
    def __init__(self, id_number, latitude, longitude, station_name):
        self.id_number = id_number
        self.latitude = latitude
        self.longitude = longitude
        self.station_name = station_name

    def __repr__(self):
        return "Station {}: {} Coords: ( {}, {} )"\
            .format(self.id_number, self.station_name, self.latitude, self.longitude)

    @classmethod
    def load_stations_from_file(cls, filename):
        stations_arr = []
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for line in reader:
                stations_arr.append(cls(int(line[0]), float(line[1]), float(line[2]), line[3]))
            return stations_arr
