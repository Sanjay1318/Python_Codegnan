'''
s = input("Enter a sentence ")

s.lower()

a = 0
e = 0
i = 0
o = 0
u = 0

for ch in s:
    if ch == "a":
        a +=1
    elif ch == "e":
        e += 1
    elif ch == "i":
        i +=1
    elif ch == "o":
        o += 1
    elif ch == "u":
        u += 1

print("a vowel occurs " , a , "times")
print("e vowel occurs " , e , "times")
print("i vowel occurs " , i , "times")
print("o vowel occurs " , o , "times")
print("u vowel occurs " , u , "times")

-------------------------------------------------------------------------------------------------------------------------------------------
'''
'''
s = input("Enter a sentence containing number names along with some text ")

digit_words = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}

result = ""

for ch in s:
    if  ch in digit_words:
        result += digit_words[ch]
    else:
        result += ch

print(result)

-------------------------------------------------------------------------------------------------------------------------------------------
'''
'''
s = input("Enter a String ")

res = s.lower()

char_list = list(res)

char_list.sort()

sorted_list = "".join(char_list)

print(sorted_list)

-----------------------------------------------------------------------------------------------------------------------------------------
'''
'''
s = input("Enter a Sentence ")

print(s.title())

-----------------------------------------------------------------------------------------------------------------------------------------
'''
'''
s = input("Enter a sentence containing number names along with some text ")

digit_letters = {
    "zero" : "0",
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

words = s.split()
result = []

for word in words:
    w = word.lower()   # to handle Two, TWO, etc.
    if w in digit_letters:
        result.append(digit_letters[w])
    else:
        result.append(word)

print(" ".join(result))
-----------------------------------------------------------------------------------------------------------------------------------------
'''

# Write a program to reverse a string.
'''
string = input("Enter a string : ")
print(string[::-1])
'''

# Write a program to check whether a number is even or odd.
'''
num = int(input("Enter a number : "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
'''

# Write a program to find the length of a list without using len().
'''
nums = list(map(int, input("Enter numbers : ").split()))
count = 0
for i in nums:
    count += 1
print(count)
'''

# Write a program to count vowels in a string.
'''
string = input("Enter a string : ")
s = string.lower()
print(s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u'))

'''

# Write a program to find the largest number in a list.
'''
nums = list(map(int,input("Enter numbers : ").split()))
print(max(nums))

# or

nums = list(map(int, input("Enter numbers : ").split()))
largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print(largest)
'''

# Write a program to remove duplicates from a list (keep order).
'''
nums = list(map(int, input("Enter numbers : ").split()))
new_list = []

for n in nums:
    if n not in new_list:
        new_list.append(n)

print(new_list)
'''















