a = list(map(int, input().split()))

a[0] = a[0] * a[0]

b = (a[1]*a[1]) + (a[2]*a[2])
c = (a[0]/b)
c = c ** 0.5

d, e = int(a[1] * c), int(a[2] * c)
print(d,e)