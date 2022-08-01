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
n, m = x, y
if m > n :
    n, m = m, n
lcm_first = m
while True :
    if lcm_first % n == 0 and lcm_first % m == 0 :
        lcm = lcm_first
        break
    lcm_first += 1
print("  >> lcm({}, {}) ={:>7}".format(x,y,lcm))