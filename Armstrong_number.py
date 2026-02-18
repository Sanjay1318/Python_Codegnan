n = input("Enter a number : ")#.strip("-")
x = abs(int(n))
y = len(str(x))
total = 0
while x > 0:
    digit = x%10
    total += digit**y
    x = x//10
print("Armstrong Number" if abs(int(n)) == total else "Not An Armstrong Number")