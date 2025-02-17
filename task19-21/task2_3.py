def f(x1, x2, pos, win_pos):
    if x1 + x2 >= 83:
        return pos in win_pos
    if pos > max(win_pos):
        return 0

    moves = [
        f(x1 + 1, x2, pos + 1, win_pos),
        f(x1 * 2, x2, pos + 1, win_pos),
        f(x1, x2 + 1, pos + 1, win_pos),
        f(x1, x2 * 2, pos + 1, win_pos),
    ]

    if pos % 2 != max(win_pos) % 2:
        return any(moves)
    else:
        return all(moves)


lst_21 = []
for i in range(1, 74):
    # 19
    # if f(9, i, 0, [2]) == 1:
    #     print(i)
    #     break
    if f(9, i, 0, [1]) == 0 and f(9, i, 0, [3]) == 1:
        print(f"#20 - {i}")
    if f(9, i, 0, [2, 4]) == 1 and f(9, i, 0, [2]) == 0:
        lst_21.append(i)

print(f"#21 - {min(lst_21)}")