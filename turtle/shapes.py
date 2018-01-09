#regular shapes 1.1,2.3
def square(s,jon,r,g,b):
    for i in range(4):
        jon.forward(s)
        jon.left(90)
        jon.color(r,g,b)    
        r = r - 50
        g = g + 50
        b = b - 20


def triangle(s):
    for i in range(3):
        turtle.forward(s)
        turtle.left(120)

def pentagon(s):
    for i in range(5):
        turtle.forward(s)
        turtle.left(72)

def hexagon(s):
    for i in range(6):
        turtle.forward(s)
        turtle.left(60)

def nonagon(s):
    for i in range(9):
        turtle.forward(s)
        turtle.left(40)


def decagon(s):
    for i in range(10):
        turtle.forward(s)
        turtle.left(36)

#anyregpoly 1.4
import turtle

n = int(input('Hello, Give me a number and I will make a polygon with that many sides '))
print ('Alright,your polygon will have ' + str(n)+  ' side')
l = int(input('How long do you want you side to be?'))
angle = n - 2
anglel = angle * 180
anyangle = 180 - (anglel/n)

wn = turtle.Screen()
wn.colormode(255)
turtl = turtle.Turtle('turtle')
            
def AnyRegPoly(n,r,g,b,):
    for i in range(n):
        turtl.forward(l)
        turtl.left(anyangle)
        turtl.color(r,g,b)
        turtl.stamp()
        r = r - 5
        g = g + 10
        b = b - 20

AnyRegPoly(n,240,50,230)
    


