# Logical Operators 

#Logical AND => Returns True if both conditions are true

x = 10
y = 5

print(x > 0 and y > 0)  # True
print(x > 0 and y < 0)  # False

#Logical OR => Returns True if only one condition is true.


a = 10
b = 9

print(a>b or b>a) # True
print(a<5 or b>15) #False

# Logical NOT => Reverses the result.

x = 10

print(not(x > 0))  # False
print(not(x < 0))  # True