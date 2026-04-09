# WAP to check if the given character input is a vowel or consonant
'''
inp = input().upper()
print("Vowel" if inp in "AEIOU" else "Consonant")
'''

# WAP to find the marks of the student from the given marks dictionary input
'''
input format :
    first line is marks dictionanry
    second line is name for searching
output format :
    Marks if the student is present else "Not Present" has to be printed
'''
'''
inp = eval(input())
stu = input()
if stu in inp:
    print(inp.get(stu)) # print(inp[stu])
else:
    print("Not Present")
'''
# WAP for designing billing systems. This should take total price as input and print what should be the final bill after applying the following discounts:
'''
1. if the total price is more than 20000, a discount of 15%
2. more than 10000, a discount of 10%
3. more than 5000, a discount of 5%
4. more than 1000, a discount of Rs.100
5. No discount in remaining cases
'''
'''
inp = float(input("Enter Bill amount : "))
if inp >= 20000:
    print("Bill amount after discount", inp - ((15/100) * inp))
elif inp >= 10000 and inp < 20000:
    print("Bill amount after discount", inp -((10/100) * inp))
elif inp >= 5000 and inp < 10000:
    print("Bill amount after discount", inp - ((5/100) * inp))
elif inp >= 1000 and inp < 5000:
    print("Bill amount after discount", inp - 100)
else:
    print("Bill amount after discount", inp)
'''

# WAP for grading students
'''
marks > 90 - A
marks > 80 - B
marks > 70 - C
marks > 60 - D
marks >= 60 - Fail
'''
'''
inp = int(input("Enter marks : "))
if inp > 90:
    print("Grade A")
elif inp > 80:
    print("Grade B")
elif inp > 70:
    print("Grade C")
elif inp > 60:
    print("Grade D")
else:
    print("Fail")
'''

# WAP to find the greatest of the given three numbers
'''
input : single line containing 3 numbers
output an integer greatest among given three
'''
'''
inp = list(map(int,input().split()))
print(max(inp))
'''










