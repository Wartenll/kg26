def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def M(n):
    total = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

count = 0
num = 1273547
while count < 5:
    num += 1
    m_val = M(num)
    if m_val % 100000 > 1 and is_prime(m_val % 100000):
        print(num, m_val)
        count += 1