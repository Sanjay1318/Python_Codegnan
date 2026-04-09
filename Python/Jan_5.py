# Performing operations directly assigning the values
'''
a = 10
b = 4

print("a+b is ", a+b)
print("a-b is ", a-b)
print("a*b is ", a*b)
print("a/b is ", a/b)
print("a//b is", a//b)
print("a%b is ", a%b)
print("a**b is ", a**b)
'''

# Performing operations by taking the input from user
# (User input is default stored as string unless we mention the specific datatype in the program
# (example in below code : we assigned float so now its float data type))
'''
a = float(input("Enter first number "))
b = float(input("Enter second number "))

print("a+b is ", a+b)
print("a-b is ", a-b)
print("a*b is ", a*b)
print("a/b is ", a/b)
print("a//b is", a//b)
print("a%b is ", a%b)
print("a**b is ", a**b)
'''

# WAP to find the sum of 2 numbers taking input from user
'''
a = float(input("Enter First number "))
b = float(input("Enter Second number "))

print("Sum of the given 2 numbers is ", a+b)
'''

# Class Types 
'''
a = input("Enter something  ")

print(type(a)) # str
print(type(10.98)) # float
print(type(10)) # int
print(type(True)) # boolean
print(type([1.2,"good","boyyyy"])) # list
print(type((1.2,"good","boyyyy"))) # tuple
print(type({"name":"good boyyyy", "marks":"90"})) # dict
print(type({1.2,"good","boyyyy"})) # set
'''

# Type Conversion or Type Casting
'''
    It is converting from one data type to other
    To do type conversion we use the functions with the same names as their respective class names
    int()           for integers
    float()       for float
    str()           for strings
    bool()       for boolean
    list()          for Lists
    tuple()      for tuple
    dict()         for dictionary
    set()           for sets

    Not all conversions are possible, only compatable values can be converted and remaining conversions throws errors(value error)
'''

# WAP to find the area of circle, taking radius from the user(consider pi = 3.14)
'''
radius = float(input("Enter Radius of the Circle "))
pi = 3.14

area = pi * radius * radius

print("Area of circle is " , float(area))
'''

# WAP to find the square root of the number
'''
num = float(input("Enter a Number "))

sqrt = num ** 0.5

print("Square root of number is  ", round(sqrt,2)) # round() rounds of to the required number of digits after point 
'''
