a = list(map(int, input().split()))
b = a[0]*a[1]-a[2]

if a[0]*a[1] <= a[2]:
    print("0")
else:
    print(b)