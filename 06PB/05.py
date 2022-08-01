cnt = 1
n = int(input())
if n == -1 :
    print("0")
else :
    high = n
    while n != -1 :
        n = int(input())
        if n > high :
            high = n
            cnt += 1
    print(cnt)
