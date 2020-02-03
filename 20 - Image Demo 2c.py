import image

source_image = image.Image("moon.jpg") #open an image
THRESHOLD = 50

width = source_image.get_width()   #find the width and
height = source_image.get_height()  #height of the image

shifted = image.EmptyImage(width,height)

window = image.ImageWin(width, height)  #create a window

source_image.draw(window)

#Set up Loops to Visit every pixel and do some work

for x in range(1,width):
    for y in range(1,height):
        #retrieve the current pixel
        current_pixel = source_image.get_pixel(x,y)
        shifted.set_pixel(x-2,y-2,current_pixel)
        
    
#     if x % 3 == 0: #to speed up the animation
#         source_image.draw(window)  #animate the manipulation
shifted.draw(window)            


for x in range(width):
    for y in range(height):
        pixel_one = source_image.get_pixel(x,y)
        pixel_two = shifted.get_pixel(x,y)
        
        avg_one = (pixel_one.get_red() + pixel_one.get_green() + pixel_one.get_blue()) / 3
        avg_two = (pixel_two.get_red() + pixel_two.get_green() + pixel_two.get_blue()) / 3
        
        if abs(avg_one - avg_two) > THRESHOLD:
            source_image.set_pixel(x,y,image.Pixel(255,0,0))
        #else:
            #source_image.set_pixel(x,y,image.Pixel(255,255,255))
    if x % 3 == 0: #to speed up the animation
        source_image.draw(window)
source_image.draw(window)