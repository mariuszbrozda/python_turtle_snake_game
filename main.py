import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from game_level import GameLevel
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
game_level = GameLevel()


screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right,'Right')


game_is_on = True



while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.inscrease_score()
        snake.extend_snake_body()

        # Increase snake speed by 1 every 5 points
        if scoreboard.score % 5 == 0:
            game_level.level_up()
            snake.speed_up_snake()


    # Detect collision with walls
    if snake.head.xcor() > 430 or snake.head.xcor() < -430 or snake.head.ycor() > 430 or snake.head.ycor() < -430:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with snake's tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False












screen.exitonclick()
