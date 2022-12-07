from turtle import Turtle
DISTANCE = 560


class Game_Env(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 280)
        self.color("white")
        self.pendown()

    def draw_walls(self):
        for i in range(4):
            self.forward(DISTANCE)
            self.right(90)