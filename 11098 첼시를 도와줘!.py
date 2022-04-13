n = int(input())
for _ in range(n):
    p = int(input())
    max = 0
    name = ""
    for _ in range(p):
        c, name1 = input().split()
        if int(c) > max: 
            max = int(c)
            name = name1
    print(name)