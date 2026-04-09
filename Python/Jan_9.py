# Built - in functions in Strings
''' These are the pre defined functions that can be used directly in any python file

        1. len(obj) - returns the length of the object / returns the number of elements present in any iterable

s = "Python Programming"
print(len(s)) # returns 18, spaces in between are also counted

        2. min() and max() - These returns minimum and maximum elements repectively
        
s = "Python Programming"
print(min(s)) # returns space( ) as space has the least ASCII value
print(max(s)) # returns y , because y has the highest ASCII value

        3. ord() - It returns the ASCII value of a given character
        
print(ord("p")) # returns 112 , ASCII value of p is 112

        4. chr() - It returns the character corresponding to given ASCII value

print(chr(98))   # returns b, the character assigned to ASCII value 98 is b

        5. sorted() - It returns the list of given elements in sorted order

s = "desutvwchab"
print(sorted(s)) # returns ['a', 'b', 'c', 'd', 'e', 'h', 's', 't', 'u', 'v', 'w']
print(sorted(s, reverse = True)) # returns ['w', 'v', 'u', 't', 's', 'h', 'e', 'd', 'c', 'b', 'a']
'''

# Accessing elements using indexing
''' Every element in the string has it's own place value called as index
     There are 2 ways of giving indices :
         1. Zero based indexing : It runs from 0 to n-1, where n is the number of characters
                                                             It runs from left to right (starting to ending)

        2. Negative based indexing : It runs from -1 to -n
                                                                    It runs from right to left(ending to starting)

s = "Python Programming"
print(s[7])    # returns p
print(s[-7])  # returns r
print(s[99]) # IndexError :  string index out of range
'''

# WAP to check if the first character and last character of the string is same. Output should be in True or False
'''
s = input("Enter yor string ")
print(s[0] is s[-1])
'''

# WAP to check if the middle character of the given string is a vowel. Always an odd length string is gauranteed. Output should be True or False
'''
s = input("Enter String ")
middle_letter = len(s) // 2

print(s[middle_letter] in ["a","e","i","o","u","A","E","I","O","U"])  # or print(s[middle_letter] in "aeiouAEIOU")
'''

# WAP to check if the second character from the end is a consonant
'''
s = input("Enter String ")
end2 = s[-2]

print(end2 not in ["a","e","i","o","u","A","E","I","O","U"])
'''
'''
To access single element , we follow the below syntax
string_obj[index]

To access a substring from the given string, we use the start index, stop index and step if needed.
This operation on strings is called as slicing.
        Syntax : str_obj[start_index : stop_index + 1 : step_size] 
These 3 values (start_index : stop_index , step_size) are optional the default values of these are as follows :
        start_index = starts from the beggining of the string that is index 0
        stop_index = stops at the ending of the string that is index of n - 1
        step_size = Default step size is 1 considering every char in the given range

s = "Python Programming"
print(s[2:10]) # thon Pro
print(s[2:10:2]) # to r
print(s[ : :2]) # Pto rgamn
print(s[ : ]) # Python Programming
'''



















