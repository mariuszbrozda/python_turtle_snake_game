
from turtle import Turtle, Screen
import random

screen = Screen()


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        rand_x_pos = random.randint(-280, 280)
        rand_y_pos = random.randint(-280, 280)
        self.goto(rand_x_pos, rand_y_pos)




