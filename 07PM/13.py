n = int(input())
a = int(input())
ans = 0
cnt = 1
i = 0
while (i<n-1) :
    b = a
    a = int(input())
    if a == b :
        cnt += 1
    else :
        cnt = 1
    if ans < cnt :
        num = a
        ans = cnt
    i += 1
print(num)
print(ans)