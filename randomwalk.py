import turtle
from turtle import Turtle, Screen
from random import randint

tim = Turtle()


def random_color():
    turtle.colormode(255)
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))


def random_turn():
    random_number = randint(-1, 1)
    if random_number == -1:
        random_color()
        tim.left(90)
    elif random_number == 0:
        random_color()
        tim.right(90)
    else:
        random_color()
        tim.right(360)


def random_straight():
    random_number = randint(0,1)
    if random_number == 0:
        random_color()
        tim.forward(10)
    else:
        random_color()
        tim.back(10)


tim.speed(100)
turtle.screensize(400, 400, "black")


game = True
while game:
    tim.pensize(10)
    random_turn()
    random_straight()

screen = Screen()
screen.exitonclick()