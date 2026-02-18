"""
================================================================================
                    PYTHON FUNCTIONS - COMPLETE GUIDE
================================================================================
A comprehensive guide to Python functions from basic to advanced.
Each section includes executable code examples with explanations.
================================================================================
"""

# ================================================================================
#                               BASIC CONCEPTS
# ================================================================================
"""
A function is a block of code with a particular functionality.
It's executed only when the function is called.
Functions help in code reusability and modularity.
"""

# Example 1: Simple function definition and calling
def greet():
    """A simple function that prints a greeting."""
    print("Hello, World!")

# Calling the function
greet()  # Output: Hello, World!
greet()  # Can be called multiple times


# ================================================================================
#                        ADVANTAGES OF FUNCTIONS
# ================================================================================
"""
1. CODE REUSABILITY: Write once, use many times
2. MODULARITY: Breaks down complex problems into smaller parts
3. ABSTRACTION: Hide implementation details
4. EASIER TESTING: Functions can be tested individually
5. FLEXIBILITY: Parameters make functions adaptable
6. READABILITY: Code becomes more organized
"""

# Example demonstrating reusability
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

# Using the same function multiple times
result1 = add(5, 3)
result2 = add(10, 20)
result3 = add(100, 200)
print(f"add(5, 3) = {result1}")    # 8
print(f"add(10, 20) = {result2}")  # 30
print(f"add(100, 200) = {result3}") # 300


# ================================================================================
#                          TYPES OF FUNCTIONS
# ================================================================================

# Type 1: Built-in Functions (pre-defined by Python)
print("\n--- Built-in Functions ---")
numbers = [1, 2, 3, 4, 5]
print(f"len([1,2,3,4,5]) = {len(numbers)}")           # 5
print(f"max([1,2,3,4,5]) = {max(numbers)}")           # 5
print(f"min([1,2,3,4,5]) = {min(numbers)}")           # 1
print(f"sum([1,2,3,4,5]) = {sum(numbers)}")           # 15
print(f"sorted([5,2,1,4,3]) = {sorted([5,2,1,4,3])}") # [1,2,3,4,5]
print(f"type(42) = {type(42)}")                         # <class 'int'>
print(f"str(42) = {str(42)}, type = {type(str(42))}")  # '42', <class 'str'>
print(f"abs(-42) = {abs(-42)}")                         # 42
print(f"range(5) = {list(range(5))}")                   # [0,1,2,3,4]

# Type 2: User-Defined Functions
def greet_user(name):
    """User-defined function."""
    return f"Hello, {name}!"

print(f"\n{greet_user('John')}")  # Hello, John!

# Type 3: Lambda Functions (anonymous functions)
square = lambda x: x ** 2
print(f"\nLambda - square(5) = {square(5)}")  # 25

add_lambda = lambda a, b: a + b
print(f"Lambda - add_lambda(3, 5) = {add_lambda(3, 5)}")  # 8

# Type 4: Recursive Functions
def factorial(n):
    """Calculate factorial using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"\nRecursion - factorial(5) = {factorial(5)}")  # 120

# Type 5: Generator Functions
def count_generator(n):
    """Generate numbers from 1 to n."""
    for i in range(1, n + 1):
        yield i

print("\nGenerator - count_generator(5):")
for num in count_generator(5):
    print(num, end=" ")  # 1 2 3 4 5

# Type 6: Higher-Order Functions
def apply_operation(func, value):
    """Takes a function as parameter."""
    return func(value)

def double(x):
    return x * 2

print(f"\n\nHigher-order - apply_operation(double, 10) = {apply_operation(double, 10)}")  # 20

# Type 7: Methods (functions associated with objects)
print("\nMethods:")
print(f"'hello'.upper() = {'hello'.upper()}")           # 'HELLO'
print(f"[1,2,3].append(4) = {[1,2,3]}")                  # [1,2,3,4]
print(f"'hello world'.title() = {'hello world'.title()}") # 'Hello World'

# Type 8: Special Functions (__init__, __str__, etc.)
class Person:
    """Class demonstrating special methods."""
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Person: {self.name}"

p = Person("John")
print(f"\nSpecial methods - __str__: {p}")  # Person: John


# ================================================================================
#                           BASIC FUNCTIONS
# ================================================================================

# Function with parameters and return value
def multiply(a, b):
    """Multiply two numbers."""
    return a * b

result = multiply(4, 5)
print(f"\nmultiply(4, 5) = {result}")  # 20


# ================================================================================
#                      PARAMETERS & ARGUMENTS
# ================================================================================

# 1. Positional Arguments
def introduce(name, age):
    """Positional arguments example."""
    print(f"My name is {name} and I am {age} years old")

introduce("John", 25)  # name="John", age=25

# 2. Keyword Arguments
introduce(age=30, name="Jane")  # Order doesn't matter

# 3. Default Parameters
def greet_person(name, message="Hello"):
    """Default parameter example."""
    print(f"{message}, {name}!")

greet_person("John")        # Hello, John!
greet_person("John", "Hi")  # Hi, John!

# 4. *args - Variable Positional Arguments
def sum_all(*args):
    """Sum all given numbers."""
    total = 0
    for num in args:
        total += num
    return total

print(f"\nsum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")  # 15
print(f"sum_all(10, 20) = {sum_all(10, 20)}")                   # 30

# 5. **kwargs - Variable Keyword Arguments
def print_info(**kwargs):
    """Print all keyword arguments."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\nprint_info:")
print_info(name="John", age=25, city="NYC")

# 6. Combining *args and **kwargs
def mixed_function(*args, **kwargs):
    """Combine positional and keyword arguments."""
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print("\nmixed_function(1, 2, 3, name='John', age=25):")
mixed_function(1, 2, 3, name="John", age=25)


# ================================================================================
#                           RETURN VALUES
# ================================================================================

# 1. Return Single Value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"\nadd_numbers(5, 3) = {result}")  # 8

# 2. Return Multiple Values (returns a tuple)
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

minimum, maximum, average = get_stats([1, 2, 3, 4, 5])
print(f"Stats: min={minimum}, max={maximum}, avg={average}")  # min=1, max=5, avg=3.0

# 3. Return Nothing (None)
def greet_no_return(name):
    print(f"Hello, {name}!")

result = greet_no_return("John")
print(f"greet_no_return returns: {result}")  # None

# 4. Early Return
def find_first_even(numbers):
    """Find first even number in a list."""
    for num in numbers:
        if num % 2 == 0:
            return num
    return None

print(f"\nfind_first_even([1,3,5,6,7]) = {find_first_even([1,3,5,6,7])}")  # 6
print(f"find_first_even([1,3,5,7]) = {find_first_even([1,3,5,7])}")        # None


# ================================================================================
#                         LAMBDA FUNCTIONS
# ================================================================================

# 1. Basic Lambda
square_lambda = lambda x: x ** 2
print(f"\nsquare_lambda(5) = {square_lambda(5)}")  # 25

# 2. Lambda with Multiple Arguments
add_lambda = lambda a, b: a + b
print(f"add_lambda(3, 5) = {add_lambda(3, 5)}")  # 8

# 3. Common Lambda Uses with Built-in Functions
numbers = [1, 2, 3, 4, 5]

# map() - applies function to all items
squared = list(map(lambda x: x**2, numbers))
print(f"\nmap with lambda - squared: {squared}")  # [1, 4, 9, 16, 25]

# filter() - filters based on condition
numbers2 = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers2))
print(f"filter with lambda - evens: {evens}")  # [2, 4, 6]

# sorted() with key
names = ["Charlie", "Alice", "Bob"]
sorted_names = sorted(names, key=lambda x: len(x))
print(f"sorted with lambda - sorted_names: {sorted_names}")  # ['Bob', 'Alice', 'Charlie']


# ================================================================================
#                         NESTED FUNCTIONS
# ================================================================================

# 1. Function Inside Function
def outer_function():
    print("Outer function called")
    
    def inner_function():
        print("Inner function called")
    
    inner_function()

print("\nouter_function():")
outer_function()

# 2. Closures
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print(f"\nadd_five(10) = {add_five(10)}")  # 15

# 3. Practical Closure Example
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(f"double(5) = {double(5)}")  # 10
print(f"triple(5) = {triple(5)}")  # 15


# ================================================================================
#                            DECORATORS
# ================================================================================

# 1. Basic Decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

print("\nsay_hello() with decorator:")
say_hello()

# 2. Decorator with Arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet_decorated(name):
    print(f"Hello, {name}!")

print("\ngreet_decorated('John') with @repeat(times=3):")
greet_decorated("John")

# 3. Preserving Function Metadata (using functools.wraps)
from functools import wraps

def my_decorator_preserved(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@my_decorator_preserved
def example():
    """Example function docstring"""
    pass

print(f"\nexample.__name__ = {example.__name__}")  # example (not wrapper)
print(f"example.__doc__ = {example.__doc__}")    # Example function docstring


# ================================================================================
#                           GENERATORS
# ================================================================================

# 1. Basic Generator
def count_up_to(n):
    """Count from 1 to n."""
    count = 1
    while count <= n:
        yield count
        count += 1

print("\ncount_up_to(5):")
for num in count_up_to(5):
    print(num, end=" ")  # 1 2 3 4 5

# 2. Generator Expressions
squares_gen = (x**2 for x in range(10))
print(f"\n\nGenerator expression - list(squares_gen): {list(squares_gen)}")  # [0,1,4,9,16,25,36,49,64,81]

# 3. Yield From
def chain_generators(*generators):
    """Chain multiple generators together."""
    for gen in generators:
        yield from gen

print("\nchain_generators([1,2], [3,4], [5,6]):")
for num in chain_generators([1, 2], [3, 4], [5, 6]):
    print(num, end=" ")  # 1 2 3 4 5 6


# ================================================================================
#                           RECURSION
# ================================================================================

# 1. Basic Recursion - Factorial
def factorial(n):
    """Calculate factorial recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"\n\nfactorial(5) = {factorial(5)}")  # 120

# 2. Fibonacci with Recursion
def fibonacci(n):
    """Calculate nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("fibonacci(0-9):")
for i in range(10):
    print(fibonacci(i), end=" ")  # 0 1 1 2 3 5 8 13 21 34

# 3. Recursion with Memoization (using lru_cache)
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memo(n):
    """Fibonacci with memoization for better performance."""
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

print(f"\n\nfibonacci_memo(100) = {fibonacci_memo(100)}")  # Much faster!


# ================================================================================
#                         SCOPE (LEGB RULE)
# ================================================================================
"""
LEGB Rule: Python looks for variables in order:
1. Local - Inside current function
2. Enclosing - Inside enclosing functions
3. Global - At module level
4. Built-in - Python's built-in names
"""

# 1. Local Scope
x = 10
def local_example():
    x = 5  # This is a LOCAL variable
    print(f"Inside local_example: x = {x}")  # Prints 5

local_example()
print(f"Outside function: x = {x}")  # Prints 10

# 2. Global Scope
x = 10
def global_example():
    global x  # Declare we're using global x
    x = 5
    print(f"Inside global_example: x = {x}")  # Prints 5

global_example()
print(f"After function call: x = {x}")  # Prints 5

# 3. Enclosing (Nonlocal) Scope
def outer():
    x = 10
    def inner():
        nonlocal x  # Use enclosing function's x
        x = 5
    inner()
    print(f"Inside outer: x = {x}")  # Prints 5

outer()


# ================================================================================
#                           DOCSTRINGS
# ================================================================================

# 1. Single Line Docstring
def greet_single(name):
    """Greet a person by name."""
    return f"Hello, {name}!"

print(f"\n{greet_single('John')}")  # Hello, John!

# 2. Multi-Line Docstring
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
    
    Returns:
        The area of the rectangle (length * width)
    """
    return length * width

print(f"calculate_area(5, 3) = {calculate_area(5, 3)}")  # 15

# 3. Accessing Docstrings
def example_doc():
    """This is a docstring"""
    pass

print(f"\nexample_doc.__doc__ = {example_doc.__doc__}")  # This is a docstring


# ================================================================================
#                        TYPE HINTS (Python 3.5+)
# ================================================================================

# 1. Basic Type Hints
def greet_type_hint(name: str) -> str:
    return f"Hello, {name}!"

print(f"\n{greet_type_hint('John')}")  # Hello, John!

# 2. Type Hints for Variables
count: int = 10
name: str = "John"
prices: list[float] = [1.99, 2.99, 3.99]
print(f"\ncount: {count}, name: {name}, prices: {prices}")

# 3. Advanced Type Hints
from typing import List, Dict, Tuple, Optional, Union

def process_data(
    data: List[int],
    options: Optional[Dict[str, str]] = None
) -> Tuple[int, str]:
    """Process data with optional configuration."""
    return len(data), "processed"

result = process_data([1, 2, 3])
print(f"\nprocess_data([1,2,3]) = {result}")  # (3, 'processed')

# Union type
def parse_input(value: Union[int, str]) -> int:
    if isinstance(value, str):
        return int(value)
    return value

print(f"parse_input('42') = {parse_input('42')}")  # 42
print(f"parse_input(42) = {parse_input(42)}")      # 42

# 4. Callable Type Hints
from typing import Callable

def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

result = apply_function(lambda x, y: x + y, 5, 3)
print(f"\napply_function(lambda x,y: x+y, 5, 3) = {result}")  # 8


# ================================================================================
#                      FUNCTION ANNOTATIONS
# ================================================================================

def greet_annotation(name: str, age: int = 25) -> str:
    return f"Hello, {name}!"

print(f"\ngreet_annotation.__annotations__ = {greet_annotation.__annotations__}")
# {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}


# ================================================================================
#                      SPECIAL FUNCTION ATTRIBUTES
# ================================================================================

def example_function(x, y=10):
    """Example function"""
    pass

print(f"\nexample_function.__name__ = {example_function.__name__}")    # example_function
print(f"example_function.__doc__ = {example_function.__doc__}")       # Example function
print(f"example_function.__defaults__ = {example_function.__defaults__}")  # (10,)


# ================================================================================
#                        PRACTICAL EXAMPLES
# ================================================================================

# 1. Validation Decorator
def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Arguments must be positive")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def divide(a, b):
    return a / b

print(f"\ndivide(10, 2) = {divide(10, 2)}")  # 5.0
# divide(-5, 2) would raise ValueError

# 2. Cache Decorator (Memoization)
def memoize(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci_cache(n):
    if n < 2:
        return n
    return fibonacci_cache(n-1) + fibonacci_cache(n-2)

print(f"fibonacci_cache(50) = {fibonacci_cache(50)}")  # Fast with caching!

# 3. Timing Decorator
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.6f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.001)
    return "Done!"

print(f"\nslow_function() = {slow_function()}")

# 4. Function Composition
def compose(f, g):
    return lambda x: f(g(x))

square = lambda x: x ** 2
add_five = lambda x: x + 5

square_after_add = compose(square, add_five)
print(f"\nsquare_after_add(3) = {square_after_add(3)}")  # (3 + 5) ** 2 = 64

# 5. Partial Function
from functools import partial

def power(base, exponent):
    return base ** exponent

square_partial = partial(power, exponent=2)
cube_partial = partial(power, exponent=3)

print(f"square_partial(5) = {square_partial(5)}")  # 25
print(f"cube_partial(5) = {cube_partial(5)}")      # 125


# ================================================================================
#                          BEST PRACTICES
# ================================================================================
"""
1. Use meaningful function names
   - Good: calculate_area()
   - Bad: calc()

2. Keep functions small and focused
   - One function = One responsibility

3. Use docstrings to document functions

4. Use type hints for better code clarity

5. Use default arguments wisely
   - Default values should be immutable (None, not [])

6. Handle exceptions appropriately

7. Use *args and **kwargs for flexible functions

8. Consider using generators for large datasets

9. Use decorators to avoid code repetition

10. Write pure functions when possible
    - Same input = Same output
    - No side effects
"""


# ================================================================================
#                            SUMMARY
# ================================================================================
"""
Functions are fundamental building blocks in Python that:
- Improve code reusability and modularity
- Make code easier to test and debug
- Support various patterns: recursion, closures, decorators
- Can be customized with parameters, arguments, and return values
- Can use advanced features like generators and type hints

Master these concepts to write clean, efficient, and Pythonic code!
"""

print("\n" + "="*80)
print("                    PYTHON FUNCTIONS GUIDE COMPLETE!")
print("="*80)
print("""
Topics Covered:
✓ Basic Concepts
✓ Advantages of Functions (6 points)
✓ Types of Functions (8 types)
✓ Basic Functions
✓ Parameters & Arguments
✓ Return Values
✓ Lambda Functions
✓ Nested Functions & Closures
✓ Decorators
✓ Generators
✓ Recursion
✓ Scope (LEGB Rule)
✓ Docstrings
✓ Type Hints
✓ Function Annotations
✓ Special Function Attributes
✓ Practical Examples
✓ Best Practices
""")
print("="*80)
print("                    Happy Coding! 🚀")
print("="*80)
