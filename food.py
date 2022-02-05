
from turtle import Turtle,Screen
import random

screen = Screen()

food = Turtle(shape='square')


class FoodClass:

    def __init__(self):
        self.food = food.dot(10)

    def show_food(self, food_x_pos, food_y_pos):
        food_x_pos = random.randint(0, 290)
        food_y_pos = random.randint(0, 290)
        self.food.goto(food_x_pos, food_x_pos)



food_class = FoodClass()

for meal in range(4):
    food_class.show_food()


screen.exitonclick()