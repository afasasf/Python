a, b = map(int, input().split())

def r(i):
    return int(str(i)[::-1])

print(r(r(a) + r(b)))