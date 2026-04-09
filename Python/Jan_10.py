# WAP to check if the given string is palindrome, output should be true or false
'''
s = input("Enter a String ")
lower_s = s.lower()
rev_s = lower_s[ : :-1]
print(lower_s == rev_s)
'''

# WAP to check if the first half of the string is same as the second half. It is guranteed that the string will always have even no. of characters
'''
s = input("Enter a string ")

length_s = len(s)
mid_index = length_s // 2

first_half = s[ :mid_index]
second_half = s[mid_index: ]

print(first_half)
print(second_half)
print(first_half == second_half)
'''

# Operations on Strings
''' continuation from Jan_9
        4. String Class Methods :
                Functions defined in a particular class work only on those data types for which they are defined.
                These types of functions are called as methods

                Synatx to call these types of functions:
                    object.function_name()
'''
# case conversion methods
'''
s = "Python Programming Language"

low_s = s.lower()
print(low_s) # python programming language

upper_s = s.upper()
print(upper_s) # PYTHON PROGRAMMING LANGUAGE

swapcase_s = s.swapcase()
print(swapcase_s) # pYTHON pROGRAMMING lANGUAGE

capital_s = s.capitalize()
print(capital_s) # Python programming language

title_s = s.title()
print(title_s) # Python Programming Language

a = "#Pyt#hon#"

strip_a = a.strip("#")                                             # in strip() function only the first occurance of the element given in brackets will be removed
print(strip_a) # Pyt#hon

print(a.lstrip("#")) # Pyt#hon#
print(a.rstrip("#")) # #Pyt#hon
'''
# WAP to check if the given gmail address is valid
'''
mail = input("Enter your Gmail address: ")

print(mail.endswith("@gmail.com") and mail.count("@") == 1 and " " not in mail)
'''

# WAP to check if a given password is valid. Conditions : should have minimun of 5 characters and maximum of 8 characters
# should have atleast one special character other than alphabet and digits, should not start with a digit
'''
password = input("Enter your password ")
length = len(password)

con1 = length >= 5 and length <= 8
con2 = not password.isalnum()
con3 = not password[0].isdigit()

print(con1 and con2 and con3)
'''
# split() - used to split the string based on a seperator. It always returns a List
'''
names = "Alex Bob Charles George"
print(names.split()) # ['Alex', 'Bob', 'Charles', 'George']

names = "Alex,Bob,Charles,George"
print(names.split(",")) # ['Alex', 'Bob', 'Charles', 'George']
'''

# join() - 
'''
print("-".join(["1","2","3","4","Good","Boy"])) # 1-2-3-4-Good-Boy
'''

# find() , rfind() , index() , rindex() , count()
''' only returns the first occurances

print("sanjay".find("a")) # 1
print("sanjay".rfind("a")) # 4
print("sanjay".index("a")) # 1
print("sanjay".rindex("a")) # 4
print("sanjay".count("a")) # 2
'''
# format() - used for formatting
''' {} - place holders
'''
'''
name = input("Enter your name ")
s = "Hi {}.  Welcome to your account"
print(s.format(name))
'''












                
