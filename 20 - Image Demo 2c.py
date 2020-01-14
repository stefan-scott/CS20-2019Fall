import image

source_image = image.Image("rooster.jpg") #open an image
add_image = image.Image("smile.png")

width = source_image.get_width()   #find the width and
height = source_image.get_height()  #height of the image
add_width = add_image.get_width()   #width of emoji
add_height = add_image.get_height() #height of the emoji

window = image.ImageWin(width, height)  #create a window

source_image.draw(window)

#Set up Loops to Visit every pixel and do some work

for x in range(add_width):
    for y in range(add_height):
        #retrieve the current pixel
        current_pixel = add_image.get_pixel(x,y)
        dest_pixel = source_image.get_pixel(x+155,y+100)
        
        #access the R,G,B component values
        r = current_pixel.get_red()
        g = current_pixel.get_green()
        b = current_pixel.get_blue()
        
        r2 = dest_pixel.get_red()
        g2 = dest_pixel.get_green()
        b2 = dest_pixel.get_blue()
        
        red = r * 0.5 + r2 * 0.5
        green = g * 0.5 + g2 * 0.5
        blue = b * 0.5 + b2 * 0.5
        
        new_pixel = image.Pixel(red, green, blue)
        
        if r<250 and g<250 and b<250:
            source_image.set_pixel(x+155,y+100,new_pixel) #create a new pixel
    
    if x % 3 == 0: #to speed up the animation
        source_image.draw(window)  #animate the manipulation
source_image.draw(window)            
