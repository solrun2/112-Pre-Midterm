n = int(input())
if n <= 0 :
    print("ERROR")
else :
    while True :
        if n == 0 :
            break
        d = n%10
        print(d)
        n = n//10
    