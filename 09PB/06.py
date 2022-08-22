def alternatingSum(n) :
    if n%2 == 0 :
        return -n // 2
    else :
        return (n+1) // 2

print(alternatingSum(int(input("Enter n: "))))