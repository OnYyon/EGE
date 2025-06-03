print(".".join(bin(int(i))[2:] for i in "118.222.130.140".split(".")))
print(".".join(bin(int(i))[2:] for i in "118.222.201.140".split(".")))

# net
print(118 & 118, 222 & 222, 130 & 201, 140 & 140, sep=".")
print(".".join(bin(int(i))[2:] for i in "118.222.128.140".split(".")))
