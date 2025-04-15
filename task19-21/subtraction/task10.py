def f(x, y, pos, wins):
    if x + y <= 18:
        return pos in wins
    if pos > max(wins):
        return 0

    moves = list()
    if x - 1 > 0:
        moves.append(f(x - 1, y,  pos + 1, wins))
    if y - 1 > 0:
        moves.append(f(x, y - 1, pos + 1, wins))
    if x // 2 > 0:
        moves.append(f(x // 2, y, pos + 1, wins))
    if y // 2 > 0:
        moves.append(f(x, y // 2, pos + 1, wins))

    if pos % 2 != max(wins) % 2:
        return any(moves)
    return all(moves)


print([m for m in range(10, 1000) if f(m, m, 0, [2]) == 1])
print([s for s in range(6, 1000) if f(13 ,s, 0, [1]) == 0 and f(13, s, 0, [3]) == 1])
print([n for n in range(10, 1000) if f(n, n, 0, [2, 4]) == 1 and f(n, n, 0, [2]) == 0])
