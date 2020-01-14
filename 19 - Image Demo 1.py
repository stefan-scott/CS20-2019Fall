import image

img = image.Image("sneakers.jpg")

width = img.get_width()
height = img.get_height()

win = image.ImageWin(width,height)

img.draw(win)
#Greyscale
for y in range(height):
    for x in range(width):
        this_pixel = img.get_pixel(x,y)  #get current pixel
        
        red = this_pixel.get_red()     # extract the original
        green = this_pixel.get_green() # r,g,b values from that
        blue = this_pixel.get_blue()   # pixel
        
        ##Do the work to the pixel   #0 → 255
        average = (red + green + blue) / 3
        THRESHOLD = 170
        
        if average > THRESHOLD:
            #should be white pixel
            red = 255
            green = 255
            blue = 255
        else:
            #should be black pixel
            red = 0
            green = 0
            blue = 0
        ##Done doing the work
        
        new_pixel = image.Pixel(red, green, blue)
        img.set_pixel(x,y,new_pixel)
        

    img.draw(win)