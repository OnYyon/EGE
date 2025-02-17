def f(x, c, win) -> int:
    if x >= 129:
        return c in win
    if c > max(win):
        return 0
    
    moves = [f(x + 1, c + 1, win), f(x * 2, c + 1, win)]
    if c % 2 != max(win) % 2:
        return any(moves) #move player
    else:
        return all(moves) #move enemy

for i in range(1, 128):
    if f(i, 0, [1]) == 1:
        print(f"#19 - {i}")
