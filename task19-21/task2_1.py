# for 19 example with inversion
def f_19(x1: int, x2: int, pos: int, win_pos: list):
    if x1 + x2 > 75:
        return pos in win_pos
    if pos > max(win_pos):
        return 0

    moves =  [
        f_19(x1 + 1, x2, pos + 1, win_pos),
        f_19(x1 * 2, x2, pos + 1, win_pos),
        f_19(x1, x2 + 1, pos + 1, win_pos),
        f_19(x1, x2 * 2, pos + 1, win_pos),
    ]

    if pos % 2 != max(win_pos) % 2:
        return any(moves)
    else:
        return any(moves)


lst_19 = []
for i in range(1, 67):
    if f_19(8, i, 0, [2]) == 1:
        lst_19.append(i)
print(f"#19 - {min(lst_19)}")


# for 20 and 21 with normal condition
def f_another(x1, x2, pos, win_pos):
    if x1 + x2 >= 75:
        return pos in win_pos
    if pos > max(win_pos):
        return 0

    moves = [
        f_another(x1 + 1, x2, pos + 1, win_pos),
        f_another(x1 * 2, x2, pos + 1, win_pos),
        f_another(x1, x2 + 1, pos + 1, win_pos),
        f_another(x1, x2 * 2, pos + 1, win_pos),
    ]

    if pos % 2 != max(win_pos) % 2:
        return any(moves)
    else:
        return all(moves)


lst_20 = []
lst_21 = []
for i in range(1, 67):
    if f_another(8, i, 0, [1, 3]) == 1 and f_another(8, i, 0, [1]) == 0:
        lst_20.append(i)
    if f_another(8, i, 0, [2, 4]) == 1 and f_another(8, i, 0, [2]) == 0:
        lst_21.append(i)

print(f"#20 - {sorted(lst_20)}")
print(f"#21 - {min(lst_21)}")
