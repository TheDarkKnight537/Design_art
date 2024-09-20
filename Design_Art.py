# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('/Users/batman/Documents/100 days of hardworking/pythonProject/jen.jpg', 30)
#
# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# lst = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     lst.append(new_color) # e.g. (255, 151, 210)
# print(lst)

import turtle as td
import random as rd

tim = td.Turtle()
td.colormode(255)
tim.speed("fast")
tim.penup()
tim.hideturtle()
color_list = [(207, 159, 82), (54, 89, 130), (146, 91, 39), (140, 26, 48), (222, 207, 104), (132, 177, 203), (158, 46, 83), (45, 55, 104), (170, 160, 39), (129, 189, 143), (83, 20, 44), (36, 43, 69), (186, 94, 106), (186, 140, 172), (84, 120, 180), (60, 39, 31), (88, 157, 92), (78, 153, 164), (195, 78, 72), (45, 74, 78), (80, 74, 44), (162, 201, 218), (58, 126, 122), (218, 176, 187), (169, 207, 170), (220, 181, 168)]
tim.setheading(135)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, rd.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        # tim.setheading(270)
        # tim.forward(50)
        # tim.setheading(180)
        # tim.forward(500)
        # tim.setheading(0)
        tim.setheading(185.710593137)
        tim.forward(502.493781056)
        tim.setheading(0)

screen = td.Screen()
screen.exitonclick()