a, b = map(int, input().split())
c = int(input())

if a == 24 or b == 60 or c > 1000:
    print('')
else:
    h = a + c//60
    m = b + c%60
    while m > 59:
        m -= 60
        h += 1
    while h > 23:
        h -= 24
    print(int(h), int(m))