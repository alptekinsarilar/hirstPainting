# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     rgb = color.rgb
#     rgb_tuple = (rgb[0], rgb[1], rgb[2])
#     rgb_colors.append(rgb_tuple)
#
# print(rgb_colors)
import turtle as t
import random

color_list = [(240, 230, 68), (182, 19, 42), (219, 238, 244), (187, 74, 36), (251, 230, 235), (18, 139, 86), (114, 180, 206), (25, 120, 166), (190, 179, 23), (218, 61, 97), (206, 164, 91), (27, 39, 74), (76, 173, 98), (176, 46, 64), (38, 44, 112), (238, 232, 3), (18, 164, 211), (216, 133, 155), (212, 72, 54), (126, 184, 127), (8, 55, 37), (12, 93, 55), (236, 157, 177), (165, 29, 26), (148, 209, 221), (8, 86, 109), (161, 210, 186), (234, 172, 164)]

t.colormode(255)
tim = t.Turtle()
tim.shape("circle")
tim.hideturtle()
tim.up()
tim.goto(-100, -100)
tim.showturtle()
for _ in range(10):
    tim.color(random.choice(color_list))
    tim.down()
    tim.stamp()
    tim.penup()
    tim.forward(50)


screen = t.Screen()
screen.exitonclick()
