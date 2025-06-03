print(".".join(f"{int(bin(int(i))[2:]):08}" for i in "11.156.152.142".split(".")))
print(".".join(f"{int(bin(int(i))[2:]):08}" for i in "11.156.157.39".split(".")))

# net
print(11 & 11, 156 & 156, 152 & 157, 142 & 39, sep=".")
print(".".join(f"{int(bin(int(i))[2:]):08}" for i in "11.156.152.6".split(".")))
print(int("11111000", 2))