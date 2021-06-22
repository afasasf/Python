a = []

for i in range(9):
    a.append(int(input()))

sum = sum(a)
b = 0
c = 0

for i in range(8):
    for j in range(i+ 1, 9):
        if sum - (a[i] + a[j]) == 100:
            b = a[i]
            c = a[j]
a.remove(b)
a.remove(c)
a.sort()
for i in a:
    print(i)