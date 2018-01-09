#3.3,4,5,and 6
import turtle
turt = turtle.Turtle('turtle')

def shapes(s,n,turt):
    turt.pu()
    turt.goto(-s/2,s/2)
    turt.pd()
    for i in range(n):

        turt.forward(s)
        turt.right(360/n)

turt.speed(0)
for i in range(2,200,8):

    shapes(i, 4, turt)


#3.1,2
from shapes import *
import turtle


wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor(15,40,34)

jon = turtle.Turtle('turtle')
jon.color(0,0,255)
jon.speed(2)

square(150,jon,235,20,220)



               
