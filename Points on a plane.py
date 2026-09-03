import math

class Point: # classes can contain several functions, as well as many other types of code
    def __init__(self, x=0.0, y=0.0): # init initializes, creating the object it is written to make
        self.__x = x # self creates the object
        self.__y = y # the self is the class itself, creating it and the __ makes it hidden. they will only exist inside the class, this is standard, so as to prevent overlapping by calling the class instead of calling variables of the same name, for example

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x -x)) # hypot is a math/algebra thing

    def distance_from_point(self, point):
        return self.distance_from_point(point.getx(), point.gety())

point1 = Point(0, 0) # classes allow you to also make multiple copies of each other, who are independant from each other
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))