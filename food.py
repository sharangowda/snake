import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(0.5,0.5)
        self.color('white')
        self.speed('fastest')
        x_cor = random.randint(-270,270)
        y_cor = random.randint(-270,270)
        self.goto(x_cor,y_cor)

    def respawn(self):
        x_cor = random.randint(-270,270)
        y_cor = random.randint(-270,270)
        self.goto(x_cor,y_cor)