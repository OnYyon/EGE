def f(x1, x2, pos: int, win_pos: list):
    if x1 + x2 >= 13:
        return pos in win_pos
    if pos > max(win_pos):
        return 0

    moves = [
        f(x1 + 1, x2, pos + 1, win_pos),
        f(x1 + 2, x2, pos + 1, win_pos),
        f(x1, x2 + 1, pos + 1, win_pos),
        f(x1, x2 + 2, pos + 1, win_pos),
    ]

    if pos % 2 != max(win_pos) % 2:
        return any(moves)
    else:
        return all(moves)


lst_20 = []
for i in range(1, 10):
    # 6
    if f(3, i, 0, [2]) == 1 and f(3, i, 0, [1]) == 1:
         print(i)
    if f(3, i, 0, [3]) == 1:
        lst_20.append(i)
    if f(3, i, 0, [4]) == 1 and f(3, i, 0, [2]) == 0:
        print(f"21 - {i}")

print(f"20 - {sorted(lst_20)}")