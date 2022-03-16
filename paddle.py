from turtle import Turtle


UP = 90
DOWN = 270


class Paddle:
    def __init__(self, starting_positions):
        self.segments = []
        self.starting_positions = starting_positions
        self.create_paddle()

    def create_paddle(self):
        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.turtlesize(2, 5)
        segment.penup()
        segment.color("White")
        segment.goto(position)
        segment.setheading(UP)
        self.segments.append(segment)

    def up(self):
        for seg_num in range(0, 3):
            self.segments[seg_num].setheading(UP)
            self.segments[seg_num].forward(10)

    def down(self):
        for seg_num in range(0, 3):
            self.segments[seg_num].setheading(DOWN)
            self.segments[seg_num].forward(10)
