sum = 0
n = int(input())
while True :
    if n == 0 :
        break
    d = n%10
    sum += d
    n = n//10
if sum % 9 == 0 :
    print("Yes {}".format(sum))
else :
    print("No {}".format(sum%9))