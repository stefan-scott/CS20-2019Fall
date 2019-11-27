import microbit, turtle

SENSITIVITY = 250 

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

while True:
    
    print(x_rotation())