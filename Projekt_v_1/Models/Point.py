class Point:

    number_of_all_registered_points = 0

    # latitude - szerokosc
    # longitude - dlugosc
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return "Point ({}, {})".format(self.latitude, self.longitude)

    def __eq__(self, other):
        return (
            self.longitude == other.longitude and
            self.latitude == other.latitude
        )

    def __hash__(self):
        return hash(str(self))



# Points playground
# pointOne = Point(17.045083,51.1004)
# pointTwo = Point(17.030175,51.109782)
# pointThree = Point(17.048102,51.104571)
#
# anotherPointOne = Point(17.045083,51.1004)
# anotherPointThree = Point(17.048102,51.104571)
#
# print(pointOne.__hash__())
# print(pointTwo.__hash__())
# print(pointThree.__hash__())
#
# print(anotherPointOne.__hash__())
# print(anotherPointThree.__hash__())
#
# points[pointOne] = 10
# points[pointTwo] = 20
# points[pointThree] = 60
#
# print(points)
#
# points[anotherPointOne] = 70
#
# print(points)
#
# print(anotherPointThree in points)
# print(anotherPointOne in points)
