import math


def f(x, y, pos, wins):
    if x + y <= 30:
        return pos in wins
    if pos > max(wins):
        return 0

    moves = [
        f(x - 1, y, pos + 1, wins),
        f(math.ceil(x / 2), y, pos + 1, wins),
        f(x, y - 1, pos + 1, wins),
        f(x, math.ceil(y / 2), pos + 1, wins),
    ]

    if pos % 2 != max(wins) % 2:
        return any(moves)
    return all(moves)


for s in range(12, 1000):
    if f(18, s, 0, [2]) == 1:
        print('№ 19:', s)
    if f(18, s, 0, [1]) == 0 and f(18, s, 0, [3]) == 1:
        print(f"20 - {s}")
    if f(18, s, 0, [2]) == 0 and f(18, s, 0, [2, 4]) == 1:
        print(f"21 - {s}")

