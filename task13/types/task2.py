import ipaddress as ip

network = ip.ip_network("192.168.32.96/28")

cnt = 0
for ip in network:
    ip_bin = f"{bin(int(ip))[2:].zfill(32)}"
    if ip_bin.count("1") % 2 == 1:
        cnt += 1
print(cnt)