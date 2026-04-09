# Relational Operators
''' These operators are used for comparision of 2 values
     They return boolean True or False based on the comparisions we do

     Symbol                            Operation
     >                                          Greater than
     >=                                       Greater than Equal to
     <                                          Less than
     <=                                       Less than Equal to
     ==                                       Is Equal to
     !=                                        Is Not Equal to
   
a = float(input("Enter first number "))          # Lets assume a = 10 and b = 20
b = float(input("Enter second number "))
                                  # Lets assume a = 10 and b = 20
print(a>b)            False
print(a>=b)         False
print(a<b)            True
print(a<=b)         True
print(a==b)         False
print(a!=b)          True

'''

# You are given details about the workout time of 2 persons
# The input is given in hours calculate the total time spent on workout by both in minutes
# Check if Person A has worked out more than Person B
'''
person_a = float(input("Enter Person A workout Time "))
person_b = float(input("Enter Person B workout Time "))

minutes_a = person_a * 60
minutes_b = person_b * 60

print("Total workout time in minutes of  combined A and B is ", float(minutes_a + minutes_b) , "Minutes")

if  minutes_a > minutes_b:
    print(" True Person A has more workout time than Person B")
elif  minutes_a == minutes_b:
    print("Both A and B has same workout time")
else:
    print("Person B has more workout time than Person A")
'''

# You will be given dimensions of 2 squares as 2 lines of input, Check if the first square can fit in the second square. Output should be true or false
'''
dimension_1 = float(input("Enter the lenght of  the side of First Square "))
dimension_2 = float(input("Enter the lenght of  the side of Second Square "))

print(dimension_1 > dimension_2)
'''
# Logical Operators
''' These are special keywords working with boolean operands and they work according to their respective logic gates

                                                        and           or
                                                        
      op1                op2                 Result      Result
      True              True               True          True
      True              False              False         True
      False             True               False         True
      False             False              False          False

      not (returns True if op is False and viceversa)
'''

# Check whether the given number is in range of 100 to 200 both inclusive. Output should be True or False
'''
num = float(input("Enter a number "))

if num >= 100 and num <= 200:
    print("True")
else:
    print("False")
'''

# Assignment Operators
''' These are special symbols used for assigning or updating values present in the variables

    =      Assignment
    +=   Adding and Reassignment
    -=    Subtracting and Reassignment
    *=   Multiplication and Reassignment
    /=   Division and Reassignment

a = 30
print(a)      # returns 30

a += 5        # a = a + 5
print(a)    # returns 35

a -= 5        # a = a - 5
print(a)    # returns 30

a *= 5        # a = a * 5
print(a)    # returns 150

a /= 5        # a = a / 5
print(a)    # returns 30
'''

# Membership Operators
''' These are used to check if an object is an member of an iterables(group of objects together is called iterables)
    These are keywords which return boolean True or False

    working of in
    present         -> True
    not present -> False

    working of not in
    present         -> False
    not present -> True

print("t" in "python")      # returns True
print("t" not in "python")      # returns False
print(2 in [1,2,3,"hello"])   # returns True









































