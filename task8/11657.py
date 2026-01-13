from itertools import product
digits= '0123456789'
ans=set()
for val in product(digits[:8], repeat=6):
   if '3' not in val and val[0] != '0':
    if len(val) == len(set(val)):
        for i in range (len(val)-1):
            if int (val[i]) % 2 == 0 and int (val[i+1]) % 2 == 0:
                ans.add(val)
res = len(ans)
print(res)
