def f(x, y, pos, wins):
    if x + y >= 178:
        return pos in wins
    if pos > max(wins):
        return 0

    moves = [
        f(x + 4, y, pos + 1, wins),
        f(x, y + 3, pos + 1, wins),
        f(x * 2, y, pos + 1, wins),
        f(x, y * 3, pos + 1, wins),
    ]

    if pos % 2 != max(wins) % 2:
        return any(moves)
    else:
        return any(moves)


for s in range(1, 157):
    if f(21, s, 0, [2]) == 1:
        print(s)
