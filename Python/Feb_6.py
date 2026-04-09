# You are designing a login system. you have to give a maximum of 3 attempts for entering correct password. incase the user enters correct password
# in any of these three attempts, then you should print "Logged in successfully" and not ask for password further
'''
a = input("User:")
b = input("Password:")
i = 1
while i <= 3:
    c = input("Enter Password again:")
    if b == c:
        print("Logged in Successfully")
        break
    print("Password Mismatch")
    i += 1
'''
# taking Matrix Input
'''
a = int(input("Enter number of rows:"))
l = []
for i in range(0,a):
    lst = list(map(int,input().split()))
    l.append(lst)
print(l) # nested list (matrix)
print("Sum of Diagonals:", (l[0][0] + l[1][1] + l[2][2]))
'''
# WAP to print the elements present in the matrix, each on an individual line
# Read the number of rows for the matrix
# We assume the matrix is square (rows = columns)
'''
a = int(input("Enter number of rows:"))
l = [] # List to store the matrix
d = 0 # Variable to store sum of principal diagonal elements
# ---------- INPUT SECTION ----------
# Taking input for each row of the matrix
for i in range(a):
    lst = list(map(int, input().split()))
    l.append(lst)
# ---------- PRINT ALL ELEMENTS ----------
# Printing all elements of the matrix line by line
for row in l:
    for val in row:
        print(val)
# ---------- ROW-WISE SUM ----------
# Printing the sum of each row
for row in l:
    print(sum(row))
# ---------- PRINCIPAL DIAGONAL SUM ----------
# Adding elements where row index == column index
for i in range(a):
    d += l[i][i]
print(d) # Printing sum of principal diagonal elements
'''


