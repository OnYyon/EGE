def f(x1, x2, pos, win_pos):
    if x1  + x2 >= 49:
        return pos in win_pos
    if pos > max(win_pos):
        return 0

    moves = [
        f(x1 + 1, x2, pos + 1, win_pos),
        f(x1 * 3, x2, pos + 1, win_pos),
        f(x1, x2 + 1, pos + 1, win_pos),
        f(x1, x2 * 3, pos + 1, win_pos),
    ]

    if pos % 2 != max(win_pos) % 2:
        return any(moves)
    else:
        return all(moves)


for i in range(1, 43):
    # 4
    # if f(5, i, 0, [2]) == 1:
    #     print(f"#19 - {i}")
    if f(5, i, 0, [1, 3]) == 1 and f(5, i, 0, [1]) == 0:
        print(f"#20 - {i}")
    if f(5, i, 0, [2, 4]) == 1 and f(5, i, 0, [2]) == 0:
        print(f"#21 - {i}")
