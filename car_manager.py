from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1,6) == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_len=1.5, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(280,random.randint(-240,240))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            x_pos = car.xcor() - self.car_speed
            car.setpos(x_pos,car.ycor())

    def levelup(self):
        self.car_speed += MOVE_INCREMENT