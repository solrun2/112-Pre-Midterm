min_before_due = int(input("Minutes before due: "))
temp = float(input("Temperature: "))
Rain = input("Is it raining (y/n)? ")
day_before_due = round(min_before_due / (60*24))
if day_before_due < 2 :
    if day_before_due < 1 :
        print(">>> A half day before due.")
        print(">>> I will do the assignment.")
    else :
        print(">>> {} days before due.".format(day_before_due))
        print(">>> I will do the assignment.")
elif day_before_due > 5 :
    print(">>> {} days before due.".format(day_before_due))
    print(">>> I will not do the assignment.")
elif temp > 40 or (temp > 25 and (Rain == "y" or Rain == "Y")) :
    print(">>> {} days before due.".format(day_before_due))
    print(">>> I will not do the assignment.")
else :
    print(">>> {} days before due.".format(day_before_due))
    print(">>> I will do the assignment.")