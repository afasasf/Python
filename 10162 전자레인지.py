t = int(input())
a, b, c = 300, 60, 10
a1=b1=c1=0
cnt = 0
if t >= a:
    a1 = t // a
    t = t % a
if t >= b:
    b1 = t // b
    t = t % b
if t >= c:
    c1 = t // c
    t = t % c
if t > 0:
    print('-1')
elif t == 0:
    print(a1,b1,c1)