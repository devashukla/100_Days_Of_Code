weight = 70 # in kg
height = 1.75 # in meters

bmi = weight / (height ** 2)

print(bmi) #O/P => 22.857142857142858
print(int(bmi)) # It will only return the integer part of the BMI value. O/P => 22
print(round(bmi)) # It will round the BMI value to the nearest integer. O/P => 23
print(round(bmi, 2)) # It will round the BMI value to 2 decimal places. O/P => 22.86
