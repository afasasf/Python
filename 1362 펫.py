cnt = 0
while True:
    o, w = map(int, input().split())
    if o == 0 and w == 0:
        break
    die = False
    while True:
        a = [*input().split()]
        if a[0] == '#' and a[1] == '0':
            break
        if w > 0:
            if a[0] == 'E':
                w -= int(a[1])
            elif a[0] == 'F':
                w += int(a[1])
        if w <= 0:
            die = True
    cnt += 1
    if w <= 0:
        print(f'{cnt} RIP')
    elif o // 2 < w < o * 2:
        print(f'{cnt} :-)')
    else:
        print(f'{cnt} :-(')