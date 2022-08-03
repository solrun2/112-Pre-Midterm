n = input()
sum = 0
max = 0
min = 1e9
cnt = 0
while(n!=""):
    sum += float(n)
    if float(n) > max :
        max = float(n)
    if float(n) < min :
        min = float(n)
    cnt +=1
    n = input()
if cnt == 0 :
    avg = 0
    min = 0
else :
    avg = sum / cnt
print("{:.2f} {:.2f}".format(max,min))
print("{:.2f} {:.2f}".format(sum,avg))