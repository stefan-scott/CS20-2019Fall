#Larger than Ten

def larger_than_10(num):
    if num > 10:
        return True
    else:
        return False
    
user_number = int(input("Enter a number: "))

answer = larger_than_10(user_number)
print(answer)

if larger_than_10(user_number):
    print("Yes, it is larger")
else:
    print("No, it is not larger")
