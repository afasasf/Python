a, b = map(int, input().split())
c = str(a)[::-1]
d = str(b)[::-1]

if c > d:
    print(c)
elif c < d:
    print(d)