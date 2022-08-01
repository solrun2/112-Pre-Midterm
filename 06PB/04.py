i = 1
score = 0
while i<=10 :
    print("Frame # {}".format(i))
    n = int(input("Number of pins down: "))
    score += n
    if n == 10 :
        pass
    else :
        print("Frame # {}".format(i))
        m = int(input("Number of pins down (0-{}): ".format(10-n)))
        score += m
    i += 1
print("Total score is {}".format(score))  


