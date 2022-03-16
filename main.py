import time
from turtle import Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

is_running = True

screen.listen()

while is_running:

    screen.update()
    time.sleep(0.1)


screen.exitonclick()
