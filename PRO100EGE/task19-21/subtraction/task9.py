def f(x, pos, wins):
    if x == 0:
        return pos in wins
    if pos > max(wins):
        return 0

    moves = list()
    if x - 3 >= 0:
        moves.append(f(x - 3, pos + 1, wins))
    if x - 4 >= 0:
        moves.append(f(x - 4, pos + 1, wins))
    if x // 2 >= 0:
        moves.append(f(x // 2, pos + 1, wins))

    if pos % 2 != max(wins) % 2:
        return any(moves)
    return all(moves)


cnt = 0
print([s for s in range(1, 39) if f(s, 0, [2]) == 1])
print([s for s in range(1, 39) if f(s, 0, [1]) == 0 and f(s, 0, [3]) == 1])
print([s for s in range(1, 39) if f(s, 0, [2, 4]) == 1 and f(s, 0, [2]) == 0])
