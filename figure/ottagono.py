from turtle import *
from termina import termina
speed(1)
color('lime')
bgcolor('black')
grandezza = int(input('grandezza dell\'ottagono --> '))
for x in range(8):
	left(45)
	forward(grandezza)
termina()