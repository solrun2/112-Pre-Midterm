print("Upper left corner coordinate:")
x1 = float(input("  << x axis: "))
y1 = float(input("  << y axis: "))
Eastern = float(input("  << Eastern: "))
Southern = float(input("  << Southern: "))
print("Enter a coordinate:")
x_coordinate = float(input("  << x axis: "))
y_coordinate = float(input("  << y axis: "))
x2 = x1 + Eastern
y2 = y1 - Southern
if x1 <= x_coordinate <= x2 and y2 <= y_coordinate <= y1 :
    print(">>> ({:.2f}, {:.2f}) is inside the rectangle.".format(x_coordinate, y_coordinate))
else :
    print(">>> ({:.2f}, {:.2f}) is not inside the rectangle.".format(x_coordinate, y_coordinate))