# JAVASCRIPT
    - it is a free open source scripting language which is used to send the data to backend using (API).
    - we use to store the data using variable
    - variable is created using var

# Rules for creating a variable:
    1. variable must start with a character aplhabet
    2. no special symbols are allowed except $ and _
    3. case sensitive
    4. keywords are not allows
    
# Data types in js:
    1. number       89,9.98,-87,-23.56
    2. string       " or "
    3. boolean      True or False
    4. undefined    garbage value
    5. null         not a garbage either 0 or null word
    6. bigint       large integer with letter n at the end 123456789876543234567652345678n
    7. symbol       creates a unique reference even same value
    8. object       combination of all the above mentioned data types

# Types of js:
    - Internal
    - External
    1. Internal:
        writing in the same html file using script tag
    2. External:
        writing in .js extension file and giving src inside script tag as attribute

# Operators in js:
    1. Arithematic              - (+,-,*,/,%)
    2. Assignment               - (=,+=,-=,/=,%=,*=)
    3. Relational               - (<,<=,>,>=,==,!=)
    4. Logical                  - (&&,||,!)
    5. Conditional or ternary   - (condition?(valid):(invalid))

Note: The Relational and Logical operators are going to work based on a conditional statement

- In js we are going to use two types of comments
    1. Single line comments (//Single line comments)
    2. Multi-line comment (/* Multi-line comment */)

- Conditional statements in JS:
    1. When we to perform an action based on a condition we are going to pass an expression to the conditional statement
    2. The expression is created using Relational and Logical operators
    3. These conditional statements are going to return a boolean value
- Types:
    1. if
    2. if else
    3. else if
    4. switch
    - we use curly braces as the block

-  Loops in JS:
    A loop is going to help us to execute a block of code multiple times it carries
        1. Initialization
        2. Condition
        3. Iteration
    We are having three types of loops
        1. While
        2. do While
        3. for
    But in js we are going to carry:
        1. for each
        2. for of 
        3. for in

# Functions in js:
    Functions are going to be used to execute multiple blocks of code 
    By using function keyword we will create a function
        Syntax:
            function functionname(arguments){
                statements;
                statements;
                return
            }
    To get a response from a function we use return keyword

# Arrays in js:
    Array is a combination of multiple values of different datatypes
    Array starts from position 0 and ends at (n-1) position
    There are few pre-defined methods in an array
    1. push : inserts at the end
    2. pop : deletes one value at the end
    3. shift : deletes one value at the start
    4. unshift : inserts multiple values at the start
    5. splice : inserts, deletes, updates multiple values at any position
        splice(position, no of values to delete, values you want to add)
    6. length : calculates the count of an array
    
# String methods in js:
    > toLowerCase() : converts the string to lowercase
    > toUpperCase() : converts the string to uppercase
    > toString() : converts the number to string
    > indexOf() : gives the index of the first occurrence of a specified value in a string
    > lastIndexOf() : gives the index of the last occurrence of a specified value in a string
    > substring() : extracts the characters from a string between two specified indices and returns the new sub string
    > substr() : extracts the characters from a string, starting at a specified index and returns the specified number of characters
    > join() : joins all the elements of an array into a string
    > charAt() : returns the character at a specified index in a string

# MATH FUNCTIONS:
    > Math.ceil() : rounds a number up to the nearest by converting to integer ex: 3.2 => 4
    > Math.floor() : rounds a number down to the nearest by converting to integer ex: 3.8 => 3
    > Math.round() : rounds a number to the nearest by converting to integer ex: 3.5 => 4, 3.2 => 3
    > Math.random() : generates a random number between 0 and 1
    > Math.max() : returns the largest of zero or more numbers
    > Math.min() : returns the smallest of zero or more numbers
    > Math.pow(base,exponent) : returns the base to the exponent power ex: Math.pow(2,3) => 8
    > Math.sqrt() : returns the square root of a number ex: Math.sqrt(16) => 4

# DATE METHODS:
    > get and set methods, instead of get place set for below methods
    > getFullYear() : returns the year of a date as a four digit number ex: 2024
    > getMonth() : returns the month of a date as a number between 0 and 11 ex: 0 for January, 1 for February, and so on
    > getDate() : returns the day of the month for a specified date as a number between 1 and 31
    > getDay() : returns the day of the week for a specified date as a number between 0 and 6 ex: 0 for Sunday, 1 for Monday, and so on
    > getHours() : returns the hour for a specified date as a number between 0 and 23
    > getMinutes() : returns the minutes for a specified date as a number between 0 and 59
    > getSeconds() : returns the seconds for a specified date as a number between 0 and 59
    > getTime() : returns the number of milliseconds since January 1, 1970 

    > toLocaleDateString() : returns a string with a language sensitive representation of the date portion of this date based on the locale and formatting options passed as arguments
    > toLocaleTimeString() : returns a string with a language sensitive representation of the time portion of this date based on the locale and formatting options passed as arguments
    > toTimeString() : returns the time portion of a Date object as a string, using locale conventions

# Note:
    By using Date() class we create an object for this class and use the date methods defined earlier.

# DOM Operations:
    In JavaScript, when we are trying to access the HTML content using js we are going to use events

    Events:
        > onclick : when we click on the element
        > onchange : when we change the value of the element
        > onsubmit : when we submit the form
        > onkeypress : when we press the key
        > onmouseover : when we hover the mouse on the element
        > onmouseout : when we move the mouse out of the element
        > onkeydown : when we press the key down
        > onkeyup : when we release the key
        > onload : when the page is loaded
        > onscroll : when we scroll the page

    Elements:
        > getElementById() : returns the element with the specified id
        > getElementsByClassName() : returns a collection of elements with the specified class name
        > getElementsByTagName() : returns a collection of elements with the specified tag name
        > querySelector() : returns the first element that matches a specified CSS selector(s) in the document
        > querySelectorAll() : returns a static NodeList of all the elements that match a
        specified CSS selector(s) in the document
        > createElement() : creates an element node with the specified name
        > setAttribute() : adds a new attribute or changes the value of an existing attribute on the specified element

    If you want to access text elements use -- innerHTML, innertext, textContent()
    If you want to access elements which used to read data like input, select use -- value
    
# Regular Expressions in JS:
    Regular expressions are patterns used to match character combinations in strings. 
    > /^ : indicates the start of a string
    > $/ : indicates the end of a string
    > + : matches the preceding element one or more times (0 or more occurrences / concatenation)
    > * : matches the preceding element zero or more times (1 or more occurrences)
    > [] : matches any one of the characters inside the brackets (rule written inside the brackets)
    > {} : matches the preceding element a specific number of times (length of the list)

# Local Storage in js:
    In javascript we can store some information on the browser by using local storage and session storage.
    This local storage is able to store upto 5mb only; even if we referesh the page, the data still remains exist until we clear it by ourself
        localStorage.setItem("itemname",value)
        localStorage.getItem("itemname")
        localStorage.removeItem("itemname")
        localStorage.clear()

# Session Storage in js:
    It is also same like local storage but the key difference is Session Storage will be flushed out whenever we refresh the page or closes the window
        sessionStorage.setItem("itemname",value)
        sessionStorage.getItem("itemname")
        sessionStorage.removeItem("itemname")
        sessionStorage.clear()

# ES6:
    ES6 stands for ECMAScript2015
    # Features
        > const
        > let
        > map
        > fliter
        > reduce
        > destrcuturing
        > arrow function / call back function
        > spread
        > find
        > asynchronous operations
            async 
            await
            setTimeout
            setInterval
            clearTimeout
            clearInterval
            promises
            event loop

# Synchronous vs Asynchronous
    Basically js is a synchronous application, means code will be executed line by line
    if you get an error in line 1, the program execution stops there itself and wont execute the remaining blocks of code until the error is cleared, so to make it asynchronous we will use es6 features
    
# QnA:
    # How do you give the connection between the frontend and backend ?
        Through using an API we are going to give the connection

    # What is an API ?
        API stands for : Application Programming Interface which looks like a url followed by end point

        example : https://www.google.com/search?q=
                    here, in above example the search?q= is the end point

    # What type of operations can be performed on an API ?
        CRUD:
            Create  : post
            Retrive : get
            Update  : put
            Delete  : delete

    # What is the response you are going to get from an API ?
        JSON : JavaScript Object Notation
        {
            "key":value,    //key always in double quotes
            "key":value,
            "key":value,
            "key":value,
     }

    # Where to integrate this API ?
        Can be integrated in frontend using JS, we are going to use fetch() an inbuilt method and a 3rd party package called as axios

    # Where are we going to create these APIs ?
        In backend using Python based frameworks (flask), Java based frameworks and other technologies(php,js)

# Promise in js:
    > fullfill
    > pending
    > reject
Promise((resolve,reject)=>{
    //code
})

