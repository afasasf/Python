n=int(input())
a=[*map(int,input().split())]
print(*[i for i in sorted(a)])