import random

class Car:

    top_acceleration = 5
    top_speed = 10

    current_acceleration = 0
    current_speed = 0

    position = 1
    force = 0

    def __init__(self):
        print("car created")

    def sense(self):
        sensor_input = self.position + (random.randrange(-20, 20) / 1000)
        return sensor_input

    def drive(self, force):
        self.force = force
        self.current_acceleration = self.top_acceleration * (force / 100)
        self.current_speed += self.current_acceleration
        if (self.current_speed > self.top_speed): self.current_speed = self.top_speed
        self.position += self.current_speed
