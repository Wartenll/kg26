from ipaddress import ip_network

def f(ip):
    ip_bin = f'{int(ip):032b}'
    third_byte = ip_bin[16:24]
    fourth_byte = ip_bin[24:32]
    return third_byte.count('0') > fourth_byte.count('0')

cnt = 0
for A in range(256):
    net = ip_network(f'246.81.65.{A}/255.255.255.224', strict=False)
    if all(f(ip) for ip in net):
        cnt += 1

print(cnt)