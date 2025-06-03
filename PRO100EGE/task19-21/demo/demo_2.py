def f(x1, x2, pos, win_pos) -> int:
    if x1 + x2 >= _:
        return pos in win_pos
    if pos > max(win_pos):
        return 0

    moves = [

    ]
    # If our player lose
    if pos % 2 != max(win_pos) % 2:
        return all(moves)
    else:
        return any(moves)
