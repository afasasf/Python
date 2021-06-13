a = list(map(int, input().split()))

b = int(a[0])
c = int(a[2]) - int(a[1])

if c > 0:
    print("{}".format((b+c)//c))
else:
    print("-1")