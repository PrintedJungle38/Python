from turtle import *
from termina import termina
speed(100)
color('cyan')
bgcolor('black')
b = 200
while b > 0:
	left(b)
	forward(b * 3)
	b -= 1
termina()