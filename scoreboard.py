
from turtle import Turtle

ALIGNMENT ='center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 380)
        self.hideturtle()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def inscrease_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))

