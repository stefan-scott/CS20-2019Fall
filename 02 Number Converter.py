#Functions Demo
import random

def fortune_one():
    print("Beware the Ides of March!")

def fortune_two():
    print("Today will be your lucky day!")
    
def fortune_three():
    print("You have a message at the office.")

choice = random.randint(0,2) #3 possibilities!

if choice == 0:
    fortune_one()
elif choice == 1:
    fortune_two()
else:
    fortune_three()