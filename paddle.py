from turtle import Turtle


UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, starting_positions):
        super().__init__()
        self.starting_positions = starting_positions
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("White")
        self.goto(self.starting_positions)
        self.y_move = 10

    def up(self):
        new_ycor = self.ycor() + self.y_move
        self.goto(self.xcor(), new_ycor)

    def down(self):
        new_ycor = self.ycor() + self.y_move * -1
        self.goto(self.xcor(), new_ycor)
