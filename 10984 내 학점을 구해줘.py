for t in range(int(input())):
    a,gpa=0,0
    for n in range(int(input())):
        c, g = map(str, input().split())
        a += int(c)
        gpa += float(c) * float(g)
    gpa = round(gpa/a,1)
    print(a, '%.1f' % gpa)