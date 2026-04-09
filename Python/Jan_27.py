'''
inp = input("enter mail : ")
password = input("Enter your password : ")

while True:
    confirm_password = input("Enter your password again : ")

    if confirm_password == password:
        print("Password matches")
        break
    else:
        print("Password doesn't match ! Try again")

'''
# Operations on sets :
'''
1. operators 
union : elements from both sets will be combined
                    | is the operator used
a = {1,2,3}
b = {2,4,5}
print(a|b) # {1, 2, 3, 4, 5}

intersection : common elements from both the sets
                                    & operator is used
a = {1,2,3}
b = {2,4,5}
print(a&b) # {2}

Difference : elements present only in first set
                               - operator is used
a = {1,2,3}
b = {2,4,5}
print(a-b) # {1, 3}

Symmetric difference : elements not common to both the sets
                                                        ^  operator is used
a = {1,2,3}
b = {2,4,5}
print(a^b) # {1, 3, 4, 5}

>= : is used for checking if the first set is a super set of second set
<= : is used for checking if first set is a subset of the second set


2. built-in functions :
All the functions that work on iterables work on sets
example : len(), min(), max(), sorted(), reversed(), sum(), . . . . . .

3. set is not indexable.
Accessing individual elements using indexing and slicing are not possible on sets

4. set methods : Functions present in a set class

syntax = set_obj.function()

Functions for adding new elements :
1. add(element) : 
 an element can be added to an existing list

 2. update(set) :
 adds multiple elements to the existing set

s = {1,2}
s.add(3)
print(s) # {1, 2, 3}
s.update({3,4,5})
print(s) # {1, 2, 3, 4, 5}

Functions for removing elements :
pop() : removes an arbitary element from the set
remove() : removes the given element , gives the error if the element is not present in the list
discard() : removes the given element , does not give the error if the element is not present in the list
clear() : removes all the elements

Function for performing set specific operations :
union(), intersection(), difference(), symmetric_difference()

a = {"a","b",1}
b = {1,2,3}
c = a.union(b) # same as a | b
print(c) # {1, 2, 3, 'b', 'a'}
c = a.intersection(b)
print(c) # {1}
c = a.difference(b)
print(c) # {'b', 'a'}
c = a.symmetric_difference(b)
print(c) # {2, 3, 'b', 'a'}
'''
'''
# Alex Bob Lilly Charles John
# Ron Bob Mike Rose Lilly Charles

set1 = set(input().split())
set2 = set(input().split())
common = set1.intersection(set2)
n = len(common)
sorted_names = sorted(common)
second_person = sorted_names[1]
print(n)
print(second_person)
'''
# unpacking of iterables : assigning elements present in a iterable to individual variables is called unpacking
'''
Tuple and List unpacking :

t = ("bob" , 21, 123456789) # can also be list
name,age,phone = t
print(name) # bob
print(age) # 21
print(phone) # 123456789
'''

















