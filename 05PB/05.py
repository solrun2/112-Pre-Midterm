n = int(input("Enter height: "))
if n>0 :
    print(" "*(2*(n-1))+"1")
    i = 1
    while(i<n):
        print(" "*(2*(n-1-i))+"1"+" "*(4*i-1)+"1")
        i += 1
