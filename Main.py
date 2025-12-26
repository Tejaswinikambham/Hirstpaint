color_list=[(253, 253, 251), (243, 252, 249), (253, 245, 250), (236, 245, 251), (215, 151, 110), (30, 104, 179), (163, 81, 44), (180, 12, 33), (116, 170, 208), (216, 131, 160), (238, 222, 101), (158, 58, 97), (223, 65, 98), (223, 80, 52), (73, 24, 11), (18, 51, 149), (126, 183, 141), (169, 149, 31), (16, 170, 206), (47, 185, 138), (153, 25, 16), (236, 169, 159), (232, 165, 182), (135, 228, 190), (39, 130, 83)]
import turtle
turtle.colormode(255)
import random
tim=turtle.Turtle()
my_Screen=turtle.Screen()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.goto(-225, -225)
tim.pendown()

for j in range(10):

    for i in range(10):

        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()

        if i == 9 and j % 2 == 0:
            tim.left(90)
            tim.penup()
            tim.forward(50)
            tim.pendown()
            tim.left(90)

        if i == 9 and j % 2 == 1:
            tim.right(90)
            tim.penup()
            tim.forward(50)
            tim.pendown()
            tim.right(90)


my_Screen.exitonclick()







