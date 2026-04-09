# List Methods :
'''    Functions present in list class
        syntax : list.function_name()
'''
# Functions for adding elements:
''' append() : adds element at the end
a = [1,2,3]
a.append(4) 
print(a) # [1,2,3,4]

    insert() : adds element at a specific index
a = [1,2,3]
a.insert(1,4) 
print(a) # [1,4,2,3]

    extend() : adds a group of elements at the end
a = [1,2,3]
a.extend([4,5,6]) 
print(a) # [1,2,3,4,5,6]
'''

# Functions for removing elements:
''' pop() : removes the last element by default. If we specify the index, it removes at that particular index
a = [1,2,3]
a.pop() 
print(a) # [1,2]
a.pop(1)
print(a) # [1]

    remove() : it takes an element and removes its first occurance
a = [1,2,3,2,3]
a.remove(2)
print(a) # [1,3,2,3]

    clear() : removes all the elements from the list making it an empty list
a = [1,2,3,2,3]
a.clear()
print(a) # []
'''

# Methods for counting and searching
''' count() : returns the number of occurences for a given element
a = [1,2,3,2,3]
print(a.count(3)) # 2

    index() : returns the index corresponding to the first occurence of an element
a = [1,2,3,2,3]
print(a.index(2)) # 1

    sort() : sorts the elements present in list
a = [1,2,3,2,3]
a.sort()
print(a) # [1, 2, 2, 3, 3]

    reverse() : for reversing a list
a = [1,2,3,2,3]
a.reverse()
print(a) # [3,2,3,2,1]

    copy() : to create the copy of a given list
a = [1,2,3,2,3]
b = a.copy()
print(b) # [1, 2, 3, 2, 3]
'''

# Tuple
''' A tuple is an immutable, ordered, collection of heterogenous elements enclosed in round parantheses

Differences between List and Tuple :
List is mutable and Tuple is immutable
Tuples are faster when compared to Lists because of immutability
Lists are enclosed in [] and Tuples are enclosed in ()

t = (1,2,3,4,5,[1.2,"python"],(1,2),"python",1.2,{"a" : 1}, {1,2},True)
print(t) # returns the same
'''

# Tuple input :
''' tuple input with string elements
inp = tuple(input().split())

    tuple input with numbers as elements
inp = tuple(map(int,input().split()))

    single element tuple
a = (1,)
'''

# Operations on Tuples
''' 
    #Operators : + can be used for tuple concatenation
                                 * can be used for repetition
                                 These work on tuples as they are creating a new tuple object, not modifying the original object
t1 = (1,2)
t2 = (3,4,5)
new = t1 + t2
print(new) # (1, 2, 3, 4, 5)
print(t1 * 2) # (1, 2, 1, 2)
print(id(t1)) # returns location of t1
print(id(t2)) # returns location of t2
print(id(new)) #returns location of new

    #Built-in functions : Functions that work on iterables
                        example : min(), max(), sorted(), . . . . .

        Indexing can be used on tuples also similar to other iterables
'''

# Tuple Methods
'''  Tuple class functions : count() and index()
a = (1,2,3,3,2,1)
print(a.count(1)) # 2
print(a.index(1)) # 0
'''

# immutability behaviour of tuple
''' Tuple does not support item assignment, but if it is having mutable elements as members, then the elements in them can be changed
'''
t = (1,[9,8])
#t[1] = [10] -> returns TypeError
t[1][0] = [7]
print(t) # (1, [[7], 8])












































































































































































































