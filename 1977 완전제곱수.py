m = int(input())
n = int(input())
a = []

for i in range(m, n+1):
    b = int(i ** 0.5)
    if i == b ** 2: a.append(i)
if a == []: print(-1)
else: print(f'{sum(a)}\n{min(a)}')