s = int(input())

for _ in range(s):
    r, p = input().split()

    for i in range(len(p)):
        for j in range(int(r)):
            print(p[i], end='')
    print()