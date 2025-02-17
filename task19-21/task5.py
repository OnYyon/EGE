def f(x, pos, win_pos) -> int:
    if x % 10 == 0:
        return pos in win_pos
    if pos > max(win_pos):
        return 0

    moves = [
        f(x + 1, pos + 1, win_pos),
        f(x + 3, pos + 1, win_pos),
        f(x + 11, pos + 1, win_pos),
    ]

    if pos % 2 != max(win_pos) % 2:
        return any(moves)
    else:
        return all(moves)


lst_19 = []
cnt_20 = 0
sum_21 = 0
for i in range(11, 100):
    if i % 10 == 0:
        continue
    if f(i, 0, [1]) == 0 and f(i, 0, [2]) == 1:
        lst_19.append(i)
    if f(i, 0, [1]) == 0 and f(i, 0, [3]) == 1:
         cnt_20 += 1
    if f(i, 0, [2, 4]) == 1 and f(i, 0, [2]) == 0:
         sum_21 += i

print(f"#19 - {min(lst_19)}")
print(f"#20 - {cnt_20}")
print(f"#21 - {sum_21}")
