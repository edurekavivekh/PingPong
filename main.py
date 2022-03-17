import time
from turtle import Screen
from paddle import *
from ball import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
right_paddle_positions = (280, 0)
left_paddle_positions = (-290, 0)
ball_starting_positions = [0, 0]

right_paddle = Paddle(right_paddle_positions)
left_paddle = Paddle(left_paddle_positions)
ball = Ball()


is_running = True

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.up)
screen.onkeypress(key="Down", fun=right_paddle.down)
screen.onkeypress(key="Left", fun=left_paddle.up)
screen.onkeypress(key="Right", fun=left_paddle.down)

while is_running:

    screen.update()
    time.sleep(0.01)
    ball.move()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    if (ball.distance(right_paddle) < 30 and ball.xcor() > 200) or (ball.distance(left_paddle) < 30 and ball.xcor() < -200):
        ball.bounce_x()

screen.exitonclick()
