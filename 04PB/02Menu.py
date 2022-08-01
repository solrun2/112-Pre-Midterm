print("---<< Main Menu >>---")
print("    <B>urger Meal")
print("    <C>hicken Meal")
print("    <P>asta Meal")
main_menu = input("Enter your choice: ")
if main_menu == "B" or main_menu == "b" :
    print("---<< Burger Sub Menu >>---")
    print("    <R>egular Burger")
    print("    <C>heese Burger")
    print("    <D>ouble Cheese Burger")
    burger = input("Enter your choice: ")
    if burger == "R" or burger == "r" :
        print("Your Regular Burger is 60 Baht.")
    elif burger == "C" or burger == "c" :
        print("Your Cheese Burger is 75 Baht.")
    elif burger == "D" or burger == "d" :
        print("Your Double Cheese Burger is 90 Baht.")
    else:
        print("Invalid sub menu choice.")
elif main_menu == "C" or main_menu == "c" :
    print("---<< Chicken Sub Menu >>---")
    print("    <F>ried Chicken")
    print("    <G>rilled Chicken")
    print("    <C>hef's Chicken")
    chicken = input("Enter your choice: ")
    if chicken == "F" or chicken == "f" :
        print("Your Fried Chicken is 120 Baht.")
    elif chicken == "G" or chicken == "g" :
        print("Your Grilled Chicken is 150 Baht.")
    elif chicken == "C" or chicken == "c" :
        print("Your Chef's Chicken is 180 Baht.")
    else:
        print("Invalid sub menu choice.")
elif main_menu == "P" or main_menu == "p" :
    print("---<< Pasta Sub Menu >>---")
    print("    <S>paghetti de Italiano")
    print("    <L>asagna Supreme")
    print("    <M>acaroni Special")
    pasta = input("Enter your choice: ")
    if pasta == "S" or pasta == "s" :
        print("Your Spaghetti de Italiano is 90 Baht.")
    elif pasta == "L" or pasta == "l" :
        print("Your Lasagna Supreme is 120 Baht.")
    elif pasta == "M" or pasta == "m" :
        print("Your Macaroni Special is 100 Baht.")
    else:
        print("Invalid sub menu choice.")
else:
    print("Invalid main menu choice.")