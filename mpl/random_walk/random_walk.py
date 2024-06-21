# Simulate random walk of n molecular
from random import choice

# class produce random walk
class RandomWalk:
    def __init__(self, num_points = 5000):
        self.num_points = num_points
        # set the start point of all random walk
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # calculate all points in the random walk
        while len(self.x_values) < self.num_points:
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
            