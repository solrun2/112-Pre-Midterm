import math
def PrimeNumber(n) :
    check = round(math.sqrt(n))
    while True :
        if check == 1 :
            return True
        if n % check == 0 :
            return False
        check -= 1

while True :
    n = int(input("Enter a number: "))
    if n == 0 :
        print("End of program, goodbye.")
        break
    elif n <= 1 :
        print("Invalid input, try again.")
    elif PrimeNumber(n) :
        print("{} is a prime number.".format(n))
    else :
        print("{} is not a prime number.".format(n))