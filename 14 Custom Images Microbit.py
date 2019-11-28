import microbit, time

clock_images = [microbit.Image.CLOCK1,
                microbit.Image.CLOCK2,
                microbit.Image.CLOCK3,
                microbit.Image.CLOCK4,
                microbit.Image.CLOCK5,
                microbit.Image.CLOCK6,
                microbit.Image.CLOCK7,
                microbit.Image.CLOCK8,
                microbit.Image.CLOCK9,
                microbit.Image.CLOCK10,
                microbit.Image.CLOCK11,
                microbit.Image.CLOCK12 ]
current_index = 0
delay_amount = 0.1
while True:                
    microbit.display.show(clock_images[current_index])
    current_index += 1
    if current_index > 11:
        current_index = 0
    #accel-x    -1024 (left) ->   1024 (right)
    x_rot = microbit.accelerometer.get_x()
    
    if x_rot <-600: delay_amount = 0.01
    elif x_rot < -200: delay_amount = 0.05
    elif x_rot < 200: delay_amount = 0.1
    elif x_rot < 600: delay_amount = 0.15
    else: delay_amount = 0.2
    
    time.sleep(delay_amount)