m = int(input())
n = int(input())
a = []

for i in range(m, n+1):
    if i == 1:
        continue
    elif i == 2:
        a.append(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i-1:
                a.append(i)
if len(a) == 0:
    print('-1')
else:
    print(f'{sum(a)}\n{min(a)}')