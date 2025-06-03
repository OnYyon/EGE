def f(x, y, pos, wins):
    if x + y >= 65:
        return pos in wins
    if max(wins) < pos:
        return 0

    moves = [
        f(x + 2, y, pos + 1, wins),
        f(x * 2, y, pos + 1, wins),
        f(x, y + 2, pos + 1, wins),
        f(x, y * 2, pos + 1, wins),
    ]

    if pos % 2 != max(wins) % 2:
        return any(moves)
    else:
        return all(moves)



for s in range(1, 60):
    # 19 - 15
    # if f(5, s, 0, [2]) == 1:
    #     print(f"19: {s}")
    # 20 - 27
    # if f(5, s, 0, [1]) == 0 and f(5, s, 0, [3]) == 1:
    #     print(s)
    if f(5, s, 0, [2, 4]) == 1 and f(5, s, 0, [2]) == 0:
        print(s)
