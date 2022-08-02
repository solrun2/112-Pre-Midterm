n = int(input("Enter a number: "))
if n < 0 :
    print("Invalid input, program terminates.")
else :
    if n == 0 :
        print("0! = 1 = 1")
    elif n == 1 :
        print("0! = 1 = 1\n1! = 1 = 1")
    else :
        print("0! = 1 = 1\n1! = 1 = 1")
        ans = 1
        i = 2
        while 2 <= i <= n :
            print("{}! = {}".format(i,i) , end="")
            j = 0
            while j < i-1 :
                print(" x ",end="")
                print(i-j-1,end="")
                j += 1
            ans *= i
            i += 1
            print(" = {}".format(ans))
        