# WAP to find the missing numbers in the number series, the series always starts from 1 and ends at some n.
# There will be a total of n-1 numbers as one number goes missing. Find that missing number.

''' input : 1 2 3 5 6 7 8
    output : 4

    input : 1 3 4 5 6
    output : 2
'''
'''
series = list(map(int,input("Enter number  series : ").split())) # 1 3 4 5 6 7 8 9

n = len(series) + 1
exp_sum = n * (n + 1) // 2
actual_sum = sum(series)

print(exp_sum - actual_sum) # 2
'''
'''
    missing square numbers
    
    input : 1 4 16 25
    output : 9

    input : 1 4 9 16 36 49 64
    output : 25
'''
'''
series = list(map(int,input("Enter number  series : ").split())) # 1 4 9 16 36 49 64

n = len(series) + 1
exp_sum = (n*(n+1)*(2*n+1)) // 6
actual_sum = sum(series)

print(exp_sum - actual_sum) # 25
'''

# WAP to find the number of characters present at even position in given string
'''
    input : python
    output : 3
'''
'''
string = input("Enter a String : ")
length_string = len(string) + 1
print(length_string // 2)
'''

# Operations on list :
'''
    1. Operators working on list :

            List concatenation (+) : used for joing elements of 2 or more lists

            List repetition (*) : used for repeating elements of a list

a = [1,2,3]
b = [4,5,6]
print(a+b) # [1, 2, 3, 4, 5, 6]
print(a*2) # [1, 2, 3, 1, 2, 3]

            Relational operators can be used
            Membership operators can be used
            Identity operators can be used

            The operators that are not supported throws  TypeError

        2. Indexing and Slicing of list :
        
                Indexing and slicing are similar to that of string data type

a = [1,2,3,4,6]
a[4] = 5
print(a) # [1, 2, 3, 4, 5]

                As list is mutable, elements at a particular position can be changed by reassingnment using index

        3. Built-in functions :
                The predefined functions that work on iterables will work on lists
                for example : min(), max(), sum(), sorted(), reverse(), . . . . . .
'''

# WAP to find the sum of even numbers from the given series of natural numbers from 1 to n.
'''
    input : 1 2 3 4 5 6
    output : 12
'''
'''
series = list(map(int,input("Enter number  series : ").split())) # 1 2 3 4 5 6
n = series[1::2]
sum_of_even_numbers = sum(n)
print(sum_of_even_numbers) # 12
'''





