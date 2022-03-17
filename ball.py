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
        self.x_move = 2
        self.y_move = 4

    def move(self):
        x_cur = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        if self.xcor() > 290 or self.xcor() < -290:
            self.goto(0, 0)
        else:
            self.goto(x_cur, y_cor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
