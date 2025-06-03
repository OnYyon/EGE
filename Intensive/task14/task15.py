from string import printable

for x in printable[:15]:
    for y in printable[:17]:
        n = int(f"123{x}5", 15) + int(f"67{y}9", 17)
        if n % 131 == 0:
            print(n // 131, x, y)