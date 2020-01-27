import math

def dist_euc(x1, y1, x2, y2):
    #calculate the straightline distance between 2 points
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    #use Pythagorean...
    dist = math.sqrt(a**2 + b**2)
    return dist

def dist_man(x1, y1, x2, y2):
    #calculate the manhatten distance between 2 points
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    #use Pythagorean...
    dist = a + b
    return dist

