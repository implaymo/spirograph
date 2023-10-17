import turtle
from turtle import Turtle, Screen
from random import randint

tim = Turtle()
turtle.colormode(255)
turtle.bgcolor("black")
tim.speed(100)
angle = 10

while tim.heading() != angle:
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    tim.circle(100)
    tim.right(angle)


screen = Screen()
screen.exitonclick()