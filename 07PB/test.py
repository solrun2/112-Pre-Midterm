x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
n, m = x, y
if m > n :
    n, m = m, n
while True :
    if m == 0 :
        break
    n, m = m, n % m
print("  >> gcd({}, {}) ={:>7}".format(x,y,n))
new_x = x // n
new_y = y // n
print("  >> lcm({}, {}) ={:>7}".format(x,y,new_x*new_y*n))