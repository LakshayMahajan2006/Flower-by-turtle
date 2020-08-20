# Flower-by-turtle
#importing packages
import turtle
import math
import random

#Setting a screen
wn = turtle.Screen()
wn.title("By Lakshay Mahajan")

#Flower

lakshay = turtle.Turtle()
lakshay.color("red", "yellow")
lakshay.speed(10)

lakshay.begin_fill()
for i in range(108):
    lakshay.forward(200)
    lakshay.left(170)

lakshay.end_fill()



turtle.done()
