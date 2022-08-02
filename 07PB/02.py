n = int(input("Enter a number: "))
if n < 1 or n > 26 :
  print("Invalid input, program terminates.")
else :
  i = n
  while i >= 1 :
    j = 1 
    c = ord("A")
    while j <= i :
      print(chr(c+j-1),end="")
      j += 1
    print("")
    i -= 1