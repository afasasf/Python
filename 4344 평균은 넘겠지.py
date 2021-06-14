c = int(input())

for i in range(c):
    a, *b = map(int, input().split())
    avg = sum(b)/a
    d = 0
    
    for j in range(len(b)):
        if b[j] > avg:
            d += 1

    print('%0.3f' % round(d/a*100, 3) + "%")