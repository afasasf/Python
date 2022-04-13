t = int(input())
a = [*map(int, input().split())]
c = 0
b = 0
for i in a:
    if i == 1:
        c += 1
        b += c
    else:
        c = 0
print(b)