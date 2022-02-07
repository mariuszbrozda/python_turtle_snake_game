
from turtle import Turtle
from scoreboard import Scoreboard


ALIGNMENT ='center'
FONT = ('Courier', 24, 'normal')



class GameLevel(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.level = 1
        self.penup()
        self.goto(250, 380)
        self.hideturtle()
        self.write(f'Level: {self.level}', align=ALIGNMENT, font=FONT)


    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', align=ALIGNMENT, font=FONT)

