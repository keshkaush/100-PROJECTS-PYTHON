from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.STARTING_MOVE_DISTANCE = 5
        self.all_cars = []

    def new_car(self):
        chance = random.randint(1, 6)
        if chance == 3:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            y_cor = random.randint(-250, 250)
            car.goto(300, y_cor)
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.STARTING_MOVE_DISTANCE)

    def update_speed(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT








