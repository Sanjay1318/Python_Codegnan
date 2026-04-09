# Data Types

# String :
''' A String is an immutable, ordered sequence of characters enclosed in quotation marks
    Multi line String :  ("""

                                                        """)

    mul_str = """ Python
    Programming
    Language"""
    print(mul_str)
                                    
    Single line Strings : (" ")
    
    var = "Good Boyyyyy @ [|0]{(0:)}"
    print(var)      # prints Good Boyyyyy @ [|0]{(0:)}

    Only quotation marks without any characters in between is an empty string

    emp_str = ""
    print(emp_str)
'''
# Properties of a String:
'''
    1. immutable :
        Changes in an existing object is not possible

    2. ordered :
        Order of insertion of characters is preserved through out its existence in memory

    3. indexable :
        Elements can be accessed using indexing

    4. string input :
        input() function considers every input by user as string object only by default

        name = input("Enter name ")
        print(type(name))  # str
'''
# Usage of backslash in strings (\) :
''' 1. It can be used as escape character
     2. It can be used to introduce new line character, tabspace character, etc....
     3. It can be used for line continuation in paragraphs to improve readability
         print("some content"
            \"continues the content in the same line as a continue paragraph")

        \t     : for tab space
        \n    : for new line
'''
# Operations on Strings 
''' 1. Operators on strings :
                a.) String Concatenation (+) : Joining 2 or more strings together

# WAP to take first name and last name as two lines of input and print the full name

firstname = input("Enter first name ")
lastname = input("Enter last name ")

print("Full name is " , firstname + " " + lastname)

                b.) String Repetition (*) : Repeats the character in the string given number of times

# WAP to print the following pattern
#  ******
#  ******
#  ******

print("*" * 6)
print("*" * 6)
print("*" * 6)

                c.) Relational Operators (<,>) works by comparing ASCII values

                d.) Logical Operators try to convert strings to boolean internally. For a non empty string boolean value will be True
                    and for empty string it will be False

                e.) Arthimetic Operators that do not work cannot be used as compound assignment operators for updating values (only + and * works)

                f.) identity and membership operators can be used

                g.) unsupported operators will result in TypeError
'''





        
