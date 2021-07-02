import random
from turtle import Turtle, Screen
import random as r
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
screen.colormode(255)


# Challenge 3

#
# jack.speed(1)
#
#
def random_color():
    color = r.randint(0, 255)
    return color


#
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
directions = [0, 90, 180, 270]
jack.pensize(15)
jack.speed("fastest")

for _ in range(1500):
    R = random_color()
    G = random_color()
    B = random_color()
    jack.color(R, G, B)
    jack.setheading(random.choice(directions))
    jack.fd(25)

screen.exitonclick()
