n = int(input("Enter a number : "))
if n < 0 :
    print("Invalid input, program terminates.")
else :
    i = 0
    ans = 1
    while i <= n :
        ans *= i
        i += 1