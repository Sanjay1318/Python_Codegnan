import sys
sys.setrecursionlimit(150000)
sys.set_int_max_str_digits(100000)
# factorial numbers
def fn_1(a):
    if a==0 :   # base case
      return 1
    else:
       return a*fn_1(a-1)  # recursive case
    
# print(fn_1(5000))

'''
a=5 
5*fn_1(4)
a=4
5*4*fn_1(3)
a=3
5*4*3*fn_1(2)
a=2
5*4*3*2*fn_1(1)
a=1
5*4*3*2*1*fn_1(0)
a=0
5*4*3*2*1*1=>  120
'''

#0,1,1,2,3,5,8,13,21,34,55,
# fibnocii number
def fibnocii_nuber(n):
   if n==0:
      return 0
   elif n==1:
      return 1
   else:
      return fibnocii_nuber(n-1)+fibnocii_nuber(n-2)
   
# print(fibnocii_nuber(5))

"""
n=5
fn(4)+fn(3)
fn(3)+fn(2)+fn(2)+fn(1)
fn(2)+fn(1)+fn(1)+fn(0)+fn(1)+fn(0)+fn(1)
fn(1)+fn(0)+fn(1)+fn(1)+fn(0)+fn(1)+fn(0)+fn(1)
1+0+1+1+0+1+0+1=5
"""

#sum of n natural numbers

x=5

def sum_natrl_nmbers(a):
   if a==1 :
      return 1
   elif a==0:
      return 1
   else:
      return a+sum_natrl_nmbers(a-1)
   
print(sum_natrl_nmbers(x))