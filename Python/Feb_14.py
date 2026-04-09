'''
n = input()
res = {}
for i in n:
    res[i] = res.get(i,0)+1
# print(res)
for keys,values in res.items():
    print(f"{keys}{values}",end="")
'''


