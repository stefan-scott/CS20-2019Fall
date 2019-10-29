#Number Converter Demo
#Where we'll try very hard

#Create a variable to hold user input
my_num = input("Please please enter an integer number: ")

#Do some conversions
while True:
    try:
        my_num_integer = int(my_num) #convert to INT
        print("As an integer:", my_num_integer)
        break
    except:
        print("That was not an integer!")
        my_num = input("Please please enter an integer number: ")
##my_num_float = float(my_num) #convert to FLOAT
##print("As a float:", my_num_float)