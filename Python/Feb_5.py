# WAP to reverse the given word without built in
'''
a = input()
b = ""
for i in a:
    b = i+b
print(b)
'''
# WAP to find the frequency of each character in a string
'''a = input()
b = {}
for i in a:
    b[i] = b.get(i,0) + 1 # res[i] = res.get(i,0) + 1
print(b) # prints in a dictionary''' 
'''
a = input()
res = {}
for i in a:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1
for i,j in res.items():
    print(f"{i} : {j}")
'''
# You are given a word containing unique characters. Find the position at which the required character is present
'''
a = input()
b = input()
c = 0
for i in a:
    if i == b:
        print(c+1)
        break # only the first occurence will be given as output
    c += 1
'''
# While loop :
'''
It is a condition based loop
while loop goes for the next iteration only when the the condition corresponding to it evaluates to be True
when the value of the condition becomes False, then the control goes to the next line after the loop

Syntax :
initialization code
while condition:
    loop body
    updation code
'''
# WAP to print natural numbers till given n
'''
a = int(input())
c = 1
while c <= a:
    print(c)
    c += 1
'''
# WAP to print sum of natural numbers till given n
'''
a = int(input())
c = 1
res = 0
while c <= a:
    res += c
    c += 1
print(res)
'''
# WAP to find factorial of a number using while loop
'''
a = int(input())
c = 1
while c <= a:
    print(c*a)
    c += 1
'''    
















    
