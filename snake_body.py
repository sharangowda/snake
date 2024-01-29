from turtle import Turtle, position
import turtle as t

SNAKE = [t.Turtle('square') for turt in range(3)]
DISTANCE = 20


class Snake():
    def __init__(self) -> None:
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for body in SNAKE:
            self.add_segment(position)



    def add_segment(self,position):
        x = 0
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        x = x - 20
        new_segment.goto(x, 0)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())
        

    def move(self):
        for seg_num in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[seg_num-1].xcor()
            new_y = self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
