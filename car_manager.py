from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.level = [6, 5, 4, 3]
        self.initial_level = 0

    def create_car(self):

        # Random chance is used to reduce the no. of cars created in a time, this makes the while loop run 1/5th time
        random_chance = random.randint(1, self.level[self.initial_level])
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape(random.choice(["car1.gif" , "car2.gif" , "car3.gif"]))
            random_y = random.randint(-250, 250)
            new_car.goto(340, random_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        if self.initial_level < 3:
            self.initial_level += 1



