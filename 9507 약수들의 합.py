b = 0
c = []
while True:
    a = int(input())
    if a == -1:
        break

    b = 0
    c = []
    for i in range(1, a):
        if a % i == 0:
            b+=i
            c.append(str(i))
    if a == b:
        print(a,'=', " + ".join(c))
    else:
        print(a, 'is NOT perfect.')