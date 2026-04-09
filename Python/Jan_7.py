# Identity Operators
''' These are the keywords used to check if two variables are pointing to the same object in the memory

    identity function : id() function returns the address of the operator written in the ()
    
    is and is not are the operators

    working of is :
    If both are same, is will return True else it will return False

    working of is not : (Opposite of  is)
    If both are not the same, is not will return True else it will return False

    Mutable  and  Immutable
    int is immutable
    float is immutable
    str is immutable
    list is mutable
    tuple is immutable
    set is mutable
    dict is mutable
'''

# Bitwise Operators
'''  These are special symbols used for bit level manipulations (total 6)

    bitwise and (&) : If both the bits under comparision are 1 then the resultant will be 1,  else the resultant will be 0
                                        Compares bit by bit 

        a = 5 # binary - 0101
        b = 3 # binary - 0011
        print(a & b) # internal result - 0001 and prints 1

    bitwise or (|) : If one of the bits is 1 then the resultant will be 1 else 0

        a = 5 # binary - 0101
        b = 3 # binary - 0011
        print(a | b) # internal result - 0111 and prints 7

    bitwise XOR (^) : If both the bits under comparision are different, the resultant will be 1, else 0
                                         if both the bits are same 1 and 1 or 0 and 0 it returns 0
                                         if both the bits are different 1 and 0 or 0 and 1 then it returns 1

        a = 5 # binary - 0101
        b = 3 # binary - 0011
        print(a ^ b) # internal result - 0110 and prints 6

    bitwise not (~) : It is an unary operator that inverts the bits from 0 to 1 and 1 to 0
                                        ~n = -(n+1)   n should be considered with the sign(+ or -)
                                        example : if n = -5 then -(-5+1) = -(-4) = 4 
                                        
        a = 5 # binary - 0101
        print(~a) # prints -6

    left shift (<<) : It is used to move bits to the left side by given number of positions
                                    When left shift is done, the number will be multiplied by 2^n

        a = 5 # binary - 0101
        print(a << 3) # a * 2^3 and prints 40

    right shift (>>) : It is used to move bits to the right side by given number of positions
                                       When left shift is done, the number will be divided by 2^n

        a = 10 # binary - 1010
        print(a >> 3) # a / 2^3 and prints 1
'''

# Question :
#   offer : Buy 2 get 60% off, Buy 1 get 30% off
#   input : 2 lines, first line number of products brought, second line price of each product assuming all are equal price
#   output : amount customer has to pay

a = int(input("Enter number of products brought "))
b = float(input("Price of each product "))

pairs = a // 2
single = a % 2

total = 0.4*b*pairs + 0.7*single*b

print("Total Amount to be paid is : " , total)




        
