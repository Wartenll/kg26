from itertools import permutations

alph = sorted('КИДАЛА')
ans = set()
for val in permutations(alph, r=5):
    val = ''.join(val)
    if 'АА' not in val:
        ans.add(val)
res = len(ans)
print(res)
