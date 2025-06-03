from fnmatch import fnmatch

# for i in range(447361, 10_000_000_000):
#     if fnmatch(str(i), "4*4736*1") and i % 7993 == 0:
#         print(i)
#         break

for i in range(44736821, 10**10, 7993):
    if fnmatch(str(i), "4*4736*1"):
        print(i, i // 7993)
