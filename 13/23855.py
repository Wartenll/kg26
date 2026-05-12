from ipaddress import ip_network
net = ip_network('172.95.116.174/255.255.192.0', False)
print(str(min(net.hosts())).replace('.','+'))
