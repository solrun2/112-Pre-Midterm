TV = int(input("How many TVs? "))
DVD = int(input("How many DVD players? "))
Audio = int(input("How many Audio Systems? "))
TV_price = TV*6000
DVD_price = DVD*1500
Audio_price = Audio*3000
Total = TV_price + DVD_price + Audio_price
print("Total price is {:.2f} baht.".format(Total))
if Total >= 24000 :
    Discount = Total*20/100
    Total = Total*80/100
    print("You've got a discount of {:.2f} baht.".format(Discount))
    print("Your payment is {:.2f} baht. Thank you!".format(Total))
else :
    print("Your payment is {:.2f} baht. Thank you!".format(Total))