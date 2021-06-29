n = int(input())

for i in range(n):
    a = input()
    b = int(len(a) / 2)

    if a[b - 1] == a[b]:
        print("Do-it")
    else:
        print("Do-it-Not")