def f(x1, x2, x3, pos, win_pos):
    if x1 + x2 + x3 >= 25 or max(x1, x2, x3) >= 20:
        return pos in win_pos
    if pos > max(win_pos):
        return 0

    moves = [
        f(x1 * 2, x2, x3, pos + 1, win_pos),
        f(x1, x2 * 2, x3, pos + 1, win_pos),
        f(x1, x2, x3 * 2, pos + 1, win_pos),
        f(x1 + 2, x2 + 2, x3 + 2, pos + 1, win_pos),
    ]

    if pos % 2 != max(win_pos) % 2:
        return any(moves)
    else:
        return all(moves)


for i in range(1, 20):
    if f(2, 3, i, 0, [2]) == 1:
        print(f"19 - {i}")
    if f(2, 3, i, 0, [3]) == 1:
        print(f"20 - {i}")
    if f(2, 3, i, 0, [2, 4]) == 1 and f(2, 3, i, 0, [2]) == 0:
        print(f"21 - {i}")