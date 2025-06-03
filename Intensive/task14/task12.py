for x in range(1, 2031):
    n = 3**100 - x
    k = 0
    while  n > 0:
      k += n%3 == 0
      n //= 3
    if k == 1:
        print(x)
