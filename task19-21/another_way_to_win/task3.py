def f(x, pos, wins):
    if x >= 100:
        return pos in wins
    if pos > max(wins):
        return 0

    moves = [
        f(x + 2, pos + 1, wins),
        f(x + 4, pos + 1, wins),
        f(x * 2, pos + 1, wins),
    ]

    if pos % 2 == wins[0] % 2:
        return any(moves)
    return all(moves)


print([s for s in range(1, 100) if f(s, 0, [1, 3]) == 1])
print([s for s in range(1, 100) if f(s, 0, [3]) == 0 and f(s, 0, [1, 3, 5]) == 1])
print([s for s in range(1, 100) if f(1, 0, [2]) == 0 and f(s, 0, [2, 4]) == 1])
