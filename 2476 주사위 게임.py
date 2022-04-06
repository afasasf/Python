t = int(input())
cnt = []
for i in range(t):
    a = list(map(int, input().split()))
    b=a;b.sort()
    if len(set(a)) == 1:
        cnt.append(10000 + b[1] * 1000)
    elif len(set(a)) == 2: 
        cnt.append(1000 + b[1] * 100)
    elif len(set(a)) == 3:
        cnt.append(max(b) * 100)
print(max(cnt))