# List
''' A List is an ordered, mutable collection of heterogenous elements enclosed in square brackets

lst = [12,23.43,True,"Python",[1,2,3],{1,2},(9,7),{1:"a"}]
print(lst)

list input :
a = "aa,bb,c,d"
lst = a.split(",")
print(lst) # ['aa', 'bb', 'c', 'd']

a = "aa bb c d"
lst = a.split(" ")
print(lst) # ['aa', 'bb', 'c', 'd']

# space separated elements input
lst = input("Enter elements : ").split()
print(lst) # ['1', '2', '3', '4']

# comma separated elements input
lst = input("Enter elements : ").split(",")
print(lst) # ['1', '2', '3', '4']
'''

# WAP to check how many words are given as input , input will be single line with space separated words,
# output should be a number saying how many words are there
'''
lst = input("Enter words : ").split()
length_lst = len(lst)
print(length_lst)
'''
# int
'''
nums = input("Enter numbers : ").split() #1 2 3 4 5 6
print(nums) # ['1', '2', '3', '4', '5', '6']
print(list(map(int,nums))) # [1, 2, 3, 4, 5, 6]

# or directly

lst = list(map(int,input("Enter numbers : ").split())) #1 2 3 4 5 6
print(lst) # [1, 2, 3, 4, 5, 6]
'''

# WAP to find the maximum element in the given numbers, input will be single line with space seperated numbers
'''
nums = list(map(int,input("Enter numbers : ").split())) # 23 34 56 76 12 34
max_num = max(nums)
print(max_num) # 76
'''

# WAP to sort the given numbers, input will be single line comma separated numbers, output should be a list with elements in ascending order
'''
nums = list(map(int,input("Enter numbers : ").split(","))) # 1,4,2,5,23,65,66
sorted_nums = sorted(nums)
print(sorted_nums) # [1, 2, 4, 5, 23, 65, 66]
'''

# WAP to find the second greatest element from the given elements, input will be single line comma seperated numbers, output should be a single number
'''
nums = list(map(int,input("Enter numbers : ").split(","))) # 1,4,2,5,23,65,66
sorted_nums = sorted(nums)
print(sorted_nums[-2]) # 65
'''

# WAP to find the average of the given numbers, input will be single line space separated numbers, output will be average of the given numbers
'''
nums = list(map(int,input("Enter numbers : ").split())) # 1 2 3 4 5 6
avg = sum(nums) / len(nums)
print("Average : {} ". format(avg)) # Average : 3.5
print("Average : ", avg) # Average :  3.5
'''















