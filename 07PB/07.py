import math

def PrimeNumber(n) :
    check = round(math.sqrt(n))
    while True :
        if check == 1 :
            return True
        if n % check == 0 :
            return False
        check -= 1

def PrimeFactor(n,i) :
    while i <= n :
        if PrimeNumber(i) :
            if n % i == 0 :
                print(i)
                n = n // i
            else : 
                i += 1
        else :
            i += 1
      
n = int(input("Enter positive integer: "))
if n == 1 :
  pass
elif n <= 0 :
  print("Invalid number.")
elif PrimeNumber(n) :
  print(n)
else :
    i = 2 
    PrimeFactor(n,i)
        