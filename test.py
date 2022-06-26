import turtle as t
import random

kachua = t.Turtle("turtle")
screen = t.Screen()


# t.listen(xdummy=None, ydummy=None)


def forward():
    kachua.fd(50)


def no_line_f():
    kachua.penup()
    kachua.fd(50)
    kachua.pendown()


def left():
    kachua.left(10)


def right():
    kachua.right(10)


def backward():
    kachua.backward(50)


def semi_circle_anti():
    kachua.circle(-25, 180)


def semi_circle():
    kachua.circle(25, 180)


def clear():
    kachua.clear()


screen.onkeypress(forward, "w")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")
screen.onkeypress(backward, "s")
screen.onkeypress(semi_circle_anti, "o")
screen.onkeypress(semi_circle, "p")
screen.onkeypress(no_line_f, "space")
screen.onkeypress(clear, "c")
screen.listen()

screen.exitonclick()
