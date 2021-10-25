import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

current_player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(current_player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.new_car()
    car_manager.move_car()

    #Detect collision with wall
    if current_player.ycor() >= 290:
        scoreboard.update_level()
        car_manager.update_speed()
        current_player.reset_position()

    #detect collision with cars
    for car in car_manager.all_cars:
        if current_player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
