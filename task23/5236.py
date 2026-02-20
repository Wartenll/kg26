def f(start, end, cnt):
    cnt += [start]
    if start == end and len(cnt) > 52: return 1
    if start > end: return 0
    return f(start + 2, end, cnt.copy) + f(start * 3, end, cnt.copy) + f(start * 4, end, cnt.copy)


print(f(2, 400,[]))
