b = []
for _ in range(7):
    a = int(input())
    if a % 2 != 0:
        b.append(a)
if sum(b) == 0:
    print('-1')
else:
    print(sum(b))
    print(min(b))