#List And its important methods

fruits = ["Cherry", "Apple", "Banana"]
print(fruits)

print(fruits[0])   # Cherry
print(fruits[1])   # Apple
print(fruits[-1])  #Banana

#Modification of List 

fruits = ["apple", "banana", "mango"]

fruits[0] = "orange"
print(fruits)  # ["orange", "banana", "mango"]

# append() => Using this function we can add the item in the end of the list.
fruits.append("grapes") 
print(fruits) #['orange', 'banana', 'mango', 'grapes']

#insert() => Kisi specific position par item add karta hai.
fruits.insert(1, "Kiwi")
print(fruits) #['orange', 'Kiwi', 'banana', 'mango', 'grapes']

# remove() => Remove the item on the basis of value.

fruits.remove("banana")
print(fruits) #['orange', 'Kiwi', 'mango', 'grapes']

#pop() => Removes the item on the basis of index.

fruits.pop(3)
print(fruits) #['orange', 'Kiwi', 'mango'] 