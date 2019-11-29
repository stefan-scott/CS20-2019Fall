import microbit, random, time

def generate_image(cur_list):
    result = cur_list[0] + cur_list[1] + cur_list[2]+ cur_list[3] +cur_list[4]
    return result

def show_image():
    microbit.display.show(microbit.Image(generate_image(active_image)))

def set_pixel(col, row, value):
    original_str = active_image[row] #row with pixel to change
    updated_str = ""
    for i in range(len(original_str)): #i = 0, 1, 2, 3, 4, 
        if i != col:
            updated_str += original_str[i]
        else:
            updated_str += str(value)
    active_image[row] = updated_str
    #show_image()
 

            #STR           INT
#This global image will be used as the "active custom image" on
#the micro:bit. Whenever we update it, re-draw it to the screen
active_image = ["00000:",
                "00000:",
                "00000:",
                "00000:",
                "00000" ]

def random_sparkle():
    x = random.randint(0,4) # 0, 1, 2, 3, 4
    y = random.randint(0,4)
    intensity = random.randint(0,9)
    set_pixel(x, y, intensity)
    show_image()

def sweep(intensity):
    for y in range(5):
        for x in range(5):
            set_pixel(x,y,intensity)
            show_image()

def set_all(intensity):
    for y in range(5):
        for x in range(5):
            set_pixel(x,y,intensity)
    show_image()

def draw_player(x, y, intensity):
    set_pixel(x,y,intensity)
    show_image()
    
def move_left():
    global player_x
    if player_x > 0:
        draw_player(player_x, player_y, 0)
        player_x -= 1
        draw_player(player_x, player_y, 9)
          
def move_right():
    global player_x
    if player_x < 4:
        draw_player(player_x, player_y, 0)
        player_x += 1
        draw_player(player_x, player_y, 9)      
set_all(0)
player_x = 2
player_y = 2
draw_player(player_x, player_y, 9)
while True:
    if microbit.button_a.was_pressed():
        move_left()
    if microbit.button_b.was_pressed():
        move_right()
    time.sleep(0.05)
    
    
    
#     for i in range(10): # 0, 1, 2 ... 9
#         set_all(i)
#         time.sleep(0.04)
#     for i in range(10): # 0, 1, 2 ... 9
#         set_all(9 - i)
#         time.sleep(0.04)

