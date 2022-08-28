import math
x = int(input())
y = int(input())
d = int(input())
if x<y and d>0 :
    while x<=y :
        print(x)
        x += d
elif x>y and d<0 :
    while x>=y :
        print(x)
        x += d
elif x==y :
    print(x)