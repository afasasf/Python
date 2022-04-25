n = int(input())
a = [*map(int, input().split())]
a.sort();b = 0

for i in range(len(a)+1):
    b += sum(a[0:i])
print(b)