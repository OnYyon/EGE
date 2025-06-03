def f(x, pos, wins):
    if x <= 19:
        return pos in wins
    if pos > max(wins):
        return 0

    moves = [
        f(x - 2, pos + 1, wins),
        f(x - 5, pos + 1, wins),
        f(x // 3, pos + 1, wins),
    ]

    if pos % 2 != max(wins) % 2:
        return any(moves)
    else:
        return all(moves)



for s in range(20, 1000):
    if f(s, 0 ,[1]) == 0 and f(s, 0, [3]) == 1:
        print(s)
