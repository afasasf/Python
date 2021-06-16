g = []
g += ['A+'] * 5
g += ['A0'] * 10
g += ['B+'] * 15
g += ['B0'] * 5
g += ['C+'] * 10
g += ['C0'] * 3
g += ['F'] * 2

a = list(map(int, input().split()))
b = int(input())

print(g[a.index(b)])