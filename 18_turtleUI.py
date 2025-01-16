# import turtle as t
# import random
# import heroes
# import colorgram

# # rinat = t.Turtle()
# # t.colormode(255)
# # # colors = ["green yellow", "deep pink", "purple", "green", "black", "yellow"]

# # rinat.shape("circle")
# # rinat.shapesize(stretch_wid=1, stretch_len=1)

# # # def draw_shape(side_size):
# # #     angle = 360 / side_size
# # #     rinat.color(random.choice(colors))
# # #     for _ in range(side_size):
# # #         rinat.forward(100)
# # #         rinat.left(angle)
# # # for shape_side in range(3, 11):
# # #     draw_shape(shape_side)
# # steps = [0, 0.25, 0.5, 0.75]

# # # for _ in range(100):
# # #     r = random.randint(1,255)
# # #     g = random.randint(1,255)
# # #     b = random.randint(1,255)
# # #     my_tuple = (r, g, b)
# # #     rinat.color(my_tuple)
# # #     rinat.pensize(10)

# # #     angle = int(random.choice(steps) * 360)
# # #     rinat.setheading(angle)
# # #     rinat.fd(20)


# # # # for step in range(10):
# # # #     # x = 30 * step * 2
# # # #     # rinat.forward(30)
# # # #     # rinat.teleport(x)
# # # #     # rinat.pos()
# # # #     rinat.forward(10)
# # # #     rinat.penup()
# # # #     rinat.forward(10)
# # # #     rinat.pendown()

# # def rand_color():
# #     r = random.randint(0,255)
# #     g = random.randint(0,255)
# #     b = random.randint(0,255)
# #     color = (r, g, b)
# #     return color
# # gap_size = 15
# # rinat.speed("fastest")
# # def draw_sparagraph(gap_size):
# #     for _ in range(360//gap_size):
# #         rinat.color(rand_color())
# #         rinat.circle(100)
# #         rinat.setheading(rinat.heading() + gap_size)
        
# # draw_sparagraph(5)
    
# # rgb_colors = []   
# # colors40 = colorgram.extract('colors.webp', 30)

# # for color in colors40:
# #     r = color.rgb.r
# #     g = color.rgb.g
# #     b = color.rgb.b
# #     rgb_colors.append((r, g, b))
# # print(rgb_colors)


# color_list = [(194, 159, 126), (18, 103, 149), (144, 75, 93), (233, 237, 234), (134, 93, 77), (129, 157, 176), (221, 227, 233), (193, 150, 159), (4, 65, 99), (207, 180, 187), (148, 167, 163), (189, 93, 76), (217, 193, 154), (66, 119, 89), (170, 139, 52), (5, 94, 82), (3, 88, 104), (22, 67, 116), (70, 47, 45), (2, 69, 64), (72, 38, 42), (176, 85, 106), (87, 52, 79), (78, 56, 55), (88, 143, 121), (102, 128, 162), (204, 186, 182), (69, 145, 166)]

# rinat = t.Turtle()

# rinat.shape("circle")

# rinat.shapesize(stretch_wid=1, stretch_len=1)
# rinat.color(random.choice(color_list))

# t.exitonclick()

import turtle as t
import random

# Преобразование RGB в HEX
def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

# Список цветов
color_list = [
    (194, 159, 126), (18, 103, 149), (144, 75, 93), (233, 237, 234), 
    (134, 93, 77), (129, 157, 176), (221, 227, 233), (193, 150, 159), 
    (4, 65, 99), (207, 180, 187), (148, 167, 163), (189, 93, 76), 
    (217, 193, 154), (66, 119, 89), (170, 139, 52), (5, 94, 82), 
    (3, 88, 104), (22, 67, 116), (70, 47, 45), (2, 69, 64), 
    (72, 38, 42), (176, 85, 106), (87, 52, 79), (78, 56, 55), 
    (88, 143, 121), (102, 128, 162), (204, 186, 182), (69, 145, 166)
]

color_list_hex = [rgb_to_hex(color) for color in color_list]


t.colormode(255)


rinat = t.Turtle()
# rinat.shape("circle")
# rinat.shapesize(stretch_wid=1, stretch_len=1)

rinat.penup()
rinat.hideturtle()
rinat.setheading(225)
rinat.fd(300)
rinat.setheading(0)
for _ in range(10):  
    for _ in range(10):  
        # rinat.color(random.choice(color_list_hex))
        rinat.dot(20, random.choice(color_list_hex))  
        rinat.forward(50)
    rinat.setheading(90)
    rinat.forward(50)
    rinat.setheading(180)
    rinat.forward(500)
    rinat.setheading(0)

# Ожидание клика для выхода
t.exitonclick()


        



# Выбор случайного цвета из списка


# Задержка для закрытия окна кликом
t.exitonclick()
