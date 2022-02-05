
from turtle import Turtle, Screen

starting_positions = [ (0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self,):
        self.segments = []


        for position in starting_positions:
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
        self.segments[0].forward(20)