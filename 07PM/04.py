import math
while True :
    print("<<Point a>>")
    x1 = int(input("Enter x coordinate: "))
    y1 = int(input("Enter y coordinate: "))
    print("<<Point b>>")
    x2 = int(input("Enter x coordinate: "))
    y2 = int(input("Enter y coordinate: "))
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0 :
        print("Goodbye")
        break
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print("Distance between ({}, {}) and ({}, {}):".format(x1,y1,x2,y2))
    print("Euclidean distance is {:.2f}.".format(distance))
    horizon = int(math.fabs(x1-x2))
    vertical = int(math.fabs(y1-y2))
    print("Horizontal distance is {}.".format(horizon))
    print("Vertical distance is {}.".format(vertical))
    if y1 > y2 :
        y = "south"
    elif y2 > y1 :
        y = "north"
    else :
        y = ""
    if x1 > x2 :
        x = "west"
    elif x2 > x1 :
        x = "east"
    else :
        x = ""
    if x == "" and y == "" :
        print("We are going nowhere.")
    elif x == "" :
        print("We are going {}.".format(y))
    elif y == "" :
        print("We are going {}.".format(x))
    else :
        print("We are going {}-{}.".format(y,x))