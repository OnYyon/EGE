def f(x, pos, win_pos):
    if x >= 21:
        return pos in win_pos
    if pos > max(win_pos):
        return 0

    moves = [
        f(x + 1, pos + 1, win_pos),
        f(x * 2, pos + 1, win_pos),
    ]

    if pos % 2 != max(win_pos) % 2:
        return any(moves)
    else:
        return all(moves)


lst_19 = []
lst_20 = []
for i in range(1, 21):
    if f(i, 0, [1]) == 0 and f(i, 0, [3]) == 1:
        lst_19.append(i)
    if f(i, 0, [2, 4]) == 1 and f(i, 0, [2]) == 0:
        lst_20.append(i)
    if f(i, 0, [1, 3, 5]) == 1 and f(i, 0, [1]) == 0 and f(i, 0, [1, 3]) == 0:
        print(f"21 - {i}")

print(f"19 - {min(lst_19)}")
print(f"20 - {min(lst_20)}")
