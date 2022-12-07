from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.show_food()

    def show_food(self):
        self.goto(random.randint(-260, 260), random.randint(-260, 260))