import ipaddress as ip

address = ip.ip_address("1.1.1.1")
print(type(address), address)
print(bin((int(address)))[2:])

network = ip.ip_network("192.168.32.128/28") # short
for i in network:
    print(i)

for ip in network.hosts(): # only for hosts
    ...

if ip.ip_address('111.81.208.27') in ip.ip_network('111.81.192.0/18'):
    print('IP-адрес 111.81.208.27 принадлежит сети.')
else:
    print('IP-адрес 111.81.208.27 не принадлежит сети.')


net = ip.ip_network('111.81.192.0/18')
print('Адрес сети:', net.network_address)
print('Маска сети:', net.netmask)


net = ip.ip_network('192.168.32.160/28')
count_uzl = len(list(net.hosts()))   # 14
count_ip = len(list(net))            # 16