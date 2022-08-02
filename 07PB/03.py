n = int(input("Enter a number: "))
if n < 1 or n > 26 :
    print("Invalid input, program terminates.")
else :
    i = 1
    c = ord("A")
    while i <= n :
      j = 1
      while j <= i :
        print(chr(c+j-1),end="")
        j += 1
      print("")
      i += 1
    i = n-1
    while i >= 1 :
      j = 1
      while j <= i :
        print(chr(c+j-1),end="")
        j += 1
      print("")
      i -= 1
