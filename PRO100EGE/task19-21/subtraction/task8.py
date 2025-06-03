def f(x, c, win):
    if x == 0:  # Указываем условие окончания игры
        return c in win
    if c > max(win):
        return 0

    moves = []  # Изначально список ходов пустой
    if x - 2 >= 0:  # Если можем сделать ход -2
        moves.append(f(x - 2, c + 1, win))  # То добавляем его в список moves
    if x - 3 >= 0:  # Если можем сделать ход -3
        moves.append(f(x - 3, c + 1, win))  # То добавляем его в список moves
    if x // 2 >= 0:  # Если можем сделать ход //2
        moves.append(f(x // 2, c + 1, win))  # То добавляем его в список moves

    if c % 2 != max(win) % 2:
        return any(moves)  # Ходит наш игрок
    else:
        return all(moves)  # Ходит противник

for s in range(1, 30):
    if f(s, 0, [1]) == 0 and f(s, 0, [2]) == 1:
         print(f"19 - {s}")
    if f(s, 0, [1]) == 0 and f(s, 0, [3]) == 1:
        print(f"20 - {s}")
    if f(s, 0, [2, 4]) == 1 and f(s, 0, [2]) == 0:
        print(f"21 - {s}")
