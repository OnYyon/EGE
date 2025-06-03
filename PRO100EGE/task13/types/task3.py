import ipaddress as ip

network = ip.ip_network("192.168.32.96/27")

cnt = 0
for i in network:
    if bin(int(i))[2:].count("1") % 2 == 0:
        cnt += 1
print(cnt)
