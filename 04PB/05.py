age = int(input("Enter your age: "))
income = int(input("Enter your net income: "))
if age>=15 and age<=60 :
    if income>= 1 and income <= 30000 :
        nit = income*0.2
        print("Your negative income tax is {:.2f} Baht.".format(nit))
    elif income>30000 and income<=79999 :
        nit = (30000*0.2) - ((income-30000)*0.12)
        print("Your negative income tax is {:.2f} Baht.".format(nit))
    else :
        print("Invalid income.")
else :
    print("Invalid age.")