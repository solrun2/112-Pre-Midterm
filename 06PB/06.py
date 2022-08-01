n = int(input())
sum = 0
while not(1<=sum<=9) :
    sum = 0
    while True :
        if n == 0 :
            break
        sum += n % 10
        n = n // 10
    n = sum
print(sum)
    
