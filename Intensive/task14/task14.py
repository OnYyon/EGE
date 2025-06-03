from string import printable

for x in printable[:15]:
    n = int(f"1{x}51", 15) - int(f"3{x}2", 15)
    if n % 4 == 0:
        print(n // 4)
