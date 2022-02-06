import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.listen()


screen.setup(900, 900)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)


# CREATE SNAKE BODY
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right,'Right')


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with wall
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.inscrease_score()
        snake.extend_snake_body()
    if snake.head.xcor() > 430 or snake.head.xcor() < -430 or snake.head.ycor() > 430 or snake.head.ycor() < -430:
        scoreboard.game_over()
        game_is_on = False












screen.exitonclick()
