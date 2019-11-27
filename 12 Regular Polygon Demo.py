#Regular Polygon Demo

import turtle

window = turtle.Screen()
wolfgang = turtle.Turtle()
wolfgang.speed(0)

franz = turtle.Turtle()
franz.color("Red")
franz.up()
franz.goto(150,0)
franz.down()

def tri(a_turtle, side_length):
    for i in range(3):
        a_turtle.fd(side_length)
        a_turtle.left(120)

def pentagon(a_turtle, side_length):
    for i in range(5):
        a_turtle.fd(side_length)
        a_turtle.left(72)


def skinny_rectangle(a_turtle ,size):
    for i in range(2):
        a_turtle.fd(size*2)
        a_turtle.left(90)
        a_turtle.fd(size)
        a_turtle.left(90)

for i in range(4):
    skinny_rectangle(wolfgang, 100)
    wolfgang.left(90)

for i in range(6):
    tri(franz, 30)
    franz.right(60)



#pentagon(franz, 60)
# for i in range(5,150,8):
#     tri(wolfgang, i)
    