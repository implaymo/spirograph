import turtle
from turtle import Turtle, Screen
from random import randint

tim = Turtle()

number_of_sides = 2
# Loop to create every shape
while number_of_sides < 10:
    number_of_sides += 1
    angle = 360 / number_of_sides
    # Gets different colors for every shape
    turtle.colormode(255)
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    for _ in range(number_of_sides):
        tim.right(angle)
        tim.forward(100)

# Keeps screen open till user clicks with mouse
screen = Screen()
screen.exitonclick()