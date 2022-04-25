a = [*map(int, input().split())];b = min(a)
while True:
    cnt = 0
    for i in range(5):
        if b % a[i] == 0:
            cnt += 1
    if cnt > 2:
        print(b)
        break
    b += 1