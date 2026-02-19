"""
================================================================================
                FUNCTION ARGUMENTS IN PYTHON - COMPLETE GUIDE
================================================================================
A comprehensive guide to understanding and using function arguments in Python.
This file covers all types of arguments with detailed explanations and examples.
================================================================================

TABLE OF CONTENTS:
1. Introduction to Function Arguments
2. Positional Arguments
3. Keyword Arguments
4. Default Arguments
5. *args - Variable Positional Arguments
6. **kwargs - Variable Keyword Arguments
7. Combining All Types
8. Argument Unpacking
9. Special Cases and Best Practices
10. Practical Examples

================================================================================
"""

# ================================================================================
#                    1. INTRODUCTION TO FUNCTION ARGUMENTS
# ================================================================================
"""
WHAT ARE FUNCTION ARGUMENTS?
-----------------------------
Arguments are values passed to a function when it is called.
These values are assigned to the function's parameters and used inside the function.

KEY TERMINOLOGY:
- Parameter: A variable in the function definition that receives a value
- Argument: The actual value passed to the function when called

Example:
    def greet(name):    # 'name' is a PARAMETER
        print(f"Hello, {name}!")
    
    greet("John")       # "John" is an ARGUMENT

WHY USE ARGUMENTS?
------------------
1. Make functions flexible and reusable
2. Allow dynamic input to functions
3. Enable data processing with different values
4. Support modular and organized code
"""

# Basic function with parameter
def introduce(name, age):
    """Function with parameters."""
    print(f"My name is {name} and I am {age} years old.")

introduce("Alice", 25)  # Passing arguments


# ================================================================================
#                       2. POSITIONAL ARGUMENTS
# ================================================================================
"""
POSITIONAL ARGUMENTS
--------------------
Arguments passed to a function in a specific order.
The position of each argument matters - the first argument goes to the first
parameter, second to second, and so on.

RULES:
- Must be provided in the exact order as parameters are defined
- Required positional arguments must be provided
- Cannot be omitted or reordered (unless using keyword arguments)
"""

print("\n" + "="*60)
print("POSITIONAL ARGUMENTS")
print("="*60)

# Example 1: Basic positional arguments
def describe_pet(animal, name):
    """Describe a pet using positional arguments."""
    print(f"I have a {animal} named {name}.")

# Calling with positional arguments
describe_pet("dog", "Buddy")      # dog = animal, Buddy = name
describe_pet("cat", "Whiskers")   # cat = animal, Whiskers = name
describe_pet("hamster", "Nibbles") # hamster = animal, Nibbles = name

# Example 2: Multiple positional arguments
def create_profile(username, email, age, city):
    """Create a user profile with positional arguments."""
    print(f"\n--- User Profile ---")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Age: {age}")
    print(f"City: {city}")

create_profile("john_doe", "john@example.com", 25, "New York")

# Example 3: Calculator with positional arguments
def calculate(a, b, operation):
    """Perform calculation based on operation type."""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Unknown operation"

print("\nCalculator examples:")
print(f"calculate(10, 5, 'add') = {calculate(10, 5, 'add')}")           # 15
print(f"calculate(10, 5, 'subtract') = {calculate(10, 5, 'subtract')}")  # 5
print(f"calculate(10, 5, 'multiply') = {calculate(10, 5, 'multiply')}")  # 50
print(f"calculate(10, 5, 'divide') = {calculate(10, 5, 'divide')}")      # 2.0

# Example 4: Position matters!
def greet_person(greeting, name):
    """Demonstrate that position matters."""
    print(f"{greeting}, {name}!")

greet_person("Hello", "John")    # Hello, John!
greet_person("John", "Hello")    # John, Hello! (wrong order!)


# ================================================================================
#                       3. KEYWORD ARGUMENTS
# ================================================================================
"""
KEYWORD ARGUMENTS
-----------------
Arguments passed with the parameter name as a keyword.
The order doesn't matter when using keyword arguments.

ADVANTAGES:
- Improves code readability
- Allows arguments to be passed in any order
- Makes it clear which value goes to which parameter
- Helps avoid mistakes with positional arguments

NOTE: Positional arguments must come before keyword arguments
"""

print("\n" + "="*60)
print("KEYWORD ARGUMENTS")
print("="*60)

# Example 1: Basic keyword arguments
def create_car(brand, model, year, color):
    """Create a car description using keyword arguments."""
    print(f"Car: {year} {color} {brand} {model}")

# Using keyword arguments (order doesn't matter)
create_car(brand="Toyota", model="Camry", year=2022, color="Blue")
create_car(year=2021, color="Red", brand="Honda", model="Civic")
create_car("Tesla", model="Model 3", color="White", year=2023)  # Mixed!

# Example 2: Keyword arguments vs positional
def display_info(name, age, occupation):
    """Display personal information."""
    print(f"\nName: {name}")
    print(f"Age: {age}")
    print(f"Occupation: {occupation}")

# Positional way
display_info("Alice", 30, "Engineer")

# Keyword way (more readable!)
display_info(name="Bob", age=25, occupation="Designer")
display_info(occupation="Doctor", name="Carol", age=35)  # Any order!

# Example 3: Practical use case - API call simulation
def make_api_request(url, method, headers, body, timeout):
    """Simulate an API request with keyword arguments."""
    print(f"\n--- API Request ---")
    print(f"URL: {url}")
    print(f"Method: {method}")
    print(f"Headers: {headers}")
    print(f"Body: {body}")
    print(f"Timeout: {timeout} seconds")

# Using keyword arguments makes the call very clear
make_api_request(
    url="https://api.example.com/users",
    method="POST",
    headers={"Content-Type": "application/json"},
    body={"name": "John", "email": "john@example.com"},
    timeout=30
)

# Example 4: Mixing positional and keyword arguments
# RULE: Positional arguments must come BEFORE keyword arguments
def mixed_args(a, b, c, d):
    print(f"a={a}, b={b}, c={c}, d={d}")

mixed_args(1, 2, c=3, d=4)  # Valid: 1,2 are positional; c,d are keyword
# mixed_args(1, 2, a=3, d=4)  # ERROR: positional arg after keyword arg!


# ================================================================================
#                       4. DEFAULT ARGUMENTS
# ================================================================================
"""
DEFAULT ARGUMENTS
-----------------
Parameters that have a default value.
If no argument is provided, the default value is used.

RULES FOR DEFAULT ARGUMENTS:
1. Default parameters must come AFTER non-default parameters
2. Default values should be immutable (None, numbers, strings, tuples)
3. Mutable default values (like lists) can cause unexpected behavior

WHY USE DEFAULT ARGUMENTS?
- Make parameters optional
- Provide sensible defaults
- Maintain backward compatibility
- Reduce function call complexity
"""

print("\n" + "="*60)
print("DEFAULT ARGUMENTS")
print("="*60)

# Example 1: Basic default arguments
def greet_user(name, greeting="Hello"):
    """Greet a user with a default greeting."""
    print(f"{greeting}, {name}!")

greet_user("Alice")           # Uses default: Hello, Alice!
greet_user("Bob", "Hi")       # Overrides default: Hi, Bob!
greet_user("Carol", "Welcome") # Welcome, Carol!

# Example 2: Multiple default arguments
def create_user(username, email, age=18, is_active=True, role="user"):
    """Create a user with default values."""
    print(f"\n--- Creating User ---")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Age: {age}")
    print(f"Active: {is_active}")
    print(f"Role: {role}")

create_user("john_doe", "john@example.com")
create_user("jane_smith", "jane@example.com", age=25)
create_user("admin", "admin@example.com", role="admin", is_active=False)

# Example 3: Default arguments with calculations
def calculate_total(price, tax_rate=0.1, discount=0):
    """Calculate total price with tax and discount."""
    subtotal = price - discount
    tax = subtotal * tax_rate
    return subtotal + tax

print("\nPricing examples:")
print(f"calculate_total(100) = ${calculate_total(100)}")           # $110 (10% tax)
print(f"calculate_total(100, 0.15) = ${calculate_total(100, 0.15)}") # $115 (15% tax)
print(f"calculate_total(100, 0.15, 10) = ${calculate_total(100, 0.15, 10)}") # $103.5

# Example 4: Function with complex defaults
def send_email(to, subject="No Subject", body="", cc=None, bcc=None):
    """Send an email with default options."""
    print(f"\n--- Sending Email ---")
    print(f"To: {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body or '(empty)'}")
    print(f"CC: {cc or 'None'}")
    print(f"BCC: {bcc or 'None'}")

send_email("friend@example.com")
send_email("friend@example.com", "Hello!", "Just saying hi!")
send_email("boss@example.com", "Report", "Here is the report...", 
           cc="colleague@example.com")

# Example 5: IMPORTANT - Mutable default argument pitfall!
def bad_append(item, items=[]):  # WRONG! Mutable default
    """This demonstrates the mutable default pitfall."""
    items.append(item)
    return items

print("\nMutable default argument pitfall:")
print(f"bad_append('a') = {bad_append('a')}")  # ['a']
print(f"bad_append('b') = {bad_append('b')}")  # ['a', 'b'] - BUG!

# Correct way - use None as default
def good_append(item, items=None):  # CORRECT!
    """Correct way to handle mutable defaults."""
    if items is None:
        items = []
    items.append(item)
    return items

print(f"good_append('a') = {good_append('a')}")  # ['a']
print(f"good_append('b') = {good_append('b')}")  # ['b'] - Correct!


# ================================================================================
#                       5. *args - VARIABLE POSITIONAL ARGUMENTS
# ================================================================================
"""
*args (VARIABLE POSITIONAL ARGUMENTS)
-------------------------------------
Allows a function to accept any number of positional arguments.
The arguments are packed into a tuple.

WHEN TO USE *args:
- When you don't know how many arguments will be passed
- For functions that work with variable-length argument lists
- When you want to collect multiple arguments into a tuple

SYNTAX:
    def function(*args):
        # args is a tuple

NOTE: args is just a convention; you can use any name like *numbers
"""

print("\n" + "="*60)
print("*args - VARIABLE POSITIONAL ARGUMENTS")
print("="*60)

# Example 1: Basic *args usage
def sum_all(*numbers):
    """Sum all numbers passed as arguments."""
    total = 0
    print(f"Received: {numbers} (type: {type(numbers).__name__})")
    for num in numbers:
        total += num
    return total

print("Sum examples:")
print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")                    # 6
print(f"sum_all(10, 20, 30, 40) = {sum_all(10, 20, 30, 40)}")       # 100
print(f"sum_all(5) = {sum_all(5)}")                                 # 5
print(f"sum_all() = {sum_all()}")                                   # 0

# Example 2: *args with regular parameters
def print_names(greeting, *names):
    """Print greeting for all names."""
    print(f"\n{greeting}!")
    for name in names:
        print(f"  - {name}")

print_names("Hello", "Alice", "Bob", "Charlie")
print_names("Welcome", "John")

# Example 3: Finding maximum with *args
def find_maximum(*numbers):
    """Find the maximum among all numbers."""
    if not numbers:
        return "No numbers provided"
    return max(numbers)

print(f"\nMaximum: find_maximum(3, 1, 4, 1, 5, 9) = {find_maximum(3, 1, 4, 1, 5, 9)}")
print(f"Maximum: find_maximum(-5, -2, -8) = {find_maximum(-5, -2, -8)}")
print(f"Maximum: find_maximum(42) = {find_maximum(42)}")

# Example 4: Practical example - Order total calculator
def calculate_order_total(*items, tax_rate=0.1):
    """Calculate total with optional tax."""
    subtotal = sum(items)
    tax = subtotal * tax_rate
    return subtotal + tax

print(f"\nOrder totals:")
print(f"calculate_order_total(10, 20, 30) = ${calculate_order_total(10, 20, 30):.2f}")
print(f"calculate_order_total(100, 50, 25, 25) = ${calculate_order_total(100, 50, 25, 25):.2f}")

# Example 5: String concatenator
def concatenate_strings(*strings, separator=" "):
    """Concatenate multiple strings with a separator."""
    return separator.join(strings)

print(f"\nconcatenate_strings('Hello', 'World') = '{concatenate_strings('Hello', 'World')}'")
print(f"concatenate_strings('A', 'B', 'C', separator='-') = '{concatenate_strings('A', 'B', 'C', separator='-')}'")
print(f"concatenate_strings('Python', 'is', 'awesome', separator='_') = '{concatenate_strings('Python', 'is', 'awesome', separator='_')}'")

# Example 6: Building a URL
def build_url(*parts, protocol="https"):
    """Build URL from parts."""
    return protocol + "://" + "/".join(parts)

print(f"\nbuild_url('example', 'com') = '{build_url('example', 'com')}'")
print(f"build_url('www', 'google', 'com', 'search') = '{build_url('www', 'google', 'com', 'search')}'")


# ================================================================================
#                   6. **kwargs - VARIABLE KEYWORD ARGUMENTS
# ================================================================================
"""
**kwargs (VARIABLE KEYWORD ARGUMENTS)
-------------------------------------
Allows a function to accept any number of keyword arguments.
The arguments are packed into a dictionary.

WHEN TO USE **kwargs:
- When you don't know how many keyword arguments will be passed
- For configuration options
- When working with named parameters dynamically

SYNTAX:
    def function(**kwargs):
        # kwargs is a dictionary

NOTE: kwargs is just a convention; you can use any name like **options
"""

print("\n" + "="*60)
print("**kwargs - VARIABLE KEYWORD ARGUMENTS")
print("="*60)

# Example 1: Basic **kwargs usage
def print_all_info(**info):
    """Print all keyword arguments."""
    print(f"Received: {info} (type: {type(info).__name__})")
    for key, value in info.items():
        print(f"  {key}: {value}")

print("\nprint_all_info examples:")
print_all_info(name="Alice", age=30, city="NYC")
print_all_info(product="Laptop", price=999, in_stock=True)

# Example 2: User profile builder with **kwargs
def create_user_profile(**profile):
    """Create user profile from keyword arguments."""
    print("\n--- User Profile ---")
    for key, value in profile.items():
        # Convert underscore_names to Title Case
        display_key = key.replace('_', ' ').title()
        print(f"{display_key}: {value}")

create_user_profile(first_name="John", last_name="Doe", age=28, city="Boston")
create_user_profile(username="jdoe", email="john@example.com")

# Example 3: Database query builder
def build_query(table, **conditions):
    """Build a simple SQL query from conditions."""
    query = f"SELECT * FROM {table}"
    
    if conditions:
        where_clauses = [f"{key} = '{value}'" for key, value in conditions.items()]
        query += " WHERE " + " AND ".join(where_clauses)
    
    return query

print("\nQuery builder:")
print(build_query("users"))
print(build_query("users", status="active"))
print(build_query("products", category="electronics", price_lt=1000))
print(build_query("orders", customer_id=123, status="shipped"))

# Example 4: Function configuration
def configure_server(**config):
    """Configure server with various options."""
    defaults = {
        'host': 'localhost',
        'port': 8080,
        'debug': False,
        'max_connections': 100
    }
    
    # Update defaults with provided config
    settings = {**defaults, **config}
    
    print("\n--- Server Configuration ---")
    for key, value in settings.items():
        print(f"  {key}: {value}")

configure_server()
configure_server(port=3000)
configure_server(host="0.0.0.0", debug=True, port=9000)

# Example 5: API response formatter
def format_response(status, **data):
    """Format API response."""
    response = {
        "status": status,
        "timestamp": "2024-01-01T00:00:00Z"
    }
    response.update(data)
    return response

print("\nAPI Responses:")
print(format_response("success", message="User created", user_id=123))
print(format_response("error", error_code=404, message="Not found"))


# ================================================================================
#                     7. COMBINING ALL TYPES
# ================================================================================
"""
COMBINING ALL TYPES OF ARGUMENTS
--------------------------------
You can use all types of arguments together in a function.
The order must be:
    1. Positional arguments
    2. *args
    3. Keyword arguments
    4. **kwargs

ORDER DIAGRAM:
    def func(pos1, pos2, *args, kwarg1=default, kwarg2=default, **kwargs):
        ...

IMPORTANT RULES:
- *args must come before **kwargs
- Keyword arguments must come after positional arguments
- Parameters with defaults can be in any position but affect calling style
"""

print("\n" + "="*60)
print("COMBINING ALL TYPES OF ARGUMENTS")
print("="*60)

# Example 1: Comprehensive function with all argument types
def complete_function(pos1, pos2, *args, kwarg1="default1", kwarg2="default2", **kwargs):
    """Function demonstrating all argument types."""
    print(f"\n--- Function Call Analysis ---")
    print(f"Positional (required): pos1={pos1}, pos2={pos2}")
    print(f"*args (variable positional): {args}")
    print(f"Keyword (with defaults): kwarg1={kwarg1}, kwarg2={kwarg2}")
    print(f"**kwargs (variable keyword): {kwargs}")

# Different ways to call this function
complete_function(1, 2)
complete_function(1, 2, 3, 4, 5)
complete_function(1, 2, 3, 4, 5, kwarg1="custom1", kwarg2="custom2")
complete_function(1, 2, 3, 4, 5, kwarg1="custom", extra1="hello", extra2="world")

# Example 2: Practical registration system
def register_user(username, * interests, newsletter=True, **preferences):
    """Register a user with all types of arguments."""
    print(f"\n--- User Registration ---")
    print(f"Username: {username}")
    print(f"Interests: {interests}")
    print(f"Newsletter: {newsletter}")
    print(f"Additional preferences: {preferences}")

register_user("john_doe")
register_user("jane_smith", "Python", "JavaScript")
register_user("alice", "AI", "ML", "Data Science", newsletter=False)
register_user("bob", "Web", newsletter=True, verified=True, tier="premium")

# Example 3: Event handler
def handle_event(event_name, *attendees, location="TBD", **event_details):
    """Handle event with all argument types."""
    print(f"\n=== {event_name} ===")
    print(f"Location: {location}")
    print(f"Attendees ({len(attendees)}):")
    for attendee in attendees:
        print(f"  - {attendee}")
    print("Event Details:")
    for key, value in event_details.items():
        print(f"  {key}: {value}")

handle_event("Python Meetup", "Alice", "Bob", "Charlie")
handle_event("Workshop", "John", "Jane", location="Conference Room A", 
             date="2024-03-15", time="6pm", capacity=50)


# ================================================================================
#                     8. ARGUMENT UNPACKING
# ================================================================================
"""
ARGUMENT UNPACKING
------------------
Passing elements of a collection (list/tuple) as individual arguments.
Also applies to dictionaries for keyword arguments.

TYPES:
1. Unpacking with * (list/tuple -> positional arguments)
2. Unpacking with ** (dictionary -> keyword arguments)

WHY USE UNPACKING?
- Pass list/tuple elements as function arguments
- Make function calls more flexible
- Combine multiple sources of arguments
"""

print("\n" + "="*60)
print("ARGUMENT UNPACKING")
print("="*60)

# Example 1: Unpacking list/tuple with *
def sum_three(a, b, c):
    """Sum three numbers."""
    return a + b + c

numbers = [1, 2, 3]
print(f"sum_three(*numbers) = {sum_three(*numbers)}")  # Unpacks to 1, 2, 3

# Example 2: Unpacking dictionary with **
def create_person(name, age, city):
    """Create a person dict."""
    return {"name": name, "age": age, "city": city}

person_dict = {"name": "Alice", "age": 30, "city": "NYC"}
print(f"create_person(**person_dict) = {create_person(**person_dict)}")

# Example 3: Combining both
def configure_app(name, version, environment, debug):
    """Configure application."""
    return {
        "app": name,
        "ver": version,
        "env": environment,
        "debug": debug
    }

app_config = {"name": "MyApp", "version": "1.0.0"}
other_config = {"environment": "prod", "debug": False}

print(f"\nconfigure_app(**app_config, **other_config) = {configure_app(**app_config, **other_config)}")

# Example 4: Practical - Function that accepts any arguments
def universal_function(*args, **kwargs):
    """Accept any arguments."""
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

my_list = [1, 2, 3]
my_dict = {"a": "first", "b": "second"}

universal_function(*my_list)     # Unpacks list as positional
universal_function(**my_dict)   # Unpacks dict as keyword
universal_function(*my_list, **my_dict)  # Both!

# Example 5: Mixing unpacked and regular arguments
def point_summary(x, y, z):
    """Summarize 3D point."""
    return f"Point({x}, {y}, {z})"

coords = [10, 20]
point_summary(*coords, 30)  # Unpack first two, add third

# Example 6: Advanced - Selectively unpacking
def process_data(a, b, c, d, e):
    """Process data with five parameters."""
    return a + b + c + d + e

data = [1, 2, 3, 4, 5]
partial_data = [1, 2]

# You can also unpack with different lengths
# But be careful - must match required arguments!
result = process_data(*partial_data, 3, **{'d': 4, 'e': 5})
print(f"\nprocess_data(*[1,2], 3, **{'d':4, 'e':5}) = {result}")


# ================================================================================
#              9. SPECIAL CASES AND BEST PRACTICES
# ================================================================================
"""
SPECIAL CASES AND BEST PRACTICES
--------------------------------

1. MUTABLE ARGUMENTS: Always use None for mutable defaults

2. TYPE CHECKING: Consider using type hints for better code

3. *args vs **kwargs: When to use which?
   - Use *args for variable positional arguments
   - Use **kwargs for variable keyword arguments
   - Use both when you need maximum flexibility

4. DOCUMENTATION: Always document your function's arguments

5. ORDER MATTERS: Remember the correct order of arguments
"""

print("\n" + "="*60)
print("SPECIAL CASES AND BEST PRACTICES")
print("="*60)

# Example 1: Type hints for arguments
def typed_function(
    name: str,              # String argument
    age: int,               # Integer argument  
    grades: list[float],    # List of floats
    active: bool = True,    # Boolean with default
    *args: int,             # Variable positional (ints)
    **kwargs: str           # Variable keyword (strings)
) -> dict:
    """Function with type hints for all argument types."""
    return {
        "name": name,
        "age": age,
        "grades": grades,
        "active": active,
        "args": args,
        "kwargs": kwargs
    }

result = typed_function("Alice", 20, [85.5, 90.0, 78.5], major="CS", minor="Math")
print(f"\nTyped function result: {result}")

# Example 2: Validation in functions
def validated_divide(dividend, divisor):
    """Divide with validation."""
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    return dividend / divisor

# Example 3: Flexible function design
class Calculator:
    """Calculator class demonstrating flexible argument handling."""
    
    def calculate(self, *args, operation="add"):
        """Perform calculation on any number of operands."""
        if not args:
            return 0
        
        result = args[0]
        for num in args[1:]:
            if operation == "add":
                result += num
            elif operation == "multiply":
                result *= num
            elif operation == "subtract":
                result -= num
            elif operation == "divide" and num != 0:
                result /= num
        
        return result

calc = Calculator()
print(f"\nCalculator.add(1,2,3,4) = {calc.calculate(1, 2, 3, 4, operation='add')}")
print(f"Calculator.multiply(2,3,4) = {calc.calculate(2, 3, 4, operation='multiply')}")

# Example 4: Using * in function definition (Python 3.8+)
def f(a, b, /, c, d, *, e, f):
    """Positional-only and keyword-only parameters."""
    print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}")

print("\nPositional-only and keyword-only:")
f(1, 2, 3, 4, e=5, f=6)  # All valid


# ================================================================================
#                     10. PRACTICAL EXAMPLES
# ================================================================================
"""
PRACTICAL EXAMPLES
------------------
Real-world scenarios demonstrating the power of function arguments.
"""

print("\n" + "="*60)
print("PRACTICAL EXAMPLES")
print("="*60)

# Example 1: Data processing pipeline
def process_data(
    data,                           # Required: data to process
    *operations,                    # Variable: operations to perform
    verbose=False,                  # Optional: verbose output
    **config                        # Variable: configuration options
):
    """Process data through multiple operations."""
    result = data
    
    print(f"Initial data: {result}")
    
    for op in operations:
        if op == "sort":
            result = sorted(result)
            if verbose: print(f"After sort: {result}")
        elif op == "unique":
            result = list(set(result))
            if verbose: print(f"After unique: {result}")
        elif op == "reverse":
            result = result[::-1]
            if verbose: print(f"After reverse: {result}")
    
    # Apply custom filters from config
    if config.get("min_value"):
        result = [x for x in result if x >= config["min_value"]]
        if verbose: print(f"After min filter: {result}")
    
    if config.get("max_value"):
        result = [x for x in result if x <= config["max_value"]]
        if verbose: print(f"After max filter: {result}")
    
    return result

print("\nData Processing:")
data = [5, 2, 8, 2, 9, 1, 5, 7]
print(f"Original: {data}")
print(f"After 'sort': {process_data(data, 'sort')}")
print(f"After 'sort', 'unique': {process_data(data, 'sort', 'unique')}")
print(f"After 'sort', 'unique', 'reverse', min_value=3: {process_data(data, 'sort', 'unique', 'reverse', min_value=3)}")

# Example 2: URL builder
def build_full_url(
    domain,                    # Required
    path="/",                  # Default
    *path_parts,              # Variable path
    scheme="https",           # Default
    port=None,                # Optional
    **query_params            # Variable query
):
    """Build a complete URL with all components."""
    # Build path
    full_path = path
    if path_parts:
        full_path = "/".join([path.rstrip('/'), *path_parts])
    
    # Build URL
    url = f"{scheme}://{domain}"
    if port:
        url += f":{port}"
    url += full_path
    
    # Add query parameters
    if query_params:
        query_string = "&".join([f"{k}={v}" for k, v in query_params.items()])
        url += f"?{query_string}"
    
    return url

print("\nURL Builder:")
print(build_full_url("example.com"))
print(build_full_url("example.com", "api", "users", port=8080))
print(build_full_url("google.com", "search", query={"q": "python", "lang": "en"}))

# Example 3: Decorator factory
def debug_function(func):
    """Decorator to debug function calls."""
    def wrapper(*args, **kwargs):
        print(f"\nCalling {func.__name__} with:")
        print(f"  Args: {args}")
        print(f"  Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"  Result: {result}")
        return result
    return wrapper

@debug_function
def complex_calculation(x, y, operation="add", *numbers, factor=1, **options):
    """Complex calculation for demonstration."""
    if operation == "add":
        result = x + y + sum(numbers)
    elif operation == "multiply":
        result = x * y
        for n in numbers:
            result *= n
    else:
        result = 0
    
    if options.get("square"):
        result **= 2
    
    return result * factor

print("\nDecorator Example:")
complex_calculation(2, 3, "add", 4, 5, factor=2, square=True)

# Example 4: Class-like functionality with closures
def create_counter():
    """Create a counter function with state."""
    count = [0]  # Using list to allow mutation in closure
    
    def counter(*labels):
        count[0] += 1
        if labels:
            return f"Count {count[0]}: {', '.join(labels)}"
        return f"Count {count[0]}"
    
    return counter

counter1 = create_counter()
counter2 = create_counter()

print("\nCounter examples:")
print(counter1())
print(counter1("event1", "event2"))
print(counter2("another"))


# ================================================================================
#                            SUMMARY
# ================================================================================
"""
FUNCTION ARGUMENTS SUMMARY
==========================

1. POSITIONAL ARGUMENTS
   - Passed in order
   - def f(a, b): f(1, 2)

2. KEYWORD ARGUMENTS  
   - Passed with parameter names
   - def f(a, b): f(a=1, b=2)

3. DEFAULT ARGUMENTS
   - Have default values
   - def f(a, b=10): f(1) or f(1, 20)

4. *args
   - Variable positional arguments
   - Tuple of values
   - def f(*args): f(1, 2, 3)

5. **kwargs
   - Variable keyword arguments
   - Dictionary of values
   - def f(**kwargs): f(a=1, b=2)

6. COMBINING ALL
   - Order: pos, *args, kwarg=default, **kwargs
   - def f(a, *args, b=1, **kwargs)

7. UNPACKING
   - *list unpacks to positional
   - **dict unpacks to keyword

KEY TAKEAWAYS:
- Choose the right argument type for your use case
- Always use None for mutable defaults
- Keep argument order in mind
- Use type hints for clarity
- Document your functions well
"""

print("\n" + "="*80)
print("             FUNCTION ARGUMENTS GUIDE COMPLETE!")
print("="*80)
print("""
Topics Covered:
✓ Introduction to Function Arguments
✓ Positional Arguments
✓ Keyword Arguments  
✓ Default Arguments
✓ *args - Variable Positional Arguments
✓ **kwargs - Variable Keyword Arguments
✓ Combining All Types
✓ Argument Unpacking
✓ Special Cases and Best Practices
✓ Practical Examples
""")
print("="*80)
print("                    Happy Coding! 🚀")
print("="*80)
