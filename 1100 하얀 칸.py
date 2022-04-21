a = [];b = 0
for _ in range(8):
    a.append(input())
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            if a[i][j] == 'F':
                b += 1
print(b)
