from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.turtlesize(1, 1)
        self.penup()
        self.color("White")
        self.speed("fastest")
        self.goto(0, 0)

    def move_left(self):
        self.setheading(180)
        self.forward(5)

    def move_right(self):
        self.setheading(0)
        self.forward(5)
