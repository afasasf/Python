a, b = map(int, input().split())

m = max(a,b)
n = min(a,b)
d = m-n-1

if n == m or n+1 == m:
    d = 0
print(d)

for i in range(n+1, m):
    print(i, end=' ')