import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

for shape in ["pikachu.gif", "car1.gif", "car2.gif", "car3.gif"]:
    try:
        screen.register_shape(shape)
    except:
        print(f"Warning: {shape} not found!")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_right, "Right")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    car_manager.cleanup_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 30:  
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
