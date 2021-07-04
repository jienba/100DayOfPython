import random
import turtle
from turtle import Turtle, Screen
import random
import heroes

jack = Turtle()
# jack.shape('turtle')
# jack.color('red')
# for _ in range(4):
#     jack.forward(200)
#     jack.left(90)

# print(heroes.gen())
# jack.speed(1)
# for _ in range(10):
#     jack.forward(20)
#     jack.penup()
#     jack.forward(20)
#     jack.pendown()
screen = Screen()
# screen.colormode(255)
turtle.colormode(255)


# Challenge 3

#
# jack.speed(1)
#
#
# My own
# def random_color():
#     color = r.randint(0, 255)
#     return color

# Angela version

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


print(random_color())
# Challenge 3
#
# for i in range(3, 10):
#     R = random_color()
#     G = random_color()
#     B = random_color()
#     jack.color(R, G, B)
#     for j in range(i):
#         jack.forward(150)
#         jack.right(360 / i)


# Challenge 4
# directions = [0, 90, 180, 270]
# jack.pensize(15)
# jack.speed("fastest")
#
# for _ in range(500):
#     jack.color(random_color())
#     jack.setheading(random.choice(directions))
#     jack.fd(25)
jack.pensize(3)
jack.speed("fastest")


def draw_spirograph(angle, circle_radius):
    number_of_tours = int(360 / angle)
    for _ in range(number_of_tours):
        jack.color(random_color())
        jack.circle(circle_radius)
        jack.left(angle)


draw_spirograph(10, 100)
screen.exitonclick()
