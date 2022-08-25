n = int(input("Enter a number: "))
if n < 1 or n > 26 :
    print("Invalid input, program terminates.")
else :
    i = 0
    c = ord("A")
    while i < n :
      j = 0
      while j <= i :
        print(chr(c+j),end="")
        j += 1
      print("")
      i += 1