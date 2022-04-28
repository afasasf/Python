p=[[0 for _ in range(101)] for _ in range(101)];res = 0
for _ in range(4):
    a=[*map(int,input().split())]
    for i in range(a[0],a[2]):
        for j in range(a[1],a[3]):
            p[i][j] = 1
for k in p:
    res += sum(k)
print(res)