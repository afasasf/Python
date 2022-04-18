a = []
for _ in range(int(input())):
    a.append(input().split())
a=sorted(a, key=lambda x:x[1])
print(a[0][0])