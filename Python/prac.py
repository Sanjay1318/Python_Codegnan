'''
def add():
    a = int(input())
    b = int(input())
    c = a+b
    print(c)
add()

def subtract():
    a = int(input())
    b = int(input())
    c = a-b
    print(abs(c))
subtract()

for i in range(5):
    x=1    
    m=""    
    for j in range(i+1):       
        m+=(str(x)+"^")  #1^       
        x+=1    
        print(m.rstrip("^")) 
'''

def range_x(start,stop = None,step = 1):
    if stop is None:
        stop = start
        start = 0
    if step == 0:
        print("Error : Step cannot be zero")
    base = []
    i = start
    while i < stop:
        base.append(i)
        i += 1
    return base[::step]
print(range_x(1,10,2))