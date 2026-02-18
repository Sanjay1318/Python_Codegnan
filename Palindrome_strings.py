n = input("Enter a String : ")
#print("Palindrome String" if n == n[::-1] else "Not a Palindrome")
i = 0
j = len(n) - 1
res = True
while i < j:
    if n[i] == n[j]:
        pass
    else:
        res = False
    i += 1
    j -= 1
print("Palindrome String" if res else "Not a Palindrome")