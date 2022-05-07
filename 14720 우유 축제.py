n=int(input())
a=[*map(int,input().split())]
cnt=0
for i in range(n):
    if a[i] == cnt % 3:
        cnt += 1
print(cnt)