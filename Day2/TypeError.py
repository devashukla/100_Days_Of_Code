    # TypeError, TypeChecking and TypeConversion
    
len(123) # this leads to type error because len() is used for string, list, tuple, dictionary, set but not for integer.

#to  avoid these types of errors we can use type checking and type conversion.

len("123") # this will work because "123" is a string and len() can be used for string.

# Type checking

print(type(123)) #=> <class 'int'>
print(type(True)) #=> <class 'bool'>
print(type("Hello World")) #=> <class 'str'>
print(type(3.14)) #=> <class 'float'>


# TypeConversion or TypeCasting => converting one data type to another data type.

int("123") # this will convert the string "123" to integer 123.

print(int("123") + int("456")) # this will convert both strings "123" and "456" to integers and then add them. O/P => 579

print(int("abc") + int("456")) # this will lead to ValueError because "abc" cannot be converted to integer.