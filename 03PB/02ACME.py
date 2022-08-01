n = float(input("Enter buying amount: "))
if n >= 3000 :
  x = (n*85)/100 
elif n>= 1000 :
  x = (n*90)/100
else : x= n
print("Amount due after discount is {:.2f} baht.".format(x))