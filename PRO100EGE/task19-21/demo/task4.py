def f(x, pos, win_pos, pattern):
    #print(pattern)
    if x > 37:
        return pos in win_pos
    if pos > max(win_pos):
        return 0

    moves = [
        f(x + 1, pos + 1, win_pos, f"1 rec - data: {x + 1, pos + 1, win_pos}"),
        f(x + 2, pos + 1, win_pos, f"\t2 rec - data: {x + 2, pos + 1, win_pos}"),
        f(x + 3, pos + 1, win_pos, f"\t\t3 rec - data: {x + 3, pos + 1, win_pos}"),
        f(x * 2, pos + 1, win_pos, f"\t\t\t4 rec - data: {x * 2, pos + 1, win_pos}"),
    ]
    if pos % 2 != max(win_pos) % 2:
        return any(moves)
    else:
        return all(moves)

# Indexes start with 1
lst = []
for i in range(1, 38):
    if f(i, 0, [2], f"call-1{i}") == 1:
        print(f"#19 - {i}")
    if f(i, 0, [1], f"call-2{i}") == 0 and f(i, 0, [3], f"call-2{i}") == 1:
        lst.append(i)
    if f(i, 0, [2, 4], f"call-3{i}") == 1 and f(i, 0, [2], f"call-3{i}") == 0:
        print(f"#21 - {i}")
print(f"#20 - {sorted(lst)}")
