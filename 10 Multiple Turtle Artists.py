#Multiple Turtle Artists Demo
import turtle, random

#Basic Setup Code
window = turtle.Screen()
window.bgcolor("Black")

turtle_list = []
NUM_TURTLES = 50
color_list = ["Blue", "Chartreuse", "PeachPuff", "Hotpink", "DarkSlateGrey", "DarkSeaGreen"]

turtle.tracer(False)

#Initialization of all the turtles
for i in range(NUM_TURTLES):
    print("creating a turtle")
    turtle_list.append(turtle.Turtle())
    turtle_list[i].setheading(360/NUM_TURTLES * i)
    turtle_list[i].color(random.choice(color_list))
    turtle_list[i].speed(0) 
#Give some instructions to the turtles. 
#Option One
for distance in range(1,150):
    for current_turtle in turtle_list:
        current_turtle.fd(distance)
        current_turtle.right(13)



