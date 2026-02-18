n = int(input("Enter a number : "))
a = 1
b = 0
print(b,end = " ")
print(a,end = " ")
n -= 2
for i in range(n):
    c = a+b
    print(c,end = " ")
    b = a
    a = c