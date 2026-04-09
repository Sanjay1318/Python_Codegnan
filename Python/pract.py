# palindrome
'''
n = input()
rev = ""
for i in range(len(n)-1,-1,-1):
    rev += n[i]
if rev == n:
    print("Palindrome")
else:
    print("Not a Palindrome")
'''
'''
# vowels
n = input().lower()
count = 0
for i in range(len(n)):
    if n[i] in "aeiou":
        count += 1
print(count)
'''
# second largest number in a list without using sort function
'''
n = list(map(int,input().split()))
largest = n[0]  
second_largest = n[0]
for i in n:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print(second_largest)
'''

# import random
# import time

# email = input("Enter your email: ")
# password = input("Enter your password: ")

# # Generate OTP
# otp = random.randint(1000, 9999)
# print("Your OTP is:", otp)

# attempts = 1

# while attempts < 10:
#     user_otp = int(input("Enter OTP: "))

#     if attempts == 5:
#         print("Too many attempts. Try again after 5 seconds...")
#         time.sleep(5)

#     if user_otp == otp:
#         print("Login Successful!")
#         break
#     else:
#         attempts += 1
#         print("Wrong OTP")

    # if attempts == 5:
    #     print("Too many attempts. Try again after 5 seconds...")
    #     time.sleep(5)


# from datetime import date
# a = date.today()
# print(a.year)
# print(a.month)

 
def solveNQueens(n):

    board = [["." for _ in range(n)] for _ in range(n)]
    res = []

    cols = set()
    diag1 = set()  # r-c
    diag2 = set()  # r+c

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return

        for c in range(n):

            if c in cols or (r-c) in diag1 or (r+c) in diag2:
                continue

            board[r][c] = "Q"
            cols.add(c)
            diag1.add(r-c)
            diag2.add(r+c)

            backtrack(r+1)

            board[r][c] = "."
            cols.remove(c)
            diag1.remove(r-c)
            diag2.remove(r+c)

    backtrack(0)
    return res


n = int(input())
solutions = solveNQueens(n)

for sol in solutions:
    for row in sol:
        print(row)
    print()