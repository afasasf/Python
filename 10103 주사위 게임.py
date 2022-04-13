n = int(input())
a = 100 #창영
b = 100 #상덕

for i in range(n):
    x, y = map(int, input().split())

    if x > y:
        b -= x
    elif x < y:
        a -= y
    elif x == y:
        continue
print(f'{a}\n{b}')