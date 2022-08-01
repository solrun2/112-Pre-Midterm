buffet_type = input("Enter your buffet choice: ")

if buffet_type == "Korean" :
    Wed = input("Is today Wednesday (yes/no)? ")
    price = 1500
    if Wed == "yes" :
        price = price*85/100
    print("Your payment is {:.2f} Baht.".format(price))
elif buffet_type == "Japanese" :
    Wed = input("Is today Wednesday (yes/no)? ")
    price = 1000
    if Wed == "yes" :
        price = price*85/100
    print("Your payment is {:.2f} Baht.".format(price))
else :
    print("Sorry, there is no {} buffet.".format(buffet_type))