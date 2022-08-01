cnt = 0
while cnt == 0 :
    cnt = 1
    x = int(input())
    y = int(input())
    if x<=0 or y<=0 or x>6 or y>6 :
        cnt = 0
        print("ERROR")
if x+y == 7 or x+y == 11 :
    print("1 {} W".format(x+y))
    exit()
elif x+y == 3 or x+y == 2 or x+y == 12 :
    print("1 {} L".format(x+y))
    exit()
else :
    target = x+y
cnt = 1
while True :
    cnt += 1
    x = int(input())
    y = int(input())
    if x+y == target :
        print("{} {} W".format(cnt,x+y))
        exit()
    elif x+y == 7 :
        print("{} {} L".format(cnt,x+y))
        exit()
    elif x<=0 or y<=0 or x>6 or y>6 :
        cnt -= 1
        print("ERROR")