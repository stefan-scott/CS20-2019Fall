import image

source_image = image.Image("giraffe.jpg") #open an image

width = source_image.get_width()   #find the width and
height = source_image.get_height()  #height of the image

window = image.ImageWin(width, height)  #create a window

source_image.draw(window)

#Set up Loops to Visit every pixel and do some work

for x in range(width):
    for y in range(height):
        #retrieve the current pixel
        current_pixel = source_image.get_pixel(x,y)
        
        #access the R,G,B component values
        r = current_pixel.get_red()
        g = current_pixel.get_green()
        b = current_pixel.get_blue()
        
        #is this pixel on the bottom half??
        if y > height/2:
            r = g
            b = g
        
        new_pixel = image.Pixel(r, g, b)  #create a new pixel
        source_image.set_pixel(x,y,new_pixel) #create a new pixel
    
    if x % 3 == 0: #to speed up the animation
        source_image.draw(window)  #animate the manipulation
source_image.draw(window)            
