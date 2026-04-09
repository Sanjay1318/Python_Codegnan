# Loops
'''
Loops are the programming structures that helps us execute a block of code multiple times

In python , there are 2 types of loops

1. for loop - number of iterations based
2. while loop - condition based

1. for loop :
A for loop can be used when we know the exact number of times the loop has to run
The running of loop is termed as iteration
'''
'''
# WAP to print the characters present in a given word, every character on an individual line
a = input()
for i in range(len(a)):
    print(a[i])
'''
'''
# WAP to find the number of characters present in the given string without using len()
inp = input()
c = 0
for i in inp:
    c += 1
print(c)
'''
# WAP to find the sum of elements in given list
'''
input : single line space separated list elements
output : single int sum of all elements

a = list(map(int,input().split()))
print(sum(a))
'''
# Range :
''' built in function used in loops for produciong iterable with required number of elements
It takes a maximum of 3 arguments
start/stop/step
'''
# WAP to print the natural numbers till given n
'''
n = int(input())
for i in range(1,n+1):
    print(i)
'''
# WAP to print the first 10 multiples of a given number
'''
a = int(input())
for i in range(1,11):
    print(a*i)
'''
# WAP to print the first n even numbers
'''
n = int(input())
for i in range(1,n+1):
    if i % 2 == 0:
        print(i)
'''

