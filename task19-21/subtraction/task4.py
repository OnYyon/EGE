import math


def f(x, pos, wins):
    if x <= 19:
        return pos in wins
    if pos > max(wins):
        return 0

    moves = [
        f(x - 1, pos + 1, wins),
        f(math.ceil(x / 2), pos + 1, wins),
    ]

    if pos % 2 != max(wins) % 2:
        return any(moves)
    return all(moves)


for s in range(20, 1000):
    if f(s, 0, [2]) == 1:
         print(f"19 - {s}")
    if f(s, 0, [1]) == 0 and f(s, 0, [3]) == 1:
        print(f"20 - {s}")
