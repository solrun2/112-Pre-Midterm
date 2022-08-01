w = float(input("Weight (kg): "))
h = float(input("Height (m): "))
bmi = w/(h**2)
print("BMI is {:.1f}".format(bmi))
if bmi<18.5 :
  print("Underweight")
elif bmi<25 :
  print("Normal weight")
elif bmi<30 :
  print("Overweight")
else : print("Obesity")