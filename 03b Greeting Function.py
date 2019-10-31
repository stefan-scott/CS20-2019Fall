#Greeting Function

def greeting():
    global name
    name = "Mr. " + name
    print("Nice to meet you," , name)


name = input("What is your name? ")
greeting()
