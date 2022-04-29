a=[i for i in range(1, 31)]
for _ in range(28):
    b = int(input())
    a.remove(b)
print(f'{min(a)}\n{max(a)}')