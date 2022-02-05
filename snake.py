
from turtle import Turtle, Screen

STARTING_POSITIONS = [ (0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self,):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle('square')
            segment.pensize(20)
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)


    def move(self):
        for seq_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seq_num - 1].xcor()
            new_y = self.segments[seq_num - 1].ycor()
            self.segments[seq_num].goto(new_x, new_y)
        self.segments[0].color('green')
        self.segments[0].forward(MOVE_DISTANCE)