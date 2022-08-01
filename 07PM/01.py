x = float(input())
if x % 1 == 0:
    x = int(x)
    print("{} is an integer.".format(x))
else :
    print("{:.1f} is not an integer.".format(x))