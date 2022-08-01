import math
n = int(input())
x = round(math.sqrt(n))
while (n % x != 0) :
    x -= 1
y = n // x
print(x + y)