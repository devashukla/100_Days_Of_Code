print("Welcome to the RollerCoaster")
Height = int(input("Please Enter your height in cm."))

if Height > 120:
    print("You can ride")
    Age = int(input("Please Enter your Age"))
    if Age > 18:
        print("Pay $12")
    elif Age > 12 & Age < 18:
        print("Pay $7")
    else:
        print("Pay $5")
else:
    print("Drink complan and come later")