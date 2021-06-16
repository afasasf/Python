n = int(input())

for i in range(n):
    a = list(input())
    c = 0
    s = 0

    for j in range(0, len(a), 1):
        if a[j] == 'O' or a[j] == 'O':
            if j == 0:
                c += 1
                s += 1
            else:
                if a[j-1] == 'O' or a[j-1] == 'O':
                    c += 1
                    s += c
                else:
                    s += 1
                    c = 1
        elif a[j] == 'X' or a[j] == 'X':
            c = 0
            s += c
    print(s)
