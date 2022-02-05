import time
from turtle import Turtle, Screen

screen = Screen()
screen.listen()
screen.setup(600, 600)
screen.bgcolor('grey')
screen.title('Snake')
screen.tracer(0)


# CREATE SNAKE BODY
y = 0

starting_positions = [ (0, 0), (-20, 0), (-40, 0)]

segments = []
for position in starting_positions:
    segment = Turtle('square')
    segment.pensize(20)
    segment.color('white')
    segment.penup()
    segment.goto(position)
    segments.append(segment)



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seq_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seq_num - 1].xcor()
        new_y = segments[seq_num - 1].ycor()
        segments[seq_num].goto(new_x, new_y)
    segments[0].forward(20)










screen.exitonclick()
