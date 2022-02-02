from turtle import Turtle, Screen

screen = Screen()
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


game_is_on = True

while game_is_on:
    for seg in segments:
        seg.forward(20)















screen.exitonclick()
