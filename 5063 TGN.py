a = int(input())

for _ in range(a):
    r, e, c = list(map(int, input().split()))

    if r > e - c: print("do not advertise")
    elif e - c == r: print("does not matter")
    else: print("advertise")