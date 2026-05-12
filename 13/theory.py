#Библеотека  ipaddress
from ipaddress import *
# Конвертирует объект в ip_address
ip = ip_address('172.16.128.0')
# ФОрмирует все ip-адресса по зданному фй пи и маске
net = ip_network('172.16.128.0/255.255.192.0')