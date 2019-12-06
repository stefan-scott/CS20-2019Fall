# Micro:bit Metrenome Person Ability Game
# How good are you at rendering the metronome obsolete??
# A simple Micro:bit:bit game

import microbit, time, random

#Global Variables
score = 0
current_round = 0

def single_round():
    """ run a single round of the metronome game """
    #create round variables
    round_time = random.randint(1,4)
    target_num_presses = random.randint(2, 10)

    print("In this round, when the micro:bit lights turn on")
    print("press A", target_num_presses, "times")
    print("in as close to", round_time, "seconds as possible")

    time.sleep(1) #1 second delay before countdown begins

    #begin countdown
    microbit.display.show("3")
    time.sleep(1)
    microbit.display.show("2")
    time.sleep(1)
    microbit.display.show("1")
    time.sleep(1)
    #Square indicates the timer has begun
    microbit.display.show(microbit.Image.SQUARE)

    #initialize counting variables
    start_time = time.time()
    num_presses = 0

    #reset the button counter
    microbit.button_a.was_pressed()
    while True:
        if microbit.button_a.was_pressed():
            num_presses += 1
        if num_presses == target_num_presses:
            break
    
    #calculate the results
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    #calculate how far off in seconds the user was
    difference = abs(elapsed_time-round_time)
    print("It took you",elapsed_time,"seconds!")
    
    if difference < 0.3:
        print("Amazing! That's worth 5 points")
        microbit.display.show(microbit.Image.ROLLERSKATE)
        time.sleep(1.5)
        return 5
    elif difference < 1:
        print("OK. That's worth 2 points")
        microbit.display.show(microbit.Image.COW)
        time.sleep(1.5)
        return 2
    else:
        print("BAD. -1 points")
        microbit.display.show(microbit.Image.SKULL)
        time.sleep(1.5)
        return -1

for i in range(3): #Play 3 Rounds in Total
    score += single_round()
    
print("Your Total Score is", score)
if score > 10:
    print("You've got some serious skillz")
else:
    print("Get Good.")
    

