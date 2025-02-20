import ipaddress as ipaddr

cnt = 0
ip = ipaddr.ip_address("71.192.0.12")
for i in range(33):
    try:
        net = ipaddr.ip_network("71.192.0.0/" + str(i))
        if ip in net:
            cnt += 1
    except Exception:
        continue
print(cnt)
