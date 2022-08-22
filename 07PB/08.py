import math

def isSquare(n) :
    root = math.sqrt(n)
    if n == 0 or n == 1 :
        return False
    elif int(root)**2 == n :
        return True
    else :
        return False

n = int(input())
cnt = 0
check = n**2 // 2
i = check
while i > 1 :
    if not isSquare(i) :
        i -= 1
        continue
    if isSquare(int(n**2 - i)) :
        print(int(math.sqrt(i)), int(math.sqrt(n**2 - i))) #check
        cnt += 1
    i -= 1
print(cnt)