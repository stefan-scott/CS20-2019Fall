#Analog Clock Demo
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

mike = turtle.Turtle()
mike.color("Blue")
mike.shape("turtle")


for i in range(12):
    mike.up()
    mike.fd(60)
    mike.down()
    mike.fd(10)
    mike.up()
    mike.fd(10)
    
    mike.stamp()
    mike.bk(80)
    mike.left(30)
    
    
    
    
