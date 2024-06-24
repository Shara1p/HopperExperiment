import numpy as np


class Coordinates:

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, coords):
        self.__x = coords

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, coords):
        self.__y = coords

    def __init__(self, mean=0, std_dev=1, num_samples=50):
        self.x = np.array([])
        self.y = np.array([])
        self.generate_coord(mean, std_dev, num_samples)

    def generate_coord(self, mean=0, std_dev=1, num_samples=50):
        random_x = np.random.normal(mean, std_dev, num_samples)
        random_y = np.random.normal(mean, std_dev, num_samples)

        self.x = random_x
        self.y = random_y
