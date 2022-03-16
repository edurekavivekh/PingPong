import time
from turtle import Screen
from paddle import *


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
right_paddle_positions = [(290, 0), (290, 0), (290, 0)]
left_paddle_positions = [(-290, 0), (-290, 0), (-290, 0)]

right_paddle = Paddle(right_paddle_positions)
left_paddle = Paddle(left_paddle_positions)

is_running = True

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.up)
screen.onkeypress(key="Down", fun=right_paddle.down)
screen.onkeypress(key="q", fun=left_paddle.up)
screen.onkeypress(key="w", fun=left_paddle.down)

while is_running:

    screen.update()
    time.sleep(0.05)


screen.exitonclick()
