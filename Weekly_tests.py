#  Write a Python program that:                                                                     
#  1. Uses a for loop to traverse a given string. 
#  2. Counts occurrences of the character at index 2.  
#  3. Prints the index position when this character occurs for the third time.
'''
a = input("Enter a string ")
need = a[3]
x = 0
count = 0
while x < len(a):
    if a[x] == need:
        count += 1
        if count == 2:
            print(f"The second occurence of {a[3]} is at {x}")
            break
    x += 1
if count != 2:
    print(f"{a[3]} does not occur twice in the string.")
'''

#  Write a Python program that performs the following tasks:                                          
#  1. Create a list containing the capitals of any 10 different countries. 
#  2. Extract the first character of each capital name. 
#  3. Using a while loop, check each extracted character: 
#    o If the character is a vowel (a, e, i, o, u in either uppercase or lowercase), 
#        concatenate it to a string named vowel_string. 
#    o If the character is not a vowel, concatenate it to another string named 
#        consonant_string. 
#  4. After processing all the capital names, display both strings.

#  Note: 
#       Do not use a for loop. 
#       The program should be case-insensitive when checking for vowels. 
'''
a = input("Enter the names of 10 different capitals separated by commas: ").split(",")
vowel_string = ""
consonant_string = ""
i = 0
while i < len(a):
    first_char = a[i][0]
    if first_char.lower() in "aeiou":
        vowel_string += first_char
    else:
        consonant_string += first_char
    i += 1
print("Vowel String:", vowel_string)
print("Consonant String:", consonant_string)
'''

#Write a Python program using nested for loops to print the following pattern:                  
''' 
        *
    *   *   *
*   *   *   *   *
    *   *   *
        *
''' 
''' 
n = int(input("Enter the number of rows for the pattern: "))
for i in range(n):
    for j in range(n):
        if (i == 0 and j == 2) or (i == 1 and (j == 1 or j == 2 or j == 3)) or (i == 2) or (i == 3 and (j == 1 or j == 2 or j == 3)) or (i == 4 and j == 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
''' 

# 1*2*3*4*5
# 1*2*3*4*5
# 1*2*3*4*5
# 1*2*3*4*5
# 1*2*3*4*5
'''
n = int(input("Enter the number of rows: "))
i=0
while i in range(n):
     j=0
     x=1
     a=""
     while j in range(n):
          a+=str(x)+"*"
          
          x+=1
          j+=1
     i+=1
     print(a.rstrip("*"))
'''

'''
def modify_string(text):
    result = ""
    i = 0
    
    while i in range(len(text)):
        ch = text[i]
        
        # Check if character is lowercase alphabet
        if ch >= 'a' and ch <= 'z':
            result += ch.upper()
        
        # Check if character is uppercase alphabet
        elif ch >= 'A' and ch <= 'Z':
            result += ch
        
        # Replace digits and special characters with '*'
        else:
            result += "*"
        
        i += 1
    
    return result


# Taking random string input from user
user_input = input("Enter a random string: ")

# Calling function
output = modify_string(user_input)

print("Modified String:", output)
'''

'''
marks = list(map(int,input().split()))
passed_marks = [m for m in marks if m > 40]
sq_passed_marks = [m**2 for m in passed_marks]
print("Original Marks:",marks)
print("Passed marks:",passed_marks)
print("Squared passed marks:",sq_passed_marks)
'''

# Shopping mall billing system
'''
def calculate_bill():
    amount = float(input())
    def apply_discount(value):
        if value >= 5000:
            disc = (lambda x: x * 0.10)(value)
        else:
            disc = (lambda x: x * 0.05)(value)
        final_amount = value - disc
        return final_amount
    pay_amount = apply_discount(amount)
    print(f"Final payable amount: \u20B9{pay_amount}")
calculate_bill()
'''
#---------------------------------------------------------------------------
'''
import math
import random
from datetime import datetime
name = input("Enter name ")
amount = float(input("Enter total purchase amount "))
f_amount = 0.05 * amount
res = math.ceil(f_amount)
bill_num = random.randint(1,100)
dt = datetime.today()
print(f"Bill number: {bill_num}")
print(f"Original Amount is: {amount}")
print(f"Bill Amount after including tax is: {res+amount}")
print(f"Current date and time : {dt}")
'''

'''
import random
from datetime import datetime
def q3(name, password):
    print("Select an option: 1.Sign Up or 2.Login")
    try:
        user_ch = int(input())
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")
        return
    if user_ch == 1:
        print("Enter your name: ")
        n = input().strip()
        print("Enter password: ")
        userpass = input().strip()
        print("Confirm password: ")
        confirm_pass = input().strip()
        while userpass != confirm_pass:
            print("Passwords don't match. Enter password again:")
            userpass = input().strip()
            print("Confirm password: ")
            confirm_pass = input().strip()
        print(f"Account created successfully for {n}")
    elif user_ch == 2:
        print("Enter name: ")
        na = input().strip()
        print("Select an option: 1.Login by password 2.Login by OTP")
        try:
            ch = int(input("Select a choice 1 or 2: "))
        except ValueError:
            print("Invalid choice.")
            return
        if ch == 1:
            print("Enter your password: ")
            entered_pass = input().strip()
            if entered_pass == password:
                print("Login successful!")
            else:
                print("Invalid password.")
        elif ch == 2:
            otp = random.randint(1000, 9999)
            print(f"The generated OTP is {otp}")
            try:
                o = int(input("Enter your OTP: "))
                if o == otp:
                    print("Valid OTP, Login Successful!")
                else:
                    print("Invalid OTP. Login unsuccessful.")
            except ValueError:
                print("Invalid OTP entered.")
        else:
            print("Invalid Choice")
    else:
        print("Invalid Option Selected")
name = input("Enter name: ").strip()
password = input("Enter password: ").strip()
q3(name, password)
'''