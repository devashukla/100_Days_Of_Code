print("Welcome to the RollerCoaster")
Height = int(input("Please Enter your height in cm."))

if Height > 120:
    print("You can ride")
    Age = int(input("Please Enter your Age"))
    if Age >= 18:
        bill = 12
        print("Adult tickets of $12")
    elif Age >= 12 :
        bill = 7
        print("Youth tickets of  $7")
    else:
        bill = 5
        print("Child tickets of  $5")
    
    want_photo = input("Do you want to take photo. Type y for Yes and n for No")
    
    if want_photo == 'y':
        bill += 3
        
    print(f"Your final bill is ${bill}")
    
else:
    print("Drink complan and come later")