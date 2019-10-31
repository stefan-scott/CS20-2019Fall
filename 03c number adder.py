num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number: "))
sum = 0.0

def add_numbers():
    global sum
    sum = num1 + num2

add_numbers()
print("The result is:",sum)