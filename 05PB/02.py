import math
hours = int(input('Enter number of hours (0-20): '))
minutes = int(input('Enter number of minutes (0-59): '))
buyAmt = int(input('Enter shopping amount: '))
allMin = hours*60+minutes
if hours < 0 or hours > 20 or minutes < 0 or minutes > 59 or buyAmt < 0 or (hours == 20 and minutes > 0):
    print("Invalid time.")
    exit()
elif allMin <= 120 :
    price = 0
elif allMin <= 240 :
    price = 20*(math.ceil(allMin/60)-2)
else :
    price = 40 + 50*(math.ceil(allMin/60)-4)
if price != 0 :
    if 300 <= buyAmt <= 3000 :
        if allMin > 240 :
            price -= 40
        else :
            price = 0
    elif buyAmt > 3000 :
        price = 0
if price == 0 :
    print("No charge, thank you.")
else :
    print("Total amount due is {} Baht, thank you.".format(price))