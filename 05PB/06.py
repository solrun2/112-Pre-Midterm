sum = 0
n = int(input())
i = 1
while True :
    if n == 0 :
        break
    d = n%10
    sum += d
    n = n//10
    i += 1
if sum % 9 == 0 :
    print("Yes {}".format(sum))
else :
    print("No {}".format(sum%9))