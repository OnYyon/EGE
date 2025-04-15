def f(x, pos, wins):
    if x <= 15:
        return pos in wins
    if pos > max(wins):
        return 0

    moves = [
        f(x - 3, pos + 1, wins),
        f(x - 6, pos + 1, wins),
        f(x // 3, pos + 1, wins),
    ]

    if pos % 2 != max(wins) % 2:
        return any(moves)
    return all(moves)


for s in range(16, 1000):
    if f(s, 0, [2]) == 1:
          print(s)
    # if f(s, 0, [1]) == 0 and f(s, 0, [3]) == 1:
    #    print(s)
    # if f(s, 0, [2, 4]) == 1 and f(s, 0, [2]) == 0:
    #      print(s)
