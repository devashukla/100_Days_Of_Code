# Pizza Order Practice 

print("Welcome to the Pizzeria")

size = input("What size of Pizza do you want ? S, M, L")
pepperoni = input("Do you want extra pepperoni? Y or N")
cheese = input("Do you want extra cheese? Y or N")

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else :
    print("You have done the wrong input")

if pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if cheese == 'Y':
    bill += 1
    
print(f"Your final bill is {bill}")
    