cnt = 1
s = input()
for i in s :
    if int(i) % 2 == 0 :
        cnt *= int(i)
if cnt == 1 :
    print(-1)
else :
    print(cnt)