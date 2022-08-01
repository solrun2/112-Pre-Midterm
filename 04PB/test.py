min = float(input("Minutes before due: "))
tem = float(input("Temperature: "))
rain = input("Is it raining (y/n)? ")
#1d = 1440m
if min == 720 :
    print(">>> 1 days before due.")
else :
    print(">>> {} days before due.".format(round(min / (60*24))))

if min < 2880 and min >= 0 :
  print(">>> I will do the assignment.")
elif min > (1440 * 5) :
  print(">>> I will not do the assignment.")
elif (tem > 40) or (tem > 25 and (rain == 'y'or rain == 'Y')) :
  print(">>> I will not do the assignment.")
else :
  print(">>> I will do the assignment.")