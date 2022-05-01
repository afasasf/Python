m, p = map(int, input().split())
a = [*map(int, input().split())]
for i in a:
    print(i - (m*p), end=' ')