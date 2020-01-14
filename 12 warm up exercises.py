def repeated_addition(a, b):
    #a -> number to add
    #b -> number of times to add it
    result = 0
    for i in range(b):
        result += a
    return result

def square(original_number):
    #compute a square using accumulator pattern
    result = 0
    for i in range(original_number):
        result += original_number
    return result

def sum_to_n(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result

def sum_to_gauss(n):
    return n*(n+1)/2






