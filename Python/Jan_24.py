# Functions for providing dynamic view on elements :
'''
1. keys() : it gives a view object with all the keys

a = {"name" : "bob" , "age" : 23, 23 : 32}
d_keys = a.keys()
print(d_keys) # dict_keys(['name', 'age', 23])
print(type(d_keys)) # <class 'dict_keys'>
d_keys = list(a.keys())
print(d_keys) # ['name', 'age', 23]
print(type(d_keys)) # <class 'list'>

2. values() : it gives a view object with all the values

a = {"name" : "bob" , "age" : 23, 23 : 32}
d_values = a.values()
print(d_values) # dict_values(['bob', 23, 32])
d_values = tuple(a.values())
print(d_values) # ('bob', 23, 32)

3. items() : it gives the key value pairs present in the dictionary

a = {"name" : "bob" , "age" : 23, 23 : 32}
d_items = a.items()
print(d_items) # dict_items([('name', 'bob'), ('age', 23), (23, 32)])
'''

# WAP to calculate the average marks for the marks given in the dictionary
'''
input : marks = {"Science" : 90,
                 "Maths" : 100,
                 "English" : 80}

output : The average of <number of subjects> subjects is <average>
'''
'''
marks = eval(input())
a = list(marks.values())
b = sum(a) / len(a)
print("The average of " , len(a) , "subjects is " , b) # The average of  3 subjects is  90.0
'''

# A persons weekly log of practice duration is given as input. Find the day no. of the week where he spent more on practice
#input : single line having space separated 7 numbes representing the durations for a week in minutes
#output : Day - <day no>
'''
example:
    input : 15 90 30 60 35 20 40
    output : Day - 2
'''
'''
inp = list(map(int,input().split()))
a = max(inp)
b = inp.index(a)
print("Day - ", b+1)
'''

# Set
''' A set is a mutable, unordered collection of unique and immutable elements enclosed in curly parantheses

s = {1, 2.34, True, False, "Python", (1,2,3)}
print(s) # {False, 1, 2.34, 'Python', (1, 2, 3)}

s = {1, 2.34, True, False, "Python", (1,2,3),[1,2], {1,2}, {"name" : "bob", "age" : 23}}
print(s) # TypeError : unhashable Type
'''

# set input :
'''
String elements :
s = set(input().split())

Integer elements :
s = set(map(int,input().split()))
'''

# WAP to find the number of distinct characters in given word
'''
input : codegnan
output : 7
'''
'''
s = set(input())
print(len(s))
'''
'''
# a = set()  --> empty set
a = set()
b = {}
print(type(a)) # <class 'set'>
print(type(b)) # <class 'dict'>
'''














