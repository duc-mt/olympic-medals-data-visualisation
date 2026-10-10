"""
==============================================================================
Module Name:   drawing_functions.py
Description:   Source module drawing_functions.py.
Author:        Mai Tan Duc <ducmai.network@gmail.com>
Created:       2026-10-10
Version:       1.0.0
License:       MIT
==============================================================================
Usage:         python3 drawing_functions.py [options]
Notes:         Requires Python 3.8+
==============================================================================
"""

#!/usr/bin/python3
import turtle


# ---------------------------- Function Definitions ---------------------------
def set_turtle(animal, pencolour, fillcolour):
    animal.shape("turtle")
    animal.color(pencolour, fillcolour)
    animal.speed(0)


def move_turtle(animal, x, y):
    animal.pu()
    animal.goto(x, y)
    animal.pd()


def segment(pie, degree):
    pie.begin_fill()
    pie.lt(180)
    pie.fd(230)
    pie.lt(90)
    pie.circle(230, degree)
    pie.lt(90)
    pie.fd(230)
    pie.end_fill()


def label(x, y, percentage):
    label = turtle.Turtle()
    set_turtle(label, "black", "black")
    label.pensize = 0
    label.begin_fill()
    move_turtle(label, x, y)
    # Create a border around the percentage
    if len(percentage) < 3:
        a = 29
    else:  # For cases where it is greater than 9%
        a = 45
    for _ in range(2):
        label.fd(a)
        label.lt(90)
        label.fd(35)
        label.lt(90)
    label.lt(-90)
    label.end_fill()
    label.hideturtle()
    label.fd(-2)
    label.lt(90)
    label.color("white")
    label.write(percentage, font=("Courier", 20))


def country(colour, y2, name):
    country = turtle.Turtle()
    set_turtle(country, colour, colour)
    move_turtle(country, 190, y2)
    country.begin_fill()
    for i in range(4):
        country.fd(10)
        country.lt(-90)
    country.end_fill()
    move_turtle(country, 215, y2 - 15)
    country.color("black")
    country.write(name, font=("Courier", 15))
    country.hideturtle()
