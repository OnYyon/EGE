def f(x, pos, wins):
    if x >= 169:
        return pos in wins
    if max(wins) < pos:
        return 0

    moves = [
        f(x + 1, pos + 1, wins),
        f(x * 3, pos + 1, wins),
    ]

    if pos % 2 == wins[-1] % 2: # Peter
        return any(moves)
    return all(moves) # Petya


print([s for s in range(1, 169) if f(s, 0, [1, 3]) == 1])
print([s for s in range(1, 169) if f(s, 0, [2]) == 0 and f(s, 0, [2, 4])])
print([s for s in range(1, 169) if f(s, 0, [1, 3, 5]) == 1 and f(s, 0, [1, 3]) == 0])
