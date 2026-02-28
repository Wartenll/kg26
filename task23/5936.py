def f(start, end, cnt=0):
    if start == end: return 1
    if start < end: return 0
    if cnt != 40 and cnt != 49:return 0
    if start == end: return 1
    return f(start +1, end) + f(start + 3, end)+ f(start -1, end)+ f(start - 3, end)

print(f(42,42))