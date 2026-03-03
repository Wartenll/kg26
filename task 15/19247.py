from itertools import combinations
def f(x,y):
    A=A1<=x<=A2
    return(x-3*y < A) or (y > 400) or (x>56)
line = [x for x in range(3,401) for eps in (0,0.1,0.9)]
ans= []
for A1,A2 in combinations(line, 2):
    if all(f(x,y) for x,y in line):
        ans.append(A2-A1)
print(max(ans))