import math

def isSquare(n) :
    root = math.sqrt(n)
    if int(root)**2 == n :
        return True
    else :
        return False

print(isSquare(99))