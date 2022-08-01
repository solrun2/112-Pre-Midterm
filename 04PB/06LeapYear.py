year = input("Enter year: ")
if year.isdigit() and year!='0' :
    years = int(year)
    if (years%4==0 and years%100!=0) or years%400==0 :
        print("{} is a leap year.".format(years))
    else : print("{} is not a leap year.".format(years))
else :
    print("Invalid year.")