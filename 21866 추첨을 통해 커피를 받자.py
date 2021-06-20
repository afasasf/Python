a = list(map(int, input().split()))
s = [100, 100, 200, 200, 300, 300, 400, 400, 500]

sum, h = 0, 0

for i in range(9):
    if a[i] > s[i]:
        h= 1
    sum += a[i]
if h:
    print("hacker")
else:
    print("draw" if sum >= 100 else "none")