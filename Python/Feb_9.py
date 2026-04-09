# Patterns
''' Square Patterns
n = int(input())
for i in range(n):
        print(("*"+" ").lstrip()*n)
'''

''' Rectangle Pattern
l = int(input())
b = int(input())
for i in range(l): # (or)  for i in range(b): print("*" * l)
    for j in range(b):
        print("*" , end = " ")
    print()
'''

'''Hollow Square
n = int(input())
for i in range(n):
    if i == 0 or i == n - 1:
        print("* " * n)
    else:
        print("* " + "  " * (n - 2) + "*")
'''

'''Hollow Rectangle
l = int(input())
b = int(input())
for i in range(0,b):
    if i == 0 or i == b - 1:
        print("*"*l)
    else:
        print("*"+" "*(l-2)+"*")
'''

''' H - Patterns (always odd number of rows gurantee)
n = int(input())
mid = n // 2
for i in range(n):
    if i == mid:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")
'''

'''Right angled triangle
n = int(input())
for i in range(n+1):
    print("* "*i)
'''

'''Right angled triangle(same numbers)
n = int(input())
for i in range(n+1):
    print(str(i)*i)
'''

'''Right angled triangle(different numbers)
n = int(input())
for i in range(1, n + 1):
    row = ""
    for j in range(1, i + 1):
        row += str(j) + " "
    print(row)

# OR

n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
'''
'''Right angled triangle(alphabets)
n = int(input())
for i in range(1, n + 1):
    row = ""
    for j in range(i):
        row += chr(97 + j) + " "
    print(row)
'''










    
