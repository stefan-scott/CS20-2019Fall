import microbit, turtle

window = turtle.Screen()
francis = turtle.Turtle()
francis.speed(0)
speed = 5

SENSITIVITY = 250

while True:
    francis.forward(speed)
    
    x = microbit.accelerometer.get_x()
    if x > SENSITIVITY:
        francis.right(10)
    elif x < -SENSITIVITY:
        francis.left(10)

    if microbit.button_a.was_pressed():
        speed = speed - 1
        if speed < 1:
            speed = 1
    if microbit.button_b.was_pressed():
        speed = speed + 1
        if speed > 20:
            speed = 20
    print(speed)
        