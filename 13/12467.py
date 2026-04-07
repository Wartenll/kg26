from ipaddress import ip_network


def f(ip):
    ip = f'{int(ip):032b}'
    return ip[16:].count('1') > 3


cnt = 0
while True:
    net = ip_network(f'183.192.{cnt}.0/255.255.252.0', False)
    if all(f(ip) for ip in net):
        print(cnt)
        break
    cnt += 1
