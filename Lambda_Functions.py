"""
===============================================
LAMBDA FUNCTIONS IN PYTHON
===============================================
A comprehensive guide from basic to advanced
===============================================

Table of Contents:
1. Introduction to Lambda Functions
2. Basic Syntax
3. Simple Examples
4. Lambda with Built-in Functions
5. Lambda with map()
6. Lambda with filter()
7. Lambda with reduce()
8. Lambda with sorted()
9. Lambda with conditional expressions
10. Multiple arguments
11. Advanced usage with list comprehensions
12. Lambda vs Regular Functions
13. Common pitfalls and best practices
"""

# ==============================================
# SECTION 1: INTRODUCTION TO LAMBDA FUNCTIONS
# ==============================================

"""
What is a Lambda Function?
- A lambda function is a small, anonymous function in Python
- It is defined using the 'lambda' keyword
- Lambda functions can have any number of arguments but can only have one expression
- They are also known as "inline functions" or "anonymous functions"

Why use Lambda Functions?
- They are useful when you need a small function for a short period of time
- They can be used as arguments to higher-order functions (map, filter, reduce)
- They make code more concise and readable in certain cases
"""

# ==============================================
# SECTION 2: BASIC SYNTAX
# ==============================================

"""
Basic Syntax:
    lambda arguments: expression

Key Points:
- 'lambda' is a keyword
- arguments: can be zero or more arguments
- expression: a single expression that returns a value
- No return statement needed (expression's value is automatically returned)
"""

# ==============================================
# SECTION 3: SIMPLE EXAMPLES
# ==============================================

# Example 1: Simple lambda function with no arguments
hello = lambda: "Hello, World!"
print("Example 1:", hello())  # Output: Hello, World!

# Example 2: Lambda function with one argument
square = lambda x: x ** 2
print("Example 2 - Square of 5:", square(5))  # Output: 25

# Example 3: Lambda function with two arguments
add = lambda a, b: a + b
print("Example 3 - Sum of 3 and 4:", add(3, 4))  # Output: 7

# Example 4: Lambda function with three arguments
product = lambda x, y, z: x * y * z
print("Example 4 - Product of 2, 3, 4:", product(2, 3, 4))  # Output: 24

# Example 5: Lambda function to check if a number is even
is_even = lambda x: x % 2 == 0
print("Example 5 - Is 10 even?", is_even(10))  # Output: True
print("Example 5 - Is 7 even?", is_even(7))    # Output: False

# Example 6: Lambda function to get the length of a string
length = lambda s: len(s)
print("Example 6 - Length of 'Python':", length("Python"))  # Output: 6

# Example 7: Lambda function to convert Celsius to Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 9/5) + 32
print("Example 7 - 0°C in Fahrenheit:", celsius_to_fahrenheit(0))    # Output: 32.0
print("Example 7 - 100°C in Fahrenheit:", celsius_to_fahrenheit(100))  # Output: 212.0

# Example 8: Lambda function to get the first character
first_char = lambda s: s[0] if s else ""
print("Example 8 - First char of 'Python':", first_char("Python"))  # Output: 'P'

# ==============================================
# SECTION 4: LAMBDA WITH BUILT-IN FUNCTIONS
# ==============================================

# Lambda with abs() - get absolute value
abs_square = lambda x: abs(x ** 2)
print("\nLambda with abs - (-4) squared and absolute:", abs_square(-4))  # Output: 16

# Lambda with round() - round a number
round_to_two = lambda x: round(x, 2)
print("Lambda with round - 3.14159 rounded:", round_to_two(3.14159))  # Output: 3.14

# Lambda with str() - convert to string
to_string = lambda x: str(x)
print("Lambda with str - 42 as string:", to_string(42), type(to_string(42)))

# Lambda with int() - convert to integer
to_int = lambda x: int(x)
print("Lambda with int - 3.7 as integer:", to_int(3.7))  # Output: 3

# ==============================================
# SECTION 5: LAMBDA WITH map()
# ==============================================

"""
map() function:
- Syntax: map(function, iterable)
- Applies a function to all items in an iterable
- Returns a map object (iterator)
- Lambda is commonly used with map()
"""

# Example 1: Square all numbers in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("\nmap() with lambda - Square numbers:", squared)  # [1, 4, 9, 16, 25]

# Example 2: Convert all strings to uppercase
words = ["python", "java", "c++", "javascript"]
uppercase = list(map(lambda s: s.upper(), words))
print("map() with lambda - Uppercase:", uppercase)  # ['PYTHON', 'JAVA', 'C++', 'JAVASCRIPT']

# Example 3: Add 10 to each number
nums = [5, 10, 15, 20, 25]
added_ten = list(map(lambda x: x + 10, nums))
print("map() with lambda - Add 10:", added_ten)  # [15, 20, 25, 30, 35]

# Example 4: Get lengths of all strings
fruits = ["apple", "banana", "cherry", "date"]
lengths = list(map(lambda s: len(s), fruits))
print("map() with lambda - String lengths:", lengths)  # [5, 6, 6, 4]

# Example 5: Multiple iterables with map()
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, list1, list2))
print("map() with lambda - Sum of two lists:", sums)  # [5, 7, 9]

# ==============================================
# SECTION 6: LAMBDA WITH filter()
# ==============================================

"""
filter() function:
- Syntax: filter(function, iterable)
- Filters items based on a function that returns True/False
- Returns only items where the function returns True
- Lambda is commonly used with filter()
"""

# Example 1: Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("\nfilter() with lambda - Even numbers:", evens)  # [2, 4, 6, 8, 10]

# Example 2: Filter odd numbers
odds = list(filter(lambda x: x % 2 != 0, numbers))
print("filter() with lambda - Odd numbers:", odds)  # [1, 3, 5, 7, 9]

# Example 3: Filter strings starting with 'a'
words = ["apple", "banana", "avocado", "cherry", "apricot"]
a_words = list(filter(lambda s: s.startswith('a'), words))
print("filter() with lambda - Words starting with 'a':", a_words)  # ['apple', 'avocado', 'apricot']

# Example 4: Filter numbers greater than 5
nums = [1, 6, 3, 8, 2, 9, 4, 7]
greater_than_5 = list(filter(lambda x: x > 5, nums))
print("filter() with lambda - Numbers > 5:", greater_than_5)  # [6, 8, 9, 7]

# Example 5: Filter palindromes
words = ["radar", "hello", "level", "world", "civic"]
palindromes = list(filter(lambda s: s == s[::-1], words))
print("filter() with lambda - Palindromes:", palindromes)  # ['radar', 'level', 'civic']

# Example 6: Filter lists with length > 3
nested = [[1, 2], [1, 2, 3, 4], [1], [1, 2, 3], [1, 2]]
filtered = list(filter(lambda lst: len(lst) > 3, nested))
print("filter() with lambda - Lists with length > 3:", filtered)  # [[1, 2, 3, 4]]

# ==============================================
# SECTION 7: LAMBDA WITH reduce()
# ==============================================

"""
reduce() function:
- Syntax: reduce(function, iterable, initial_value)
- Applies a function to pairs of items cumulatively
- Returns a single value
- Must be imported from functools
"""

from functools import reduce

# Example 1: Sum all numbers in a list
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print("\nreduce() with lambda - Sum:", total)  # Output: 15

# Example 2: Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print("reduce() with lambda - Product:", product)  # Output: 120

# Example 3: Find maximum number
max_num = reduce(lambda x, y: x if x > y else y, numbers)
print("reduce() with lambda - Maximum:", max_num)  # Output: 5

# Example 3b: Find minimum number
min_num = reduce(lambda x, y: x if x < y else y, numbers)
print("reduce() with lambda - Minimum:", min_num)  # Output: 1

# Example 4: Concatenate strings
words = ["Python", " is", " awesome"]
result = reduce(lambda x, y: x + y, words)
print("reduce() with lambda - Concatenated:", result)  # Output: "Python is awesome"

# Example 5: Find the longest word
words = ["cat", "elephant", "dog", "hippopotamus"]
longest = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print("reduce() with lambda - Longest word:", longest)  # Output: "hippopotamus"

# ==============================================
# SECTION 8: LAMBDA WITH sorted()
# ==============================================

"""
sorted() function with key parameter:
- Syntax: sorted(iterable, key=function)
- key parameter specifies a function to be called on each list element
- Lambda is commonly used as the key function
"""

# Example 1: Sort by length of string
words = ["cat", "elephant", "dog", "hippopotamus", "ant"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print("\nsorted() with lambda - By length:", sorted_by_length)  
# ['cat', 'dog', 'ant', 'elephant', 'hippopotamus']

# Example 2: Sort by last character
words = ["apple", "banana", "cherry", "date"]
sorted_by_last = sorted(words, key=lambda x: x[-1])
print("sorted() with lambda - By last char:", sorted_by_last)  
# ['banana', 'date', 'apple', 'cherry']

# Example 3: Sort list of tuples by second element
pairs = [(1, 5), (3, 2), (2, 8), (4, 1)]
sorted_by_second = sorted(pairs, key=lambda x: x[1])
print("sorted() with lambda - Tuples by 2nd element:", sorted_by_second)  
# [(4, 1), (3, 2), (1, 5), (2, 8)]

# Example 4: Sort dictionary by values
d = {'a': 4, 'b': 2, 'c': 5, 'd': 1}
sorted_dict = sorted(d.items(), key=lambda x: x[1])
print("sorted() with lambda - Dict by value:", sorted_dict)  
# [('d', 1), ('b', 2), ('a', 4), ('c', 5)]

# Example 5: Reverse sort
numbers = [5, 2, 8, 1, 9]
sorted_reverse = sorted(numbers, key=lambda x: -x)
print("sorted() with lambda - Reverse:", sorted_reverse)  # [9, 8, 5, 2, 1]

# ==============================================
# SECTION 9: LAMBDA WITH CONDITIONAL EXPRESSIONS
# ==============================================

"""
Lambda with conditional expressions (ternary operator):
    lambda arguments: value_if_true if condition else value_if_false
"""

# Example 1: Check if a number is positive, negative, or zero
check_num = lambda x: "positive" if x > 0 else ("negative" if x < 0 else "zero")
print("\nConditional lambda - Check 5:", check_num(5))    # positive
print("Conditional lambda - Check -3:", check_num(-3))   # negative
print("Conditional lambda - Check 0:", check_num(0))    # zero

# Example 2: Return absolute value
abs_value = lambda x: x if x >= 0 else -x
print("Conditional lambda - Abs(-7):", abs_value(-7))    # 7
print("Conditional lambda - Abs(5):", abs_value(5))      # 5

# Example 3: Classify by age
age_group = lambda age: "Child" if age < 13 else ("Teen" if age < 20 else "Adult")
print("Conditional lambda - Age 8:", age_group(8))       # Child
print("Conditional lambda - Age 15:", age_group(15))    # Teen
print("Conditional lambda - Age 25:", age_group(25))    # Adult

# Example 4: Return "Even" or "Odd"
even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print("Conditional lambda - 10:", even_odd(10))  # Even
print("Conditional lambda - 7:", even_odd(7))    # Odd

# ==============================================
# SECTION 10: MULTIPLE ARGUMENTS
# ==============================================

# Example 1: Two arguments - calculate area
area_rectangle = lambda l, w: l * w
print("\nTwo args - Area of 5x3:", area_rectangle(5, 3))  # 15

# Example 2: Three arguments - volume of cuboid
volume = lambda l, w, h: l * w * h
print("Three args - Volume of 2x3x4:", volume(2, 3, 4))  # 24

# Example 3: Multiple arguments - power operation
power = lambda base, exp: base ** exp
print("Two args - 2^10:", power(2, 10))  # 1024

# Example 4: Multiple arguments with default values (NOT directly possible)
# Use wrapper function for defaults
power_with_default = lambda base, exp=2: base ** exp
print("Default args - 5^2:", power_with_default(5))   # 25
print("Default args - 5^3:", power_with_default(5, 3))  # 125

# ==============================================
# SECTION 11: ADVANCED - LIST COMPREHENSIONS
# ==============================================

# Lambda with list comprehension - create list of lambda functions
funcs = [lambda x, i=i: i * x for i in range(5)]
print("\nList of lambda functions:")
print("  funcs[0](2):", funcs[0](2))  # 0*2 = 0
print("  funcs[1](2):", funcs[1](2))  # 1*2 = 2
print("  funcs[2](2):", funcs[2](2))  # 2*2 = 4
print("  funcs[3](2):", funcs[3](2))  # 3*2 = 6
print("  funcs[4](2):", funcs[4](2))  # 4*2 = 8

# Advanced: Nested lambda
nested_lambda = lambda x: (lambda y: x + y)
add_five = nested_lambda(5)
print("Nested lambda - add_five(3):", add_five(3))  # 8

# Advanced: Lambda returning lambda
multiplier = lambda x: lambda y: x * y
double = multiplier(2)
triple = multiplier(3)
print("Lambda returning lambda - double(5):", double(5))   # 10
print("Lambda returning lambda - triple(5):", triple(5))   # 15

# ==============================================
# SECTION 12: LAMBDA VS REGULAR FUNCTIONS
# ==============================================

"""
Comparison: Lambda vs Regular Functions

Regular Function:
    def square(x):
        return x ** 2

Equivalent Lambda:
    square = lambda x: x ** 2

When to use Lambda:
- Small, one-time use functions
- As arguments to higher-order functions
- When function brevity is important

When to use Regular Functions:
- Complex logic requiring multiple statements
- When you need docstrings
- When function will be reused multiple times
- When debugging is important
"""

# Example comparison
def regular_add(a, b):
    """Regular function to add two numbers"""
    return a + b

lambda_add = lambda a, b: a + b  # Equivalent one-liner

print("\nRegular function:", regular_add(3, 4))  # 7
print("Lambda function:", lambda_add(3, 4))       # 7

# ==============================================
# SECTION 13: COMMON PITFALLS AND BEST PRACTICES
# ==============================================

"""
Common Pitfalls:
1. Forgetting that lambda can only have one expression
2. Trying to use statements (if/else is OK, loops are NOT)
3. Not understanding closure in loops

Best Practices:
1. Keep lambda functions simple and short
2. Use meaningful variable names when assigning lambda
3. Prefer list comprehensions over map/filter with lambda when clearer
4. Use regular functions for complex logic
"""

# Pitfall: Lambda cannot have statements (except conditional)
# This will cause SyntaxError:
# lambda x: for i in range(x): print(i)  # WRONG!

# Pitfall: Lambda with mutable default arguments
# counter = lambda i=[]: i.append(1)  # WRONG! Don't do this

# Correct way to avoid closure issues in loops
# Use default argument to capture current value
funcs_correct = [lambda x, i=i: i * x for i in range(5)]

# ==============================================
# SUMMARY
# ==============================================

print("\n" + "="*50)
print("LAMBDA FUNCTIONS - KEY TAKEAWAYS")
print("="*50)
print("""
1. Lambda functions are anonymous functions
   Syntax: lambda arguments: expression

2. They are useful for short, one-time operations

3. Common use cases:
   - map(), filter(), reduce()
   - sorted() key parameter
   - Event handlers in GUI
   - Quick operations in data processing

4. Limitations:
   - Only one expression
   - No statements (for, while, etc.)
   - No docstrings
   - Hard to debug

5. Best Practice:
   - Keep it simple
   - Use for small operations
   - Prefer regular functions for complex logic
""")
