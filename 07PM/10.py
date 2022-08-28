n = int(input())
ans = 0
while True :
    if n == 0 :
        break
    d = n % 10
    if d % 2 == 1 :
        ans += d
    n = n // 10
if ans == 0 :
    ans = -1
print(ans)