def f(x, y, pos, wins):
    if x + y >= 64:
        return pos in wins
    if pos > max(wins):
        return 0

    moves = [
        f(x + 1, y, pos + 1, wins),
        f(x + y, y, pos + 1, wins),
        f(x, y + 1, pos + 1, wins),
        f(x, y + x, pos + 1, wins),
    ]

    if pos % 2 != max(wins) % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 58):
    if f(6, s, 0, [2]) == 0 and f(6, s, 0, [2, 4]) == 1:
        print(s)
