from turtle import *
import turtle
from termina import termina
speed(1)
color('lime')
bgcolor('black')
grandezza = int(input('grandezza del quadrato --> '))
turtle.pu()
right(90)
forward(grandezza / 2)
left(90)
forward(grandezza / 2)
turtle.pd()
for x in range(4):
	left(90)
	forward(grandezza)
termina()