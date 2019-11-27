import microbit, turtle, random

SENSITIVITY = 250
END_LINE_X = 400
window = turtle.Screen()
window.setup(1000, 300)

flash = turtle.Turtle()
pokey = turtle.Turtle()
referee = turtle.Turtle()

referee.up()
referee.pensize(4)
referee.goto(END_LINE_X,-150)
referee.left(90)
referee.down()
referee.fd(300)

flash.up()
flash.goto(-400, 100)
flash.down()

pokey.up()
pokey.goto(-400, -100)
pokey.down()

def x_rotation():
    """ Simple Function to return whether the
Microbit is Flat, tilted Left, or tilted right"""
    
    rotation = microbit.accelerometer.get_x()
    if rotation < SENSITIVITY and rotation > SENSITIVITY*-1:
        return "flat"
    elif rotation >= SENSITIVITY:
        return "right"
    else:
        return "left"

last_position = x_rotation()
while True:
    current_position = x_rotation()
    if current_position == "right":
        if last_position != "right":
            flash.fd(5)
            last_position = "right"
            
    elif current_position == "left":
        if last_position != "left":
            flash.fd(5)
            last_position = "left"
    pokey.fd(random.randint(1,4))
    
    if pokey.xcor() > END_LINE_X:
        print("Computer Wins!!")
        break
    elif flash.xcor() > END_LINE_X:
        print("Player Wins!!!")
        break
print("Program Done")
    
    