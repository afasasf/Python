a = []
for _ in range(8):
    a.append(int(input()))

b = []

for i in sorted(a, reverse=True)[:5]:
    b.append(a.index(i)+1)

print(sum(sorted(a, reverse=True)[:5]))
b.sort()
print(*b)