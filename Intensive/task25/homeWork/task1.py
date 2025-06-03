from fnmatch import fnmatch

for x in range(0, 10**12, 98591):
  if fnmatch(str(x), '12?3*456??9'):
    print(x, x // 98591)