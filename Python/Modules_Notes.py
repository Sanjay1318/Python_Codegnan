"""
================================================================================
                    PYTHON MODULES - COMPLETE GUIDE
================================================================================
A comprehensive guide to Python modules from basic to advanced.
Each section includes executable code examples with explanations.
================================================================================
"""

# ================================================================================
#                               BASIC CONCEPTS
# ================================================================================
"""
A MODULE is a file containing Python code (definitions, statements, functions,
classes, etc.) that can be imported and used in other Python files.

WHY MODULES MATTER:
-------------------
1. CODE ORGANIZATION: Split code into manageable files
2. REUSABILITY: Write once, use in multiple programs
3. NAMESPACE SEPARATION: Avoid naming conflicts
4. MAINTAINABILITY: Easier to maintain and debug
5. SCALABILITY: Build large applications from small pieces
"""

print("=" * 80)
print("                    PYTHON MODULES TUTORIAL")
print("=" * 80)


# ================================================================================
#                     CREATING YOUR FIRST MODULE
# ================================================================================

# To create a module, simply save Python code in a .py file
# Example: mymodule.py containing functions/variables

# Let's create a simple module-like structure in this file
def module_example_function():
    """A function that simulates a module's functionality."""
    return "Hello from module!"


# This file itself can be imported as a module!
print("\n" + "-" * 40)
print("1. IMPORTING THIS FILE AS A MODULE")
print("-" * 40)

# Import the current module
import sys

# Get the module's name
print(f"Current module name: {__name__}")
print(f"Current file: {__file__}")


# ================================================================================
#                     IMPORTING MODULES
# ================================================================================

print("\n" + "-" * 40)
print("2. DIFFERENT WAYS TO IMPORT")
print("-" * 40)

# Method 1: Import entire module
print("\nMethod 1: import module_name")
import math
print(f"  math.pi = {math.pi}")
print(f"  math.sqrt(16) = {math.sqrt(16)}")

# Method 2: Import specific items (recommended for clarity)
print("\nMethod 2: from module_name import item1, item2")
from math import pi, sqrt
print(f"  pi = {pi}")
print(f"  sqrt(25) = {sqrt(25)}")

# Method 3: Import with alias (aliasing)
print("\nMethod 3: import module_name as alias")
import math as m
print(f"  m.sin(m.pi/2) = {m.sin(m.pi/2)}")

# Method 4: Import all items (not recommended)
print("\nMethod 4: from module_name import *")
# from math import *  # Would import all (avoid in production)
print("  from math import * - Imports all (avoid in production)")

# Method 5: Import with custom alias
print("\nMethod 5: from module_name import item as alias")
from math import sqrt as square_root
print(f"  square_root(81) = {square_root(81)}")


# ================================================================================
#                     BUILT-IN MODULES
# ================================================================================

print("\n" + "-" * 40)
print("3. COMMON BUILT-IN MODULES")
print("-" * 40)

# os - Operating System interface
import os
print("\nos module:")
print(f"  Current directory: {os.getcwd()}")
print(f"  List files: {os.listdir('.')[:5]}...")  # First 5 files

# sys - System parameters and functions
import sys
print("\nsys module:")
print(f"  Python version: {sys.version}")
print(f"  Platform: {sys.platform}")

# datetime - Date and time
import datetime
print("\ndatetime module:")
print(f"  Current time: {datetime.datetime.now()}")
print(f"  Today's date: {datetime.date.today()}")

# random - Random number generation
import random
print("\nrandom module:")
print(f"  Random integer (1-100): {random.randint(1, 100)}")
print(f"  Random choice from list: {random.choice(['apple', 'banana', 'cherry'])}")
print(f"  Shuffled list: {random.sample([1,2,3,4,5], 5)}")

# json - JSON encoding/decoding
import json
print("\njson module:")
data = {"name": "John", "age": 30}
json_str = json.dumps(data)
print(f"  Dict to JSON: {json_str}")
print(f"  JSON to dict: {json.loads(json_str)}")

# collections - Specialized container datatypes
from collections import Counter, defaultdict
print("\ncollections module:")
counter = Counter(['a', 'b', 'c', 'a', 'a', 'b'])
print(f"  Counter(['a','b','c','a','a','b']): {dict(counter)}")

# itertools - Iterator functions
import itertools
print("\nitertools module:")
print(f"  count(1):", end=" ")
counter_iter = itertools.count(1)
for _ in range(5):
    print(next(counter_iter), end=" ")
print()

# functools - Higher-order functions
from functools import lru_cache
print("\nfunctools module:")
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(f"  fibonacci(30) = {fibonacci(30)} (with memoization)")

# re - Regular expressions
import re
print("\nre module:")
pattern = r'\d+'
text = "There are 123 apples and 456 oranges"
matches = re.findall(pattern, text)
print(f"  findall(r'\\d+', '{text}'): {matches}")


# ================================================================================
#                     THE importlib MODULE
# ================================================================================

print("\n" + "-" * 40)
print("4. DYNAMIC IMPORTS WITH importlib")
print("-" * 40)

"""
importlib allows dynamic importing of modules at runtime.
This is useful when the module name is not known until runtime.
"""

import importlib

# Dynamic import example
module_name = "math"
math_module = importlib.import_module(module_name)
print(f"Dynamically imported '{module_name}':")
print(f"  math_module.sqrt(49) = {math_module.sqrt(49)}")


# ================================================================================
#                     MODULE ATTRIBUTES
# ================================================================================

print("\n" + "-" * 40)
print("5. MODULE ATTRIBUTES")
print("-" * 40)

import math

# __name__ - Module's name
print(f"math.__name__ = '{math.__name__}'")

# __file__ - Module's file path
print(f"math.__file__ = '{math.__file__}'")

# __doc__ - Module's docstring (first line)
print(f"math.__doc__ = '{math.__doc__[:50]}...'")

# __dict__ - Module's namespace dictionary
print(f"len(math.__dict__) = {len(math.__dict__)} items")

# __package__ - Module's package (if any)
print(f"math.__package__ = '{math.__package__}'")

# __spec__ - Module's spec object
print(f"math.__spec__ = {math.__spec__}")


# ================================================================================
#                     THE sys.path VARIABLE
# ================================================================================

print("\n" + "-" * 40)
print("6. UNDERSTANDING sys.path")
print("-" * 40)

"""
sys.path is a list of directories that Python searches for modules.
Order of search:
1. Current directory (or script's directory)
2. PYTHONPATH environment variable
3. Installation-dependent defaults
"""

import sys
print("sys.path locations:")
for i, path in enumerate(sys.path[:5], 1):
    print(f"  {i}. {path}")

# Adding custom directories to path
# sys.path.append('/path/to/module')  # Add custom path
# sys.path.insert(0, '/path/to/module')  # Add with priority


# ================================================================================
#                     CREATING CUSTOM MODULES
# ================================================================================

print("\n" + "-" * 40)
print("7. CREATING CUSTOM MODULES")
print("-" * 40)

# To create a module:
# 1. Create a .py file (e.g., mymodule.py)
# 2. Define functions/classes/variables
# 3. Import and use in other files

# Example module structure:
"""
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# Can also have a main block
if __name__ == "__main__":
    print("Module running directly")
"""

# Let's simulate importing a custom module
print("\nExample custom module structure:")

# Create a simple class that simulates a module
class CustomModule:
    """Simulates a custom module with functions."""
    
    @staticmethod
    def greet(name):
        return f"Hello, {name}!"
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

# Using the "module"
module = CustomModule()
print(f"  module.greet('World') = {module.greet('World')}")
print(f"  module.add(5, 3) = {module.add(5, 3)}")
print(f"  module.multiply(4, 7) = {module.multiply(4, 7)}")


# ================================================================================
#                     THE __main__ BLOCK
# ================================================================================

print("\n" + "-" * 40)
print("8. THE __name__ == '__main__' PATTERN")
print("-" * 40)

"""
When a Python file is run directly, __name__ is set to '__main__'
When imported as a module, __name__ is set to the module name

This allows code to run ONLY when the file is executed directly,
not when imported as a module.
"""

def main_function():
    """Function to demonstrate __name__ pattern."""
    print("This code runs when the file is executed directly!")
    print(f"Module name: {__name__}")

# Check if this file is run directly
if __name__ == "__main__":
    print("\nThis block executes when run directly:")
    main_function()
else:
    print("\nThis module was imported (not run directly)")
    print(f"Imported from: {__name__}")


# ================================================================================
#                     RELOADING MODULES
# ================================================================================

print("\n" + "-" * 40)
print("9. RELOADING MODULES")
print("-" * 40)

"""
Sometimes you need to reload a module after making changes.
importlib.reload() allows this without restarting Python.
"""

import importlib
import math

# To reload a module after changes:
# importlib.reload(math)

print("Using importlib.reload(module):")
print("  - Reloads a module after it's been imported")
print("  - Useful during development when modifying modules")
print("  - Not commonly needed in production")


# ================================================================================
#                     PACKAGES
# ================================================================================

print("\n" + "-" * 40)
print("10. PYTHON PACKAGES")
print("-" * 40)

"""
A PACKAGE is a directory containing multiple modules and a special
__init__.py file. It organizes related modules together.

Directory Structure:
-------------------
mypackage/
    __init__.py        # Makes it a package
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
"""

# Importing from packages
# import mypackage.module1
# from mypackage import module1, module2

# The __init__.py file
print("\n__init__.py file:")
print("  - Makes a directory a Python package")
print("  - Can contain initialization code")
print("  - Can explicitly define what gets imported with *")

# Package example structure
print("\nPackage example:")
print("""
mypackage/
├── __init__.py       # from mypackage import *
├── utils.py          # Helper functions
├── math_helpers.py   # Math utilities
└── data/
    ├── __init__.py
    ├── reader.py
    └── writer.py
""")


# ================================================================================
#                     MODULE SEARCH ORDER
# ================================================================================

print("\n" + "-" * 40)
print("11. MODULE SEARCH ORDER")
print("-" * 40)

"""
When you write 'import foo', Python searches in this order:

1. Built-in modules (math, sys, etc.)
2. Current directory
3. PYTHONPATH directories
4. Installation-dependent default directories

You can find where a module is located using __file__ attribute.
"""

import math
import sys

print(f"math module location: {math.__file__}")
print(f"sys module location (built-in): {sys}")
print(f"Current working directory: {os.getcwd()}")


# ================================================================================
#                     HANDLING IMPORTS CORRECTLY
# ================================================================================

print("\n" + "-" * 40)
print("12. BEST PRACTICES FOR IMPORTS")
print("-" * 40)

# Good import patterns
print("\n✓ GOOD IMPORT PATTERNS:")

# 1. Standard library imports first
import os
import sys
import json

# 2. Third-party imports second
# import numpy as np
# import pandas as pd

# 3. Local application imports last
# from myapp import models

# Use specific imports
from math import pi, e  # ✓ Better than: import math

# Use aliases for long module names (third-party)
# import numpy as np  # ✓
# import pandas as pd  # ✓

# Avoid wildcard imports
# from math import *  # ✗ Bad - pollutes namespace

print("""
✓ Import order:
  1. Standard library
  2. Third-party
  3. Local modules

✓ Use: from module import specific_items
✓ Use: import module as alias (for readability)
✓ Avoid: from module import * (pollutes namespace)

✓ Always check if module exists before import:
  try:
      import mymodule
  except ImportError:
      print("Module not found")
""")


# ================================================================================
#                     THE dir() FUNCTION
# ================================================================================

print("\n" + "-" * 40)
print("13. EXPLORING MODULES WITH dir()")
print("-" * 40)

"""
dir(module) returns a list of all attributes and methods
available in a module.
"""

import math

# Get all attributes of math module
math_attrs = dir(math)
print(f"Number of attributes in math: {len(math_attrs)}")
print(f"\nFirst 15 attributes: {math_attrs[:15]}")

# Filter specific types
print("\nFunctions in math module:")
funcs = [attr for attr in dir(math) if callable(getattr(math, attr)) and not attr.startswith('_')]
print(f"  {funcs[:10]}...")

# Constants in math module
print("\nConstants in math module:")
constants = [attr for attr in dir(math) if not callable(getattr(math, attr)) and not attr.startswith('_')]
print(f"  {constants}")


# ================================================================================
#                     THE getattr() FUNCTION
# ================================================================================

print("\n" + "-" * 40)
print("14. DYNAMIC ATTRIBUTE ACCESS WITH getattr()")
print("-" * 40)

"""
getattr(module, 'attribute_name') allows accessing module
attributes dynamically using strings.
"""

import math

# Dynamic attribute access
attr_name = "pi"
print(f"getattr(math, '{attr_name}') = {getattr(math, attr_name)}")

attr_name = "sqrt"
print(f"getattr(math, '{attr_name}')(25) = {getattr(math, attr_name)(25)}")

# With default value
print(f"getattr(math, 'nonexistent', 'default') = {getattr(math, 'nonexistent', 'default')}")

# Practical use: iterate through module attributes
print("\nAll functions in math module:")
for attr in dir(math):
    if not attr.startswith('_') and callable(getattr(math, attr, None)):
        print(f"  {attr}()")


# ================================================================================
#                     MODULE VS SCRIPT
# ================================================================================

print("\n" + "-" * 40)
print("15. MODULE VS SCRIPT")
print("-" * 40)

"""
MODULE: A .py file meant to be imported
SCRIPT: A .py file meant to be run directly

The key difference is how __name__ is set:
- Run directly: __name__ == '__main__'
- Imported: __name__ == 'module_name'
"""

def module_example():
    """Example function to demonstrate module behavior."""
    print(f"Running in: {__name__}")
    if __name__ == "__main__":
        print("This is being run as a script")
    else:
        print("This is being imported as a module")

print("module_example():")
module_example()


# ================================================================================
#                     PRACTICAL EXAMPLES
# ================================================================================

print("\n" + "-" * 40)
print("16. PRACTICAL EXAMPLES")
print("-" * 40)

# Example 1: Creating a utility module
print("\nExample 1: Utility module pattern")

class StringUtils:
    """A utility class for string operations."""
    
    @staticmethod
    def reverse(s):
        return s[::-1]
    
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]
    
    @staticmethod
    def word_count(s):
        return len(s.split())

utils = StringUtils()
print(f"  reverse('hello'): {utils.reverse('hello')}")
print(f"  is_palindrome('radar'): {utils.is_palindrome('radar')}")
print(f"  word_count('hello world'): {utils.word_count('hello world')}")

# Example 2: Configuration module
print("\nExample 2: Configuration module pattern")

class Config:
    """Configuration settings."""
    DEBUG = True
    DATABASE_URL = "localhost:5432"
    MAX_CONNECTIONS = 100
    
    @classmethod
    def get(cls, key, default=None):
        return getattr(cls, key, default)

print(f"  Config.DEBUG: {Config.DEBUG}")
print(f"  Config.get('DATABASE_URL'): {Config.get('DATABASE_URL')}")
print(f"  Config.get('NONEXISTENT', 'default'): {Config.get('NONEXISTENT', 'default')}")

# Example 3: Module as singleton
print("\nExample 3: Singleton pattern in module")

# In a module file, top-level variables are effectively singletons
module_data = {"initialized": True}

def get_shared_data():
    """Access shared module data."""
    return module_data

print(f"  Shared data: {get_shared_data()}")


# ================================================================================
#                     COMMON MODULE PATTERNS
# ================================================================================

print("\n" + "-" * 40)
print("17. COMMON MODULE PATTERNS")
print("-" * 40)

# Pattern 1: Facade pattern
print("\nPattern 1: Facade - Simplified interface")
"""
# Use a single import for multiple submodules
import包.ecommerce
from 包.ecommerce import Customer, Order, Payment
"""

# Pattern 2: Plugin architecture
print("\nPattern 2: Plugin/Factory pattern")
"""
# Dynamic module loading for plugins
import importlib
plugin = importlib.import_module(f"plugins.{plugin_name}")
plugin.initialize()
"""

# Pattern 3: Lazy imports
print("\nPattern 3: Lazy imports (defer expensive imports)")
"""
def heavy_computation():
    import heavy_module  # Only imported when needed
    return heavy_module.process()
"""

# Pattern 4: Circular import handling
print("\nPattern 4: Avoiding circular imports")
"""
Solution 1: Move import to function
Solution 2: Import from parent package
Solution 3: Restructure code to avoid cycles
"""


# ================================================================================
#                     MODULES AND PYTHON PATH
# ================================================================================

print("\n" + "-" * 40)
print("18. PYTHON PATH AND MODULES")
print("-" * 40)

# Understanding where Python looks for modules
import sys
import os

print("Python module search locations:")
print(f"\n1. Current directory: {os.getcwd()}")
print(f"2. PYTHONPATH: {sys.path[0] if sys.path else 'Not set'}")
print(f"3. Installation directory: {sys.prefix}")
print(f"4. Standard library: {sys.exec_prefix}")

# Adding to path at runtime
print("\nAdding custom path at runtime:")
# sys.path.insert(0, '/path/to/your/modules')


# ================================================================================
#                     THIRD-PARTY MODULES
# ================================================================================

print("\n" + "-" * 40)
print("19. USING THIRD-PARTY MODULES")
print("-" * 40)

"""
Third-party modules are installed using pip (package installer).
Commonly used packages:
"""

# Examples of popular third-party modules
print("""
pip install numpy      # Numerical computing
pip install pandas     # Data analysis
pip install requests   # HTTP requests
pip install flask      # Web framework
pip install django     # Full-stack framework
pip install matplotlib # Plotting
pip install pytest     # Testing
pip install beautifulsoup4  # Web scraping
""")

# Using pip from command line:
# pip install package_name
# pip list  # Show installed packages
# pip uninstall package_name


# ================================================================================
#                     MODULE DEPENDENCIES
# ================================================================================

print("\n" + "-" * 40)
print("20. CHECKING MODULE DEPENDENCIES")
print("-" * 40)

# Check if a module is available
def import_module_safe(module_name):
    """Try to import a module, return True if successful."""
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False

modules_to_check = ['math', 'json', 'requests', 'numpy', 'pandas']
print("Checking module availability:")
for module in modules_to_check:
    available = import_module_safe(module)
    print(f"  {module}: {'✓ Available' if available else '✗ Not found'}")


# ================================================================================
#                     PYTHON STANDARD LIBRARY OVERVIEW
# ================================================================================

print("\n" + "-" * 40)
print("21. PYTHON STANDARD LIBRARY CATEGORIES")
print("-" * 40)

print("""
Core Modules:
  - builtins    : Built-in functions and types
  - sys         : System-specific parameters
  - os          : OS interface
  - io          : I/O operations

Data Types:
  - datetime    : Date and time
  - collections : Container datatypes
  - json        : JSON encoding
  - csv         : CSV file handling

Algorithms:
  - itertools   : Iterator functions
  - functools   : Higher-order functions
  - operator    : Functional operators

Text Processing:
  - re          : Regular expressions
  - string      : String operations
  - textwrap    : Text wrapping

File & Directory:
  - pathlib     : Object-oriented paths
  - glob        : File name patterns
  - shutil      : File operations

Testing:
  - unittest    : Unit testing framework
  - doctest     : Test from docstrings

Networking:
  - socket      : Low-level networking
  - http        : HTTP modules
  - urllib      : URL handling
""")


# ================================================================================
#                     ERRORS AND EXCEPTIONS
# ================================================================================

print("\n" + "-" * 40)
print("22. IMPORT ERRORS AND HANDLING")
print("-" * 40)

# Common import errors and solutions

# 1. ModuleNotFoundError
print("\n1. ModuleNotFoundError - Module doesn't exist")
print("   Solution: Install package or check spelling")

# 2. ImportError
print("\n2. ImportError - Import failed")
print("   Solution: Check module structure and __init__.py")

# 3. AttributeError
print("\n3. AttributeError - Attribute doesn't exist")
print("   Solution: Check module's exported attributes")

# Safe import pattern
print("\nSafe import pattern:")
try:
    import mymodule
    print("  ✓ Import successful")
except ImportError as e:
    print(f"  ✗ Import failed: {e}")


# ================================================================================
#                     BEST PRACTICES
# ================================================================================

print("\n" + "-" * 40)
print("23. BEST PRACTICES")
print("-" * 40)

print("""
1. ORGANIZE CODE INTO MODULES
   - Each file should have a single responsibility
   - Group related functionality together

2. USE DESCRIPTIVE NAMES
   - Good: database_utils.py, user_auth.py
   - Bad: utils.py, helpers.py (too generic)

3. DOCUMENT YOUR MODULES
   - Add docstrings at module level
   - Document public functions/classes

4. USE __all__ TO CONTROL EXPORTS
   __all__ = ['function1', 'ClassA']  # Only these are imported with *

5. HANDLE IMPORTS CORRECTLY
   - Import order: stdlib → third-party → local
   - Use specific imports when possible

6. USE EXCEPTION HANDLING
   try:
       import mymodule
   except ImportError:
       # Handle missing module

7. AVOID CIRCULAR IMPORTS
   - Import at function level if needed
   - Restructure code to break cycles

8. VERSION YOUR MODULES
   __version__ = "1.0.0"

9. CREATE __init__.py FOR PACKAGES
   - Makes directories importable as packages

10. USE TYPE HINTS
    - Improves code clarity and IDE support
""")


# ================================================================================
#                     SUMMARY
# ================================================================================

print("\n" + "=" * 80)
print("                         KEY TAKEAWAYS")
print("=" * 80)
print("""
┌─────────────────────────────────────────────────────────────────────────────┐
│  WHAT IS A MODULE?                                                          │
│  ───────────────                                                            │
│  • A .py file containing Python code                                        │
│  • Can contain functions, classes, variables                                │
│  • Imported using 'import' statement                                         │
│                                                                             │
│  IMPORTING MODULES                                                          │
│  ───────────────                                                            │
│  • import module_name                                                        │
│  • from module_name import item                                              │
│  • import module_name as alias                                               │
│  • from module_name import * (avoid!)                                       │
│                                                                             │
│  MODULE ATTRIBUTES                                                           │
│  ───────────────                                                            │
│  • __name__    : Module name                                                 │
│  • __file__    : File path                                                   │
│  • __doc__     : Docstring                                                   │
│  • __dict__    : Namespace dictionary                                        │
│                                                                             │
│  PACKAGES                                                                    │
│  ────────                                                                    │
│  • Directory with __init__.py                                                │
│  • Contains multiple modules                                                 │
│  • Organized hierarchically                                                  │
│                                                                             │
│  BEST PRACTICES                                                              │
│  ──────────────                                                             │
│  • Use specific imports                                                      │
│  • Follow import order (stdlib → third-party → local)                       │
│  • Document modules with docstrings                                          │
│  • Use __all__ to control exports                                            │
└─────────────────────────────────────────────────────────────────────────────┘
""")

print("=" * 80)
print("               PYTHON MODULES TUTORIAL COMPLETE!")
print("=" * 80)
print("""
Topics Covered:
✓ Basic Concepts
✓ Creating Your First Module
✓ Importing Modules (5 methods)
✓ Built-in Modules (os, sys, datetime, random, json, etc.)
✓ The importlib Module
✓ Module Attributes (__name__, __file__, __doc__, etc.)
✓ Understanding sys.path
✓ Creating Custom Modules
✓ The __name__ == '__main__' Pattern
✓ Reloading Modules
✓ Packages
✓ Module Search Order
✓ Best Practices for Imports
✓ The dir() Function
✓ getattr() Function
✓ Module vs Script
✓ Practical Examples
✓ Common Module Patterns
✓ Python Path
✓ Third-Party Modules
✓ Module Dependencies
✓ Standard Library Overview
✓ Import Errors Handling
✓ Best Practices
""")
print("=" * 80)
print("                    Happy Coding! 🚀")
print("=" * 80)

