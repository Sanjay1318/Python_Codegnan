n = input("Enter a number : ")
x = abs(int(n))
total = 0
while x > 0:
    digit = x%10
    total = total * 10 + digit
    x = x//10
print("Palindrome Number" if abs(int(n)) == total else "Not a Palindrome Number")