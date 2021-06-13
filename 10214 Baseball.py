t = int(input())

for i in range(t):
    a = 0
    b = 0
    for _ in range(9):
        y, k = map(int, input().split())
        a += y
        b += k

    if a > b:
        print("Yonsei")
    elif a < b:
        print("Korea")
    else:
        print("Draw")