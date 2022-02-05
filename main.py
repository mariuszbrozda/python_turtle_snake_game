import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.listen()
screen.setup(600, 600)
screen.bgcolor('grey')
screen.title('Snake')
screen.tracer(0)


# CREATE SNAKE BODY
snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()












screen.exitonclick()
