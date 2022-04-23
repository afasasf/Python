for _ in range(int(input())):
    a = [*map(str, input().split())]
    print(*a[2:], *a[:2])