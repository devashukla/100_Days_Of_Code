 #Example for explaining Nested If-Else Statement
print("Welcome to the RollerCoaster")
Height = int(input("Please Enter your height in cm."))

if Height > 120:
    print("You can ride")
    Age = int(input("Please Enter your Age"))
    if Age > 18:
        print("Pay $12")
    else:
        print("Pay $7")
else:
    print("Drink complan and come later")