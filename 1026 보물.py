n=int(input())
a=[*map(int,input().split())]
b=[*map(int,input().split())]
a.sort();b.sort(reverse=True)
res=0
for i in range(n):
    res+=a[i]*b[i]
print(res)