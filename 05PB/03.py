n = int(input("Enter number: "))
cnt = 0
while(n>=0):
    if n%2 == 1 :
        cnt += 1
    n = int(input("Enter number: "))
print("Received {} odd numbers".format(cnt))