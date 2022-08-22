a = int(input())
b = int(input())
i = a
while i <= b :
    j = a
    while j <= b :
        if i == j :
            pass 
        else :
            k = a
            while k <= b :
                if j == k :
                    pass 
                else :
                    print("{}{}{}".format(i,j,k))
                k += 1
        j += 1
    i += 1