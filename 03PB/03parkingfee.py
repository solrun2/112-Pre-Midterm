import math
h = int(input("Enter number of hours: "))
m = int(input("Enter number of minutes: "))
if h<0 or m<0 or m>=60 :
  print("Input Error!")
elif h==0 and m<=15 :
  print("No charge, thanks.")
elif h==2 and m==0 :
  print("Total amount due is 10 Bahts.")
elif h<2 :
  print("Total amount due is 10 Bahts.")
elif m==0 :
  print("Total amount due is {} Bahts.".format(10+(h-2)*10))
else : 
  print("Total amount due is {} Bahts.".format(10+(h-1)*10))