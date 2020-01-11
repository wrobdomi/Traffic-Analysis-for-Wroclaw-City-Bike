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



    # def add_movie(self, name, genre):
    #     movie = Movie(name, genre, False)
    #     self.movies.append(movie)
    #
    # def delete_movie(self, name):
    #     self.movies = list(filter(lambda movie: movie.name != name, self.movies))
    #
    # def watched_movies(self):
    #     movies_watched = list(filter(lambda x: x.watched, self.movies))
    #     return movies_watched
    #
    # def save_to_file(self):
    #     with open("{}.txt".format(self.name), 'w') as f:
    #         f.write(self.name + "\n")
    #         for movie in self.movies:
    #             f.write("{},{},{}\n".format(movie.name, movie.genre, str(movie.watched)))
    #
    # @classmethod
    # def load_from_file(cls, filename):
    #     with open(filename, 'r') as f:
    #         content = f.readlines()
    #         username = content[0]
    #         movies = []
    #         for line in content[1:]:
    #             movie_data = line.split(",") # [name, genre, watched]
    #             movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == "True"))
    #
    #         user = cls(username)
    #         user.movies = movies
    #         return user