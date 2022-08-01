height = int(input("Enter height: "))
width = int(input("Enter width: "))
if height <= 0 or width <= 0 :
    print("Invalid input, program terminates.")
else :
    i = 0
    while i < height :
        j = i%2
        print(" "*j+"* "*width)
        i += 1