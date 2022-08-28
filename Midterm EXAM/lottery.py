price = int(input())
target = int(input())
guess = int(input())
t1 = ((target//10)//10)%10
t2 = (target//10)%10
t3 = target%10
g1 = ((guess//10)//10)%10
g2 = (guess//10)%10
g3 = guess%10
cnt = 0
if t1 == g1 :
    cnt += 1
if t2 == g2 :
    cnt += 1
if t3 == g3 :
    cnt += 1
x = 0
if cnt == 1 :
    x += 1.0
if cnt == 2 :
    x += 3.0
if cnt == 3 :
    x += 6.0
if cnt == 1 :
    if g1 == t2 and g2 == t1 :
        x += 0.8
    elif g1 == t3 and t1 == g3 :
        x += 0.8
    elif g2 == t3 and g3 == t2 :
        x += 0.8
if cnt != 3 :
    if g1 == t1 + 1 or g1 == t1 - 1 :
        x += 0.3
    if g2 == t2 + 1 or g2 == t2 - 1 :
        x += 0.3
    if g3 == t3 + 1 or g3 == t3 - 1 :
        x += 0.3
print(price*x)