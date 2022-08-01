import math
x = float(input("Enter x : "))
if x < 0 :
    ans = math.sqrt(x**2+1)
elif x == 0 :
    ans = x
elif 0 < x <= 99 :
    ans = 3*(x**2)-(1-x)**2
else :
    ans = 2*(x**3)-(x/(math.sqrt(x+1)))
print(f"f({x:.2f}) = {math.ceil(ans)}")