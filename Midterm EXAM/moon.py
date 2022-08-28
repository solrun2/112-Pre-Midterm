num = int(input())
m = 1
x = num
while m<=12 :
    if m%2 == 1 :
        r = 14
    else :
        r = 15
    while x <= 15 :
        if x == 8 or x == 15 :
            print("x {} {}".format(x,m))
        x += 7
    n = x - 15
    while n <= r :
        if n == 8 or n == r :
            print("n {} {}".format(n,m))
        n += 7
    x = n - 15
    m += 1