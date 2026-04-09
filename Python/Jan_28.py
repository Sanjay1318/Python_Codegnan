# Output formatting
'''
There are multiple ways for printing the output in a formatted way
1. comma based formatting
We can give multiple objects to print function, it generates a new string by adding spaces between those objects by default
# WAP to find the area of a given square
inp = int(input("Enter the side of a square"))
area = inp * inp
print("The area of the square is : ",area)

2.  % operator based formatting
"string with format specifiers" % (v1,v2,v3,v4, . . . . . .)

%d - int
%f - float
%.nf - rounded float to n digits after decimal point
%s - string

name = input("Enter name: ")
age = int(input("Enter your age:"))
print("This is %s and %s years old" %(name,age))
marks = 89.92365
print("Marks scored %.2f" %(marks))

# Print the area of the circle
inp = int(input("Enter radius of the circle : "))
pi = 3.142567
area = pi * inp * inp
print(area) # 28.283103000000004
print("The area of the circle with %d radius is %.2f" %(inp,area)) # The area of the circle with 3 radius is 28.28

3. Formatted String literals
We mention f at the beginning of the string and placeholders({}) with the variables or simple expressions inside the string.
The f  at the beginning indicates that it is not a direct string literal and the curly brackets({}) should be considered as pplace holders.

name =input()
age = int(input())
op = f"This is {name} and age is {age}"
print(op)
a = 10
b = 20
print(f"sum of a and b is {a+b}")

4. format method in string class
This function is present in string class
We call this function on a string object which has placeholders
We pass the values that have to be embedded inside the string to the functions as aurguments in proper order

name =input()
age = int(input())
op = "This is {} and age is {}"
print(op.format(name,age))

# program to find the sum of 2 numbers
inp = list(map(int,input().split()))
print(sum(inp))
'''


















