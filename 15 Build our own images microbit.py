import microbit, random, time

def generate_image(cur_list):
    result = cur_list[0] + cur_list[1] + cur_list[2]+ cur_list[3] +cur_list[4]
    return result
    


my_image  = "00009:" \
            "00009:" \
            "90009:" \
            "49094:" \
            "13931"

list_image = ["00000:",
              "00000:",
              "00000:",
              "00000:",
              "00000" ]

while True:
    row = random.randint(0,4)
    col = random.randint(0,4)
    list_image[row][col] = random.randint(0,9)
    
    image_to_display = microbit.Image(generate_image(list_image))
    microbit.display.show(image_to_display)