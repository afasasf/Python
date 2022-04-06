a = [*map(int, input().split())];b = 0
while a[1]:
    b += 1
    if a[0] % b < 1: a[1] -= 1
    if b > a[0]: b = 0;break
print(b)