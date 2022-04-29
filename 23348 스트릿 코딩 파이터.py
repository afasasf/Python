d=[*map(int,input().split())]
res=[]
for _ in range(int(input())):
    b=0
    for _ in range(3):
        a=[*map(int,input().split())]
        for i in range(3):
            b += a[i] * d[i]
    res.append(b)
print(max(res))