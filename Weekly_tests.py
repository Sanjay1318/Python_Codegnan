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