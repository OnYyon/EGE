from ipaddress import ip_network
print(".".join(f"{bin(int(i))[2:]:08}" for i in "11.92.135.56".split(".")))
print(".".join(f"{bin(int(i))[2:]:08}" for i in "255.244.0.0".split(".")))

# net
print(".".join(str(int(i, 2)) for i in "10110000.10111000.10000000.00000000".split(".")))


net = ip_network("176.184.128.0/255.244.0.0")
# lst = max(ip for ip in net.hosts())
