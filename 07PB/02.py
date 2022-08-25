n = int(input("Enter a number: "))
if n < 1 or n > 26 :
  print("Invalid input, program terminates.")
else :
  i = n
  while i > 0 :
    j = 0 
    c = ord("A")
    while j < i :
      print(chr(c+j),end="")
      j += 1
    print("")
    i -= 1