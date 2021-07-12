import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.up,"Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
        if car.xcor() < -310:
            car_manager.all_cars.remove(car)
    if player.ycor() > 250:
        player.reset()
        scoreboard.increase_score()
        car_manager.levelup()
    

screen.exitonclick()