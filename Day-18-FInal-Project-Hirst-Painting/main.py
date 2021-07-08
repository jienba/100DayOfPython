import random
import colorgram
from turtle import Turtle, Screen

# def extract_rgb_color(path_image, number_of_colours):
#     colours = colorgram.extract(path_image, number_of_colours)
#     colours_rgb = []
#     for colour in colours:
#         red = colour.rgb.r
#         green = colour.rgb.g
#         blue = colour.rgb.b
#         color = (red, green, blue)
#         colours_rgb.append(color)
#     return colours_rgb
#
#
# print(extract_rgb_color('paint.jpg', 10))
screen = Screen()
jack = Turtle()
screen.colormode(255)

rgb_colors = [(246, 242, 235), (247, 240, 244), (239, 242, 247), (237, 245, 240), (212, 149, 95), (215, 80, 62),
              (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40)]

jack.hideturtle()
# down-left corner
jack.penup()
x = -300
y = -250
jack.goto(x, y)


# the ten dots
def draw_hist_paint():
    for _ in range(10):
        jack.dot(30, random.choice(rgb_colors))
        jack.penup()
        jack.forward(60)


for _ in range(10):
    draw_hist_paint()
    y += 50
    jack.goto(x, y)

screen.exitonclick()
