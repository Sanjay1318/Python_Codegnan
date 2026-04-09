# WAP to find the length of the longest word in the given sentence
a = input().split(" ")
b = 0
for i in a:
    if len(i) > b:
        b = len(i)
print(b)
