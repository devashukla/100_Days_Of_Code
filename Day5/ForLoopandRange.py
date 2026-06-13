#for loop with range function

for number in range(1, 10): # 10 is not included, so the generated number can be any integer from 1 to 9.
    print(number)
    
    for x in range (0, 13, 3): # Start from 1, stop before 13, and increase by 3 each time
        print(x)
    #Generates: 0, 3, 6, 9, 12