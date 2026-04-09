# WAP to find the count of even and odd nums in given list of nums
'''
a = list(map(int,input().split()))
e = 0
o = 0
for i in a:
    if i % 2 == 0:
        e += 1
    else:
        o += 1
print(e)
print(o)
'''
# WAP to print values only from the given dictionary
'''
a = eval(input())
for i in a:
    print(a.get(i))
'''
# WAP to calculate the total bill when the details of purchase are given as dictionary
'''
a = eval(input())
c = 0
for i in a.values():
    c += i
print(c)
'''
# WAP to find the grade of the student using the marks input
''' Rules for grading
    average > 90 - A
    average > 70 - B
    average > 50 - C
    Below that D
input format : dictionary with subject name as key and marks as values
output : Grade given to particular student
'''
'''
marks = eval(input())
s = 0
n = 0
for i in marks:
    s += marks[i]
    n += 1
avg = s//n
if avg > 90:
    print("A")
elif avg > 70:
    print("B")
elif avg > 50:
    print("C")
else:
    print("D")
'''

# Loop control statements :
'''
They are used to control the working of loop
1. break - used to exit a loop early
2. continue - to skip some steps in current iteration and move to next iteration

we can use else with loops
working:
    when the loop exits early using break, the else block of code will be skipped
    otherwise, the else block of code gets executed



















