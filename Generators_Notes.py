"""
================================================================================
                        PYTHON GENERATORS - COMPLETE GUIDE
================================================================================
A comprehensive guide to Python generators with clear explanations
and executable code examples for easy understanding.
================================================================================
"""

# ================================================================================
#                         WHAT ARE GENERATORS?
# ================================================================================
"""
 generators are special type of functions that yield values one at a time
 instead of returning a single value. They produce a sequence of values
 on-demand (lazily), which makes them memory-efficient for handling
 large datasets or infinite sequences.

 KEY CHARACTERISTICS:
 --------------------
 ✓ Uses 'yield' keyword instead of 'return'
 ✓ Returns a generator object (iterator)
 ✓ Remembers its state between yield statements
 ✓ Can pause and resume execution
 ✓ Memory efficient - doesn't store entire sequence in memory
 ✓ Lazy evaluation - values generated only when needed
"""

print("=" * 80)
print("                    PYTHON GENERATORS TUTORIAL")
print("=" * 80)


# ================================================================================
#                      BASIC GENERATOR FUNCTION
# ================================================================================

def count_up_to(n):
    """
    A simple generator that yields numbers from 1 to n.
    
    Args:
        n: The upper limit (inclusive)
    
    Yields:
        Numbers from 1 to n, one at a time
    """
    count = 1
    while count <= n:
        yield count
        count += 1


# Using the generator
print("\n" + "-" * 40)
print("1. BASIC GENERATOR")
print("-" * 40)

print("count_up_to(5):")
for num in count_up_to(5):
    print(num, end=" ")  # Output: 1 2 3 4 5

# Converting to list
numbers = list(count_up_to(3))
print(f"\nlist(count_up_to(3)) = {numbers}")  # [1, 2, 3]


# ================================================================================
#                   GENERATOR vs NORMAL FUNCTION
# ================================================================================

print("\n" + "-" * 40)
print("2. GENERATOR vs NORMAL FUNCTION")
print("-" * 40)

# Normal function - returns all values at once (eager evaluation)
def count_up_to_list(n):
    """Normal function returning a list."""
    result = []
    count = 1
    while count <= n:
        result.append(count)
        count += 1
    return result

# Generator function - yields values one by one (lazy evaluation)
def count_up_to_gen(n):
    """Generator function yielding values."""
    count = 1
    while count <= n:
        yield count
        count += 1

print("Normal function (count_up_to_list(3)):")
result_list = count_up_to_list(3)
print(f"  Returns: {result_list}")  # [1, 2, 3] - all at once

print("\nGenerator function (count_up_to_gen(3)):")
result_gen = count_up_to_gen(3)
print(f"  Returns: {result_gen}")  # <generator object...>
print(f"  Type: {type(result_gen)}")  # <class 'generator'>


# ================================================================================
#                    GENERATOR EXPRESSIONS
# ================================================================================

print("\n" + "-" * 40)
print("3. GENERATOR EXPRESSIONS")
print("-" * 40)

"""
Generator expressions are similar to list comprehensions but use
parentheses instead of square brackets. They create anonymous generators.
"""

# Syntax: (expression for item in iterable if condition)

# Example 1: Square of numbers
squares = (x**2 for x in range(5))
print("Generator expression: (x**2 for x in range(5))")
print(f"  Type: {type(squares)}")
print(f"  As list: {list(squares)}")  # [0, 1, 4, 9, 16]

# Example 2: With condition
evens = (x for x in range(10) if x % 2 == 0)
print(f"\n(x for x in range(10) if x % 2 == 0)")
print(f"  As list: {list(evens)}")  # [0, 2, 4, 6, 8]

# Example 3: String manipulation
words = ("Hello", "World", "Python")
upper_words = (word.upper() for word in words)
print(f"\n(word.upper() for word in ['Hello', 'World', 'Python'])")
print(f"  As list: {list(upper_words)}")  # ['HELLO', 'WORLD', 'PYTHON']


# ================================================================================
#                      YIELD KEYWORD EXPLAINED
# ================================================================================

print("\n" + "-" * 40)
print("4. YIELD KEYWORD")
print("-" * 40)

"""
yield vs return:
- return: Exits the function and sends back a value
- yield: Pauses the function, saves its state, and yields a value
         The function can be resumed from where it left off
"""

def simple_yield():
    """Demonstrates yield behavior."""
    print("  Before first yield")
    yield 1
    print("  After first yield, before second")
    yield 2
    print("  After second yield")
    yield 3

print("Execution flow of generator with multiple yields:")
gen = simple_yield()
print(f"\n  Created generator: {gen}")

print(f"\n  next(gen): {next(gen)}")  # 1
print(f"  next(gen): {next(gen)}")  # 2
print(f"  next(gen): {next(gen)}")  # 3
# print(f"  next(gen): {next(gen)}")  # Would raise StopIteration


# ================================================================================
#                      SENDING VALUES TO GENERATORS
# ================================================================================

print("\n" + "-" * 40)
print("5. SENDING VALUES TO GENERATORS (send)")
print("-" * 40)

def generator_with_send():
    """Generator that can receive values using send()."""
    received = yield "Starting..."
    yield received
    yield "Done"

gen = generator_with_send()
print("Using send() to communicate with generator:")

# First call must be next() to start the generator
result = next(gen)
print(f"  next(gen): {result}")  # Starting...

# Use send() to send a value
result = gen.send("Hello from send!")
print(f"  gen.send('Hello from send!'): {result}")  # Hello from send!

result = next(gen)
print(f"  next(gen): {result}")  # Done


# ================================================================================
#                      YIELD FROM (DELEGATION)
# ================================================================================

print("\n" + "-" * 40)
print("6. YIELD FROM (Generator Delegation)")
print("-" * 40)

"""
yield from allows a generator to delegate to another generator or iterable.
It automatically iterates through the sub-generator and yields its values.
"""

def chain_iterables(*iterables):
    """Chain multiple iterables together using yield from."""
    for iterable in iterables:
        yield from iterable

print("Chaining multiple iterables with yield from:")
result = list(chain_iterables([1, 2], [3, 4], [5, 6]))
print(f"  list(chain_iterables([1,2], [3,4], [5,6])) = {result}")

# Without yield from (manual approach)
def chain_manual(*iterables):
    """Manual chaining without yield from."""
    for iterable in iterables:
        for item in iterable:
            yield item

print(f"\n  list(chain_manual([1,2], [3,4], [5,6])) = {list(chain_manual([1, 2], [3, 4], [5, 6]))}")


# ================================================================================
#                    INFINITE GENERATORS
# ================================================================================

print("\n" + "-" * 40)
print("7. INFINITE GENERATORS")
print("-" * 40)

"""
Generators are perfect for infinite sequences because they generate
values on-demand and don't store them in memory.
"""

def infinite_counter():
    """An infinite counter - generates numbers forever."""
    count = 1
    while True:
        yield count
        count += 1

print("Infinite counter (first 10 values):")
counter = infinite_counter()
for _ in range(10):
    print(next(counter), end=" ")  # 1 2 3 4 5 6 7 8 9 10

def fibonacci_generator():
    """Infinite Fibonacci sequence generator."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\n\nFibonacci generator (first 15 values):")
fib = fibonacci_generator()
for _ in range(15):
    print(next(fib), end=" ")  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

def cycle_generator(iterable):
    """Cycle through an iterable infinitely."""
    while True:
        for item in iterable:
            yield item

print("\n\nCycle generator (repeating ['A', 'B', 'C']):")
cycle = cycle_generator(['A', 'B', 'C'])
for _ in range(12):
    print(next(cycle), end=" ")  # A B C A B C A B C A B C


# ================================================================================
#                    PIPING GENERATORS
# ================================================================================

print("\n" + "-" * 40)
print("8. PIPING GENERATORS (Chaining)")
print("-" * 40)

"""
Generators can be piped together to create data processing pipelines.
Each generator transforms data and passes it to the next.
"""

def numbers_up_to(n):
    """Generate numbers from 1 to n."""
    for i in range(1, n + 1):
        yield i

def square_numbers(gen):
    """Square each number from the generator."""
    for num in gen:
        yield num ** 2

def filter_even(gen):
    """Keep only even numbers."""
    for num in gen:
        if num % 2 == 0:
            yield num

# Piping: numbers -> square -> filter even
print("Generator pipeline example:")
print("  numbers(5) -> square -> filter_even")

result = filter_even(square_numbers(numbers_up_to(5)))
print(f"  Result: {list(result)}")  # [4, 16]

# Using built-in generators
print("\nUsing map and filter with generators:")
nums = range(1, 11)
result = list(filter(lambda x: x > 20, map(lambda x: x**2, nums)))
print(f"  squares of 1-10, filtered > 20: {result}")


# ================================================================================
#                    GENERATOR METHODS
# ================================================================================

print("\n" + "-" * 40)
print("9. GENERATOR METHODS")
print("-" * 40)

"""
Generator objects have special methods:
- next()     : Get next value
- send()     : Send value to generator
- throw()    : Throw exception in generator
- close()    : Close the generator
"""

def demo_generator():
    """Demo generator for methods."""
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print("  Generator was closed!")

print("Generator methods demonstration:")

gen = demo_generator()
print(f"  next(gen): {next(gen)}")  # 1
print(f"  next(gen): {next(gen)}")  # 2

# Using close()
gen.close()  # Raises GeneratorExit, generator is closed


# ================================================================================
#                    MEMORY EFFICIENCY
# ================================================================================

print("\n" + "-" * 40)
print("10. MEMORY EFFICIENCY")
print("-" * 40)

"""
Generators are memory efficient because they yield values one at a time
instead of storing the entire sequence in memory.
"""

import sys

# List vs Generator memory comparison
large_range = 1000000

# List stores ALL values in memory
list_example = list(range(large_range))
list_size = sys.getsizeof(list_example)
print(f"Memory for list(range(1,000,000)): {list_size:,} bytes")

# Generator stores only the logic
gen_example = (x for x in range(large_range))
gen_size = sys.getsizeof(gen_example)
print(f"Memory for generator: {gen_size:,} bytes")

print(f"\nMemory saved: {list_size - gen_size:,} bytes ({((list_size - gen_size) / list_size * 100):.1f}%)")


# ================================================================================
#                    PRACTICAL EXAMPLES
# ================================================================================

print("\n" + "-" * 40)
print("11. PRACTICAL EXAMPLES")
print("-" * 40)

# Example 1: Reading large files
print("Example 1: File reader (memory efficient)")
def read_file_lines(filename):
    """Read file line by line."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        yield None

# Example 2: Running statistics
print("\nExample 2: Running statistics generator")
def running_stats(numbers):
    """Calculate running sum and average."""
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
        yield {
            'number': num,
            'sum': total,
            'average': total / count,
            'count': count
        }

data = [10, 20, 30, 40, 50]
print(f"Running stats for {data}:")
for stat in running_stats(data):
    print(f"  {stat}")

# Example 3: Pagination
print("\nExample 3: Pagination generator")
def paginate(items, page_size):
    """Yield pages of items."""
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]

items = list(range(1, 26))  # 25 items
print(f"Paginating {len(items)} items with page_size=7:")
for i, page in enumerate(paginate(items, 7), 1):
    print(f"  Page {i}: {page}")

# Example 4: Prime number generator
print("\nExample 4: Prime number generator")
def is_prime(n):
    """Check if number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(limit=None):
    """Generate prime numbers, optionally up to a limit."""
    num = 2
    while limit is None or num <= limit:
        if is_prime(num):
            yield num
        num += 1

print("First 20 prime numbers:")
primes = prime_generator()
prime_list = [next(primes) for _ in range(20)]
print(f"  {prime_list}")


# ================================================================================
#                    COMMON PATTERNS
# ================================================================================

print("\n" + "-" * 40)
print("12. COMMON GENERATOR PATTERNS")
print("-" * 40)

# Pattern 1: Window/Buffer
print("Pattern 1: Sliding window")
def sliding_window(iterable, n=2):
    """Create sliding windows of size n."""
    window = []
    for item in iterable:
        window.append(item)
        if len(window) == n:
            yield tuple(window)
            window.pop(0)

data = [1, 2, 3, 4, 5]
print(f"  sliding_window({data}, 3):")
for window in sliding_window(data, 3):
    print(f"    {window}")

# Pattern 2: Filter chain
print("\nPattern 2: Filter chain")
def filter_chain(data, *filters):
    """Apply multiple filters to data."""
    for item in data:
        if all(f(item) for f in filters):
            yield item

numbers = range(1, 31)
result = filter_chain(numbers, lambda x: x % 2 == 0, lambda x: x % 3 == 0)
print(f"  Numbers 1-30 divisible by 2 and 3: {list(result)}")

# Pattern 3: Transform chain
print("\nPattern 3: Transform chain")
def transform_chain(data, *transforms):
    """Apply multiple transformations to data."""
    for item in data:
        value = item
        for transform in transforms:
            value = transform(value)
        yield value

numbers = [1, 2, 3, 4, 5]
result = transform_chain(numbers, lambda x: x * 2, lambda x: x + 1)
print(f"  Double then add 1 to {numbers}: {list(result)}")


# ================================================================================
#                    GENERATOR vs ITERATOR
# ================================================================================

print("\n" + "-" * 40)
print("13. GENERATOR vs ITERATOR")
print("-" * 40)

"""
Iterator:
- An object that implements __iter__() and __next__()
- Must manually implement the iteration logic

Generator:
- A special type of iterator created from generator functions
- Automatically implements __iter__(), __next__(), send(), throw(), close()
- Much simpler to write than manual iterators
"""

# Manual Iterator (more code)
class CountIterator:
    """Manual iterator implementation."""
    def __init__(self, limit):
        self.limit = limit
        self.current = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Generator (much simpler)
def count_generator(limit):
    """Generator equivalent."""
    current = 1
    while current <= limit:
        yield current
        current += 1

print("Manual Iterator:")
for num in CountIterator(3):
    print(f"  {num}", end=" ")

print("\n\nGenerator (same result, less code):")
for num in count_generator(3):
    print(f"  {num}", end=" ")


# ================================================================================
#                    WHEN TO USE GENERATORS
# ================================================================================

print("\n" + "-" * 40)
print("14. WHEN TO USE GENERATORS")
print("-" * 40)

print("""
USE GENERATORS WHEN:
--------------------
✓ Working with large datasets (memory efficiency)
✓ Processing data streams (on-demand processing)
✓ Creating infinite sequences
✓ Building data pipelines
✓ Reading large files line by line
✓ Implementing lazy evaluation
✓ You only need to iterate once
✓ Building custom iterators (simpler code)

AVOID GENERATORS WHEN:
----------------------
✗ You need to iterate multiple times over the same data
✗ You need random access to elements (by index)
✗ The dataset is small and fits easily in memory
✗ You need to know the length/count beforehand
""")


# ================================================================================
#                    BEST PRACTICES
# ================================================================================

print("\n" + "-" * 40)
print("15. BEST PRACTICES")
print("-" * 40)

print("""
1. Use generators for memory efficiency with large data
2. Prefer generator expressions for simple transformations
3. Use yield from for delegating to sub-generators
4. Close generators properly when done (or use context managers)
5. Don't forget that generators are exhausted after one use
6. Use meaningful variable names in generators
7. Add docstrings explaining what the generator yields
8. Chain generators for clean data pipelines
9. Use next() with default value to avoid StopIteration
10. Consider itertools for complex generator operations
""")


# ================================================================================
#                    SUMMARY
# ================================================================================

print("\n" + "=" * 80)
print("                         KEY TAKEAWAYS")
print("=" * 80)
print("""
┌─────────────────────────────────────────────────────────────────────────────┐
│  GENERATOR BASICS                                                           │
│  ─────────────                                                               │
│  • Created using 'yield' keyword in a function                              │
│  • Returns a generator object (iterator)                                    │
│  • Values are produced lazily (on-demand)                                    │
│  • Remembers state between yields                                           │
│                                                                             │
│  GENERATOR EXPRESSIONS                                                      │
│  ───────────────────                                                        │
│  • Syntax: (expr for item in iterable if condition)                        │
│  • Memory efficient alternative to list comprehensions                      │
│                                                                             │
│  YIELD FROM                                                                 │
│  ─────────                                                                  │
│  • Delegates to sub-generators                                              │
│  • Simplifies generator chaining                                            │
│                                                                             │
│  ADVANTAGES                                                                 │
│  ──────────                                                                 │
│  • Memory efficient (no need to store entire sequence)                     │
│  • Fast to create (less code than manual iterators)                         │
│  • Perfect for infinite sequences                                           │
│  • Ideal for data pipelines                                                 │
└─────────────────────────────────────────────────────────────────────────────┘
""")

print("=" * 80)
print("               GENERATORS TUTORIAL COMPLETE!")
print("=" * 80)
print("""
Topics Covered:
✓ What are Generators
✓ Basic Generator Function
✓ Generator vs Normal Function
✓ Generator Expressions
✓ Yield Keyword
✓ Sending Values (send)
✓ Yield From (Delegation)
✓ Infinite Generators
✓ Piping Generators
✓ Generator Methods
✓ Memory Efficiency
✓ Practical Examples
✓ Common Patterns
✓ Generator vs Iterator
✓ When to Use Generators
✓ Best Practices
""")
print("=" * 80)
print("                    Happy Coding! 🚀")
print("=" * 80)
