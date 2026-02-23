"""
===============================================
NESTED FUNCTIONS IN PYTHON
===============================================
A comprehensive guide from basic to advanced
==============================================

Table of Contents:
1. Introduction to Nested Functions
2. Basic Syntax and Definition
3. Simple Examples
4. Scope and Closures
5. Returning Nested Functions
6. Decorators (Advanced)
7. Practical Applications
8. Nonlocal Keyword
9. Multiple Levels of Nesting
10. Nested Functions with Arguments
11. Common Patterns and Use Cases
12. Best Practices and Pitfalls
"""

# ==============================================
# SECTION 1: INTRODUCTION TO NESTED FUNCTIONS
# ==============================================

"""
What is a Nested Function?
- A nested function is a function defined inside another function
- The inner function is "nested" within the outer function
- Also known as "inner functions" or "local functions"

Why use Nested Functions?
1. Encapsulation: Hide helper functions from the outside world
2. Closure: Create factory functions that remember values
3. Decorators: Modify behavior of other functions
4. Organization: Group related helper functions together
5. Data hiding: Keep implementation details private
"""

# ==============================================
# SECTION 2: BASIC SYNTAX AND DEFINITION
# ==============================================

"""
Basic Syntax:
    def outer_function(parameters):
        # outer function code
        def inner_function():
            # inner function code
        # call inner function or return it
"""

# ==============================================
# SECTION 3: SIMPLE EXAMPLES
# ==============================================

# Example 1: Basic nested function
def greet():
    """Outer function"""
    def say_hello():
        """Inner function"""
        print("Hello!")
    
    # Call the inner function
    say_hello()

print("Example 1 - Basic nested function:")
greet()  # Output: Hello!

# Example 2: Nested function with parameters
def calculate_area(shape):
    """Calculate area based on shape type"""
    
    def rectangle_area(width, height):
        return width * height
    
    def circle_area(radius):
        import math
        return math.pi * radius ** 2
    
    if shape == "rectangle":
        return rectangle_area(5, 3)
    elif shape == "circle":
        return circle_area(4)

print("\nExample 2 - Nested function with parameters:")
print("Rectangle area:", calculate_area("rectangle"))  # Output: 15
print("Circle area:", round(calculate_area("circle"), 2))  # Output: 50.27

# Example 3: Nested function that does multiple operations
def string_processor(text):
    """Process a string with multiple operations"""
    
    def remove_spaces(s):
        return s.replace(" ", "")
    
    def to_uppercase(s):
        return s.upper()
    
    def add_exclamation(s):
        return s + "!"
    
    result = remove_spaces(text)
    result = to_uppercase(result)
    result = add_exclamation(result)
    return result

print("\nExample 3 - Multiple nested functions:")
print(string_processor("hello world"))  # Output: HELLOWORLD!

# ==============================================
# SECTION 4: SCOPE AND CLOSURES
# ==============================================

"""
Understanding Scope in Nested Functions:
- LEGB Rule: Local, Enclosing, Global, Built-in
- Inner functions can access outer function's variables
- Outer functions cannot access inner function's variables

Closure:
- A closure is created when a nested function references variables 
  from its enclosing scope
- The inner function "remembers" the environment in which it was created
"""

# Example 1: Inner function accessing outer variables
def outer():
    x = 10
    
    def inner():
        print(f"Inner function accessing x: {x}")
    
    inner()

print("Example 4 - Accessing outer variables:")
outer()  # Output: Inner function accessing x: 10

# Example 2: Closure - inner function remembers outer variables
def outer_with_closure():
    x = 10
    
    def inner():
        return x * 2
    
    return inner  # Return the function, not calling it

closure = outer_with_closure()
print("\nExample 5 - Closure:")
print("Calling closure:", closure())  # Output: 20
print("x is still accessible through closure:", closure())  # Still returns 20

# Example 3: Multiple closures from same function
def multiplier_factory(n):
    """Factory function that creates multiplier functions"""
    
    def multiply(x):
        return x * n
    
    return multiply

double = multiplier_factory(2)
triple = multiplier_factory(3)
print("\nExample 6 - Factory function:")
print("Double of 5:", double(5))   # Output: 10
print("Triple of 5:", triple(5))   # Output: 15
print("Double of 10:", double(10))  # Output: 20

# ==============================================
# SECTION 5: RETURNING NESTED FUNCTIONS
# ==============================================

"""
Why Return Nested Functions?
- Create function factories
- Implement decorators
- Build customizable functions
- Achieve data hiding
"""

# Example 1: Function that returns a function
def power_factory(power):
    """Create a function that raises to a specific power"""
    
    def power_func(base):
        return base ** power
    
    return power_func

square = power_factory(2)
cube = power_factory(3)
fourth_power = power_factory(4)

print("\nExample 7 - Function returning function:")
print("Square of 4:", square(4))    # 16
print("Cube of 4:", cube(4))        # 64
print("4th power of 4:", fourth_power(4))  # 256

# Example 2: Greeting factory
def greeting_factory(greeting):
    """Create a personalized greeting function"""
    
    def greet(name):
        return f"{greeting}, {name}!"
    
    return greet

say_hello = greeting_factory("Hello")
say_goodbye = greeting_factory("Goodbye")
say_welcome = greeting_factory("Welcome")

print("\nExample 8 - Greeting factory:")
print(say_hello("John"))      # Hello, John!
print(say_goodbye("John"))    # Goodbye, John!
print(say_welcome("John"))    # Welcome, John!

# Example 3: Counter factory
def counter_factory():
    """Create a counter function"""
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

counter1 = counter_factory()
counter2 = counter_factory()

print("\nExample 9 - Counter factory:")
print("counter1():", counter1())  # 1
print("counter1():", counter1())  # 2
print("counter1():", counter1())  # 3
print("counter2():", counter2())  # 1 (independent counter)

# ==============================================
# SECTION 6: DECORATORS (ADVANCED)
# ==============================================

"""
Decorators:
- A decorator is a function that takes another function as input
- It extends the behavior of the original function
- Uses nested functions with closures

Decorator Syntax:
    @decorator_name
    def function_to_decorate():
        pass
"""

# Example 1: Basic decorator
def my_decorator(func):
    """Decorator that adds functionality before and after"""
    
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs")
    
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

print("\nExample 10 - Basic decorator:")
say_whee()

# Example 2: Decorator with arguments
def timer_decorator(func):
    """Decorator that measures execution time"""
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Function completed"

print("\nExample 11 - Decorator with arguments:")
result = slow_function()
print("Result:", result)

# Example 3: Practical decorator - logging
def log_calls(func):
    """Decorator to log function calls"""
    
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    
    return wrapper

@log_calls
def add(a, b):
    return a + b

@log_calls
def multiply(a, b):
    return a * b

print("\nExample 12 - Logging decorator:")
add(3, 4)
multiply(5, 6)

# Example 4: Practical decorator - authentication
def require_authentication(func):
    """Decorator to check authentication"""
    is_authenticated = False  # This would typically come from a session
    
    def wrapper(*args, **kwargs):
        if is_authenticated:
            return func(*args, **kwargs)
        else:
            return "Authentication required!"
    
    return wrapper

@require_authentication
def get_user_data():
    return "User data: John, 30 years old"

print("\nExample 13 - Authentication decorator:")
print(get_user_data())

# ==============================================
# SECTION 7: PRACTICAL APPLICATIONS
# ==============================================

# Application 1: Data validation
def validate_input(validation_rules):
    """Create a validator based on rules"""
    
    def validate(data):
        errors = []
        for rule_name, rule_func in validation_rules.items():
            if not rule_func(data):
                errors.append(f"Failed: {rule_name}")
        return errors if errors else "Valid"
    
    return validate

rules = {
    "positive": lambda x: x > 0,
    "integer": lambda x: isinstance(x, int),
    "less_than_100": lambda x: x < 100
}

validator = validate_input(rules)

print("\nApplication 1 - Data validation:")
print("Validating 50:", validator(50))    # Valid
print("Validating -5:", validator(-5))    # ['Failed: positive']
print("Validating 150:", validator(150))  # ['Failed: less_than_100']

# Application 2: Caching/Memoization
def memoize(func):
    """Decorator to cache function results"""
    cache = {}
    
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\nApplication 2 - Memoization:")
print("Fibonacci(10):", fibonacci(10))  # 55

# Application 3: Rate limiting
def rate_limiter(max_calls, time_period):
    """Decorator to limit function calls"""
    import time
    
    calls = []
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            now = time.time()
            # Remove calls outside the time period
            calls[:] = [call_time for call_time in calls if now - call_time < time_period]
            
            if len(calls) < max_calls:
                calls.append(now)
                return func(*args, **kwargs)
            else:
                return f"Rate limit exceeded. Try again later."
        
        return wrapper
    
    return decorator

@rate_limiter(3, 10)  # 3 calls per 10 seconds
def api_call():
    return "API response"

print("\nApplication 3 - Rate limiting:")
print(api_call())  # API response
print(api_call())  # API response
print(api_call())  # API response
print(api_call())  # Rate limit exceeded

# ==============================================
# SECTION 8: NONLOCAL KEYWORD
# ==============================================

"""
nonlocal Keyword:
- Used to modify variables in an enclosing (non-global) scope
- Required when you want to assign to a variable in the outer function
- Cannot be used for global variables (use 'global' for that)
"""

# Example 1: Modifying outer variable without nonlocal (causes error)
def counter_without_nonlocal():
    count = 0
    
    def increment():
        # count = count + 1  # This would cause UnboundLocalError
        pass

# Example 2: Using nonlocal to modify outer variable
def counter_with_nonlocal():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

counter = counter_with_nonlocal()

print("\nExample 14 - Using nonlocal:")
print("Count 1:", counter())  # 1
print("Count 2:", counter())  # 2
print("Count 3:", counter())  # 3

# Example 3: Multiple modifications
def bank_account(initial_balance):
    balance = initial_balance
    
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance -= amount
        return balance
    
    return deposit, withdraw

deposit, withdraw = bank_account(100)

print("\nExample 15 - Bank account with nonlocal:")
print("Initial:", 100)
print("After deposit 50:", deposit(50))  # 150
print("After withdraw 30:", withdraw(30))  # 120

# ==============================================
# SECTION 9: MULTIPLE LEVELS OF NESTING
# ==============================================

# Example 1: Two levels of nesting
def outer1():
    x = "outer1"
    
    def inner1():
        y = "inner1"
        
        def inner2():
            print(f"x: {x}, y: {y}")
        
        inner2()
    
    inner1()

print("\nExample 16 - Multiple nesting levels:")
outer1()

# Example 2: Factory of factories
def multiplier_factory_advanced(factor):
    """Outer factory"""
    
    def power_factory(power):
        """Inner factory"""
        
        def calculate(n):
            """Actual function"""
            return (n * factor) ** power
        
        return calculate
    
    return power_factory

# Create: (n * 2) ^ 3
calc = multiplier_factory_advanced(2)(3)

print("\nExample 17 - Factory of factories:")
print("(5 * 2) ^ 3 =", calc(5))  # (10)^3 = 1000

# ==============================================
# SECTION 10: NESTED FUNCTIONS WITH ARGUMENTS
# ==============================================

# Example 1: Passing arguments through all levels
def calculate(a, b):
    """Outer function with parameters"""
    
    def add(x, y):
        """Inner function with parameters"""
        return x + y
    
    def multiply(x, y):
        """Another inner function"""
        return x * y
    
    sum_result = add(a, b)
    product_result = multiply(a, b)
    return sum_result, product_result

print("\nExample 18 - Arguments through levels:")
print("calculate(4, 5):", calculate(4, 5))  # (9, 20)

# Example 2: Args and kwargs in nested functions
def process_data(*args, **kwargs):
    """Process with flexible arguments"""
    
    def transform(*args, **kwargs):
        args = tuple(x * 2 for x in args)
        kwargs = {k: v.upper() for k, v in kwargs.items()}
        return args, kwargs
    
    return transform

result = process_data(1, 2, 3, name="john", city="boston")
print("\nExample 19 - Args and kwargs:")
print("Result:", result)  # ((2, 4, 6), {'name': 'JOHN', 'city': 'BOSTON'})

# ==============================================
# SECTION 11: COMMON PATTERNS AND USE CASES
# ==============================================

# Pattern 1: Private helper functions
def public_api():
    """Public function that uses private helpers"""
    
    def validate_input(data):
        """Private helper - not accessible outside"""
        return isinstance(data, (int, float))
    
    def process_data(data):
        """Private helper - not accessible outside"""
        return data * 2
    
    def format_output(data):
        """Private helper - not accessible outside"""
        return f"Result: {data}"
    
    # Use the helpers
    if validate_input(10):
        result = process_data(10)
        return format_output(result)
    return "Invalid input"

print("\nPattern 1 - Private helpers:")
print(public_api())  # Result: 20

# Pattern 2: Lazy evaluation
def lazy_evaluator():
    """Functions that compute only when needed"""
    
    def expensive_computation():
        print("Computing...")
        return sum(range(1000000))
    
    result = None
    
    def get_result():
        nonlocal result
        if result is None:
            result = expensive_computation()
        return result
    
    return get_result

lazy = lazy_evaluator()
print("\nPattern 2 - Lazy evaluation:")
print("First call:", lazy())  # Computes
print("Second call:", lazy())  # Returns cached

# Pattern 3: Strategy pattern
def apply_operation(operation_type):
    """Apply different strategies"""
    
    strategies = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Error"
    }
    
    return strategies.get(operation_type, lambda x, y: "Invalid operation")

add_func = apply_operation("add")
multiply_func = apply_operation("multiply")

print("\nPattern 3 - Strategy pattern:")
print("5 + 3 =", add_func(5, 3))  # 8
print("5 * 3 =", multiply_func(5, 3))  # 15

# ==============================================
# SECTION 12: BEST PRACTICES AND PITFALLS
# ==============================================

"""
Best Practices:
1. Use nested functions for helper functions that are only used once
2. Use closures when you need to remember values
3. Use decorators to modify function behavior
4. Keep nesting levels reasonable (2-3 levels max)
5. Use meaningful names for nested functions

Pitfalls:
1. Excessive nesting makes code hard to read
2. Forgetting nonlocal when modifying outer variables
3. Mutable default arguments in nested functions
4. Not returning the nested function when needed
"""

# Pitfall: Excessive nesting
# AVOID THIS:
def avoid_deep_nesting():
    def level1():
        def level2():
            def level3():
                def level4():
                    print("Too deep!")
                level4()
            level3()
        level2()
    level1()

# Better approach: Keep it shallow
def better_approach():
    def level1_helper():
        def level2_helper():
            print("Manageable")
        level2_helper()
    level1_helper()

# Pitfall: Not using nonlocal
def pitfall_example():
    x = 10
    
    def inner():
        # x = x + 1  # Would cause UnboundLocalError
        # Must use: nonlocal x
        pass
    
    return inner

# ==============================================
# SUMMARY
# ==============================================

print("\n" + "="*50)
print("NESTED FUNCTIONS - KEY TAKEAWAYS")
print("="*50)
print("""
1. Nested functions are functions defined inside other functions

2. They can access variables from outer scope (closure)

3. Use nonlocal to modify outer function variables

4. Common uses:
   - Private helper functions
   - Function factories (decorators)
   - Creating closures
   - Data encapsulation
   - Implementing patterns (strategy, decorator)

5. Decorators:
   - Modify function behavior
   - Use @decorator syntax
   - Common: @timer, @log, @cache

6. Best Practices:
   - Keep nesting shallow (2-3 levels)
   - Use descriptive names
   - Prefer modules for complex helpers
   - Use nonlocal only when needed
""")
