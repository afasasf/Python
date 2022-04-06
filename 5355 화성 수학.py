t = int(input())

for _ in range(t):
    a = list(map(str, input().split()))
    c = float(a[0])
    a.remove(a[0])
    b = len(a)
    for i in range(b):
        if '@' in a[i]: c *= 3
        elif '%' in a[i]: c += 5
        elif '#' in a[i]:c -= 7  
    print(f"{c:.2f}")