from itertools import combinations


a = []
for _ in range(int(input())):
    name, d, m, y = input().split()
    a.append([name, int(d), int(m), int(y)])
a.sort(key=lambda x:(x[3],x[2],x[1]))
print(a[-1][0])
print(a[0][0])