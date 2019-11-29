import microbit, random, time

def generate_image(cur_list):
    result = cur_list[0] + cur_list[1] + cur_list[2]+ cur_list[3] +cur_list[4]
    return result

def show_image():
    microbit.display.show(microbit.Image(generate_image(active_image)))


def set_pixel(col, row, value):
    original_string = active_image[row]
    updated_string = ""
    for i in range(len(original_string)): #loop through each char in row to modify
        if i != col:                      #could be 5 or 6 chars...
            updated_string += original_string[i]
        else:
            updated_string += str(value)
    active_image[row] = updated_string
    show_image()

#This global image will be used as the "active custom image" on
#the micro:bit. Whenever we update it, re-draw it to the screen
active_image = ["00000:",
                "00000:",
                "00000:",
                "00000:",
                "00000" ]

def random_sparkle():
    row = random.randint(0,4)
    col = random.randint(0,4)
    set_pixel(col, row, random.randint(0,9))
    print(active_image)
    
def sweep(step):
    clear()
    for i in range(5):
        set_pixel(i,int(step/2),9)

def clear():
    active_image = ["00000:",
                    "00000:",
                    "00000:",
                    "00000:",
                    "00000" ]
    show_image()
counter = 0
while True:
    sweep(counter)
    counter += 1
    if counter >=10: counter = 0
    #time.sleep(0.1)
