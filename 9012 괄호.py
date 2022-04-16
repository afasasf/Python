for _ in range(int(input())):
    a, c = [*input()], 0

    for i in a:
        if i=='(': c += 1
        else: c -= 1
        if c == -1: break

    if c == 0: print('YES')
    else: print('NO')