import math
import turtle

def square(t,l):
    for i in range(4):
        t.fd(l)
        t.lt(90)

def polygon(t,l,n,a):
    angle = a/n
    for i in range(n):
        t.fd(l)
        t.lt(angle)

def circle(t,r,a=360):
    nn = 360/a
    c = 2*math.pi*r
    n = 50
    l = c/(n*nn)
    polygon(t, l, n, a)


bob = turtle.Turtle()

circle(bob,100, 180)
turtle.mainloop()